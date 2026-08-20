#!/usr/bin/env python3
"""Build the browsable shot library from the Video Shotcraft curation snapshot.

The curation JSON says which shots Yoru kept; the upstream checkout holds the
Apache-2.0 implementations and the Chinese recipe cards. This script joins them
into `shots/`, one directory per card, so the library is readable straight from
GitHub without a local server and without watching a video first.

    python scripts/build-shot-library.py [--upstream ../video-shotcraft]

Verdicts are authoritative. A card is only copied wholesale when every one of
its styles carries the same verdict. Cards that mix verdicts are split per
style, and any card whose styles cannot be matched to implementation files
unambiguously is reported instead of guessed — copying a rejected shot into the
keep tree would silently overwrite a decision she already made.
"""

from __future__ import annotations

import argparse
import bz2
import json
import re
import shutil
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SNAPSHOT = REPO / "curation" / "video-shotcraft-2026-08-20.json.bz2"
META = REPO / "curation" / "video-shotcraft-2026-08-20.meta.json"
OUT = REPO / "shots"

CATEGORY_LABELS = {
    "interaction": "交互与功能演示",
    "camera": "运镜与空间",
    "ui-entrance": "界面登场与陈列",
    "opening": "开场与品牌",
    "data": "数据与指标",
    "effects": "光效与强调",
    "transition": "转场",
    "rhythm": "节奏与蒙太奇",
    "outro": "收尾",
    "typography": "文字与字卡",
}

# Implementation filenames are PascalCase renderings of the style key, often with
# an extra word: drift-assembly -> LetterformDriftAssembly, tracking-expand ->
# TrackingExpandReveal. Matching on the squashed lowercase form covers both.
def squash(text: str) -> str:
    return re.sub(r"[^a-z0-9]", "", text.lower())


def read_recipe(path: Path) -> dict:
    """Pull the front-matter fields out of a shot recipe card."""
    if not path.is_file():
        return {}
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        return {}
    fields = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip()
    return fields


def recipe_section(path: Path, heading: str) -> str:
    """Return one `## heading` section of a recipe card, without the heading."""
    if not path.is_file():
        return ""
    text = path.read_text(encoding="utf-8")
    match = re.search(rf"^## {re.escape(heading)}\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    return match.group(1).strip() if match else ""


def match_styles_to_files(styles: list[str], files: list[Path]) -> dict[str, Path] | None:
    """Map each style key to its implementation file, or None if ambiguous.

    Requires a 1:1 population first — a card with six styles and four files
    cannot be split safely no matter how well the names read. Names that do not
    overlap at all (input-morph-assemble / InputMorphsIntoLogo) are resolved by
    elimination, but only down to the last remaining pair.
    """
    if len(styles) != len(files):
        return None
    mapping: dict[str, Path] = {}
    remaining = list(files)
    unresolved = []
    for style in styles:
        key = squash(style)
        hits = [f for f in remaining if key in squash(f.stem) or squash(f.stem) in key]
        if len(hits) == 1:
            mapping[style] = hits[0]
            remaining.remove(hits[0])
        else:
            unresolved.append(style)
    if len(unresolved) == 1 and len(remaining) == 1:
        mapping[unresolved[0]] = remaining.pop()
        unresolved.pop()
    return mapping if not unresolved and not remaining else None


def name_only_matches(styles: list[str], files: list[Path]) -> dict[str, Path]:
    """Match only the styles whose name a file actually carries; skip the rest."""
    mapping: dict[str, Path] = {}
    remaining = list(files)
    for style in styles:
        key = squash(style)
        hits = [f for f in remaining if key in squash(f.stem) or squash(f.stem) in key]
        if len(hits) == 1:
            mapping[style] = hits[0]
            remaining.remove(hits[0])
    return mapping


def rewrite_imports(text: str) -> str:
    """Re-point upstream's shared modules at our `_kernel/`, one level deeper."""
    text = text.replace("../../_fixtures/", "../../../_kernel/")
    text = text.replace("../../_textures/", "../../../_kernel/textures/")
    return text


def card_readme(card: str, category: str, recipe: Path, rows: list[dict], upstream: dict) -> str:
    fields = read_recipe(recipe)
    permalink = f"{upstream['repo']}/blob/{upstream['commit']}"
    lines = [
        f"# {card}",
        "",
        f"**{CATEGORY_LABELS.get(category, category)}**",
        "",
    ]
    if fields.get("一句话"):
        lines += [fields["一句话"], ""]
    for label in ("适用", "时长", "能量"):
        if fields.get(label):
            lines.append(f"- **{label}** {fields[label]}")
    lines.append("")

    lines += ["## 我的判断", "", "| 变体 | 判断 | 分数 | 预览 |", "|---|---|---:|---|"]
    for row in sorted(rows, key=lambda r: (-r["score"], r["style"])):
        score = row["score"] or ""
        lines.append(
            f"| `{row['style']}` | {row['verdict']} | {score} | [看片]({row['previewUrl']}) |"
        )
        if row.get("note"):
            lines.append(f"| | | | 备注：{row['note']} |")
    lines.append("")

    for heading in ("意图", "参数表", "已知坑"):
        body = recipe_section(recipe, heading)
        if body:
            lines += [f"## {heading}", "", body, ""]

    lines += [
        "## 出处",
        "",
        f"- 参数卡原文 [{recipe.name}]({permalink}/references/shots/{category}/{recipe.name})",
        f"- 上游实现 [{category}/{card}]({permalink}/demos/{category}/{card})",
        "- 授权 Apache-2.0，可改可用，见 [`../../../LICENSE`](../../../LICENSE) 与 [`../../../NOTICE.md`](../../../NOTICE.md)",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--upstream", default=str(REPO.parent / "video-shotcraft"))
    args = parser.parse_args()
    up = Path(args.upstream).resolve()

    snapshot = json.loads(bz2.open(SNAPSHOT).read())
    rows = next(v for v in snapshot.values() if isinstance(v, list))
    meta = json.loads(META.read_text(encoding="utf-8"))
    upstream = {"repo": meta["upstream"]["repo"], "commit": meta["upstream"]["commit"]}

    cards: dict[str, list[dict]] = {}
    for row in rows:
        cards.setdefault(row["card"], []).append(row)

    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "_kernel").mkdir(parents=True)

    shutil.copy2(up / "LICENSE", OUT / "LICENSE")
    for name in ("Fixtures.tsx", "Motion.tsx"):
        text = (up / "demos" / "_fixtures" / name).read_text(encoding="utf-8")
        (OUT / "_kernel" / name).write_text(rewrite_imports(text), encoding="utf-8")
    shutil.copytree(up / "demos" / "_textures", OUT / "_kernel" / "textures")

    placed: dict[str, list[tuple[str, str, list[dict]]]] = {"keep": [], "maybe": []}
    partial: list[tuple[str, list[str]]] = []
    no_code: list[str] = []

    for card, card_rows in sorted(cards.items()):
        category = card_rows[0]["recipePath"].split("/")[2]
        recipe = up / "references" / "shots" / category / f"{card}.md"
        src = up / "demos" / category / card
        files = sorted(src.glob("*.tsx")) if src.is_dir() else []
        verdicts = {r["verdict"] for r in card_rows}

        if verdicts == {"reject"}:
            continue

        if len(verdicts) == 1:
            bucket = card_rows[0]["verdict"]
            groups = {bucket: (card_rows, files)}
        else:
            styles = [r["style"] for r in card_rows]
            mapping = match_styles_to_files(styles, files)
            if mapping is None:
                # No clean 1:1. Fall back to name matching alone: a file travels
                # only with the style whose name it carries, so a rejected style
                # can never ride along on a keep. Styles the upstream never
                # implemented still get a directory — the recipe card and the
                # preview are the reference, the code was only ever a bonus.
                mapping = name_only_matches(styles, files)
                orphans = sorted(f.name for f in files if f not in mapping.values())
                if orphans:
                    partial.append((f"{category}/{card}", orphans))
            groups = {}
            for bucket in ("keep", "maybe"):
                picked = [r for r in card_rows if r["verdict"] == bucket]
                if picked:
                    groups[bucket] = (picked, [mapping[r["style"]] for r in picked if r["style"] in mapping])

        for bucket, (bucket_rows, bucket_files) in groups.items():
            dest = OUT / bucket / category / card
            dest.mkdir(parents=True, exist_ok=True)
            for f in bucket_files:
                dest.joinpath(f.name).write_text(
                    rewrite_imports(f.read_text(encoding="utf-8")), encoding="utf-8"
                )
            dest.joinpath("README.md").write_text(
                card_readme(card, category, recipe, bucket_rows, upstream), encoding="utf-8"
            )
            placed[bucket].append((category, card, bucket_rows))
            if not bucket_files:
                no_code.append(f"{bucket}/{category}/{card}")

    write_index(OUT, placed, upstream, partial)
    write_notice(OUT, upstream, meta)

    print(f"keep  {len(placed['keep'])} cards")
    print(f"maybe {len(placed['maybe'])} cards")
    if no_code:
        print(f"\nrecipe card only, no implementation upstream ({len(no_code)}):")
        for item in no_code:
            print(f"  {item}")
    if partial:
        print(f"\nimplementation files left behind, no style claims them ({len(partial)}):")
        for card_path, orphans in partial:
            print(f"  {card_path}: {', '.join(orphans)}")


def write_index(out: Path, placed: dict, upstream: dict, partial: list) -> None:
    lines = [
        "# Shots — 镜头库",
        "",
        "从 Video Shotcraft 筛出来的镜头动作。一个目录一条参考：`README.md` 说它是什么、",
        "参数怎么调、你当时怎么判断的，旁边的 `.tsx` 就是实现。",
        "",
        "- `keep/` — 认可的，可以直接拿去用",
        "- `maybe/` — 待定的，代码留着但不进主线",
        "- `_kernel/` — 所有实现共用的两个模块（缓动/插值 + 占位 UI）",
        "",
        f"上游 {upstream['repo']} @ `{upstream['commit'][:7]}`，Apache-2.0。",
        "改动见 [`NOTICE.md`](NOTICE.md)。",
        "",
    ]
    for bucket, title in (("keep", "keep — 认可"), ("maybe", "maybe — 待定")):
        lines += [f"## {title}", ""]
        by_cat: dict[str, list] = {}
        for category, card, rows in placed[bucket]:
            by_cat.setdefault(category, []).append((card, rows))
        for category in sorted(by_cat, key=lambda c: -len(by_cat[c])):
            label = CATEGORY_LABELS.get(category, category)
            lines += [f"### {label} · `{category}`", ""]
            for card, rows in sorted(by_cat[category]):
                best = max(r["score"] for r in rows)
                mark = f" **{best}分**" if best else ""
                styles = ", ".join(f"`{r['style']}`" for r in rows)
                lines.append(f"- [{card}]({bucket}/{category}/{card}/){mark} — {styles}")
            lines.append("")
    if partial:
        lines += [
            "## 上游还有没收录的实现文件",
            "",
            "这些卡的目录里还剩下一些 `.tsx`，文件名跟你评过的任何变体都对不上——",
            "多半是上游自己的迭代版本，没有单独进过筛选。没有判断依据就不搬，",
            "想看的话去上游对应目录。",
            "",
        ]
        for card_path, orphans in partial:
            lines.append(f"- `{card_path}` — {', '.join(orphans)}")
        lines.append("")
    (out / "README.md").write_text("\n".join(lines), encoding="utf-8")


def write_notice(out: Path, upstream: dict, meta: dict) -> None:
    text = f"""# NOTICE

本目录下的 `.tsx` 实现来自 Video Shotcraft，按 Apache License 2.0 使用。

- 上游仓库 {upstream['repo']}
- 上游 commit `{upstream['commit']}`（{meta['upstream']['commitDate']}）
- 原始授权文件保留在 [`LICENSE`](LICENSE)

## 我们做了什么改动

1. **只收录筛选留下的部分。** 上游 209 个候选里，`keep/` 和 `maybe/` 只放留下和待定的，
   否决的不复制（判断记录仍完整保存在 `curation/`）。
2. **改了 import 路径。** 上游的 `demos/_fixtures/` 和 `demos/_textures/` 在这里合并成
   `_kernel/`，所有实现文件里对应的相对路径同步改写。除此之外实现代码未做修改。
3. **每个目录新增了 `README.md`**，由 `scripts/build-shot-library.py` 从上游的中文参数卡
   和我们自己的筛选记录生成。这部分是我们写的，不属于上游。

上游对镜头手法的来源与法律边界另有说明，见上游仓库的
`references/shots/ATTRIBUTION.md`。
"""
    (out / "NOTICE.md").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
