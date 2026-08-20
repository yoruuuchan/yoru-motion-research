#!/usr/bin/env python3
"""Build the Locomotion layout index — navigation only, no copied code.

Locomotion ships without a LICENSE (`legal/license-tracker.yml` records it as
`reference_only`), so unlike the Shotcraft shots we cannot bring the
implementations into this repository. What we can do is point at them exactly.

Both halves turned out to be publicly addressable at a pinned commit:

- source   src/templates/<base>/Composition.tsx
- preview  public/videos/<file>          (all 427 present upstream)

So the index gives every kept variant a link that plays in the browser and a
link to the code that made it, without redistributing either.

    python scripts/build-layout-index.py
"""

from __future__ import annotations

import bz2
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SNAPSHOT = REPO / "curation" / "locomotion-2026-08-19.json.bz2"
OUT = REPO / "layouts" / "README.md"

UPSTREAM = "https://github.com/locomotion-pro/locomotion"
# Pinned so the links keep resolving if upstream moves. Verified 2026-08-20:
# all 61 curated template directories and all 427 preview files exist at this
# commit, which is also the current HEAD (last pushed 2026-04-01).
COMMIT = "d42711f950c2c6776056df4d9c7c729d4490ba50"

SOURCE = f"{UPSTREAM}/blob/{COMMIT}/src/templates"
PREVIEW = f"{UPSTREAM}/blob/{COMMIT}/public/videos"

ORDER = {"keep": 0, "maybe": 1, "reject": 2}

# Written from watching the rendered clips, frame by frame — upstream is
# reference_only, so the source was never read. Each line says what is visibly
# on screen and what the shot is for, in the words you would actually search
# with. Only the 20 templates that kept at least one skin are described.
DESCRIPTIONS = {
    "app-feature-callout": "浏览器窗弹入 → 窗内内容填好 → 一个深色药丸标签从右侧飞进来贴在窗角。给某个功能点名。",
    "appointment-booking": "卡片弹入，可选项一条条往下堆出来，最后底部实心按钮压上收口。表单、选时间、任何「选一个再确认」。",
    "bar-chart-reveal": "柱子从左到右一根根长起来，数值跟着柱顶一起冒出来，明度从浅到深。比大小。",
    "before-after": "左边先把「以前」立起来（✗ 逐条落），中间一个箭头，右边再给「现在」（✓ 逐条落）。对比、改造前后。",
    "bento-grid": "大小交错的格子按顺序一格一格弹进来，每格一个图标一个短标签。能力总览、做过什么。",
    "changelog": "卡片弹入，更新条目一条条打勾出现，每条底下一根细线。版本更新、这次改了什么。",
    "concept-breakdown": "小眉题 + 大问句标题先立住，要点一条条淡入上浮。解释一个概念。",
    "countdown-timer": "三个数字格持续翻动递减，一路跑到 00 00 00。倒计时、快开始了。",
    "day-summary": "卡片弹入，主数字从 0 滚上去，同时下面的任务条一条条打勾。日报、这段时间做完了什么。",
    "feature-showcase": "大标题立住不动，三个方框卡从左到右一个个弹入。三点并列、卖点排排站。",
    "modal-explainer": "背景压暗，白卡弹入，卡内按页翻步骤，底下有分页点和一条走着的进度条。分步讲解。",
    "patient-journey": "一条横线上编号圆点 1→2→3→4 依次亮起，虚线连接，每个点下面挂标签。流程、一段旅程怎么走完。",
    "payment-flow": "三个带编号的小方框横排弹入，之间用短横线连接。紧凑版流程，比 patient-journey 占地小。",
    "portfolio-breakdown": "圆环从 12 点方向画出来，右边图例一条条跟上，环上分段由深到浅。占比、时间花在哪。",
    "product-reveal": "商品图卡弹入，名称淡入，价格出现，旁边跟一个划掉的原价。单品、商品。",
    "screen-showcase": "浏览器窗弹入，窗内内容块一块块填满，右侧编号功能列表一条条出现。产品界面展示。",
    "social-post": "推文卡弹入（头像 + 用户名），正文淡入，底部三个互动数字滚动计数上去。社交截图、口碑。",
    "staggered-words": "大字一个词一个词错峰弹入。标题、口号。",
    "step-explainer": "标题下步骤逐条出现，每条带 01/02/03 编号和一条从左画到右的下划线。步骤说明。",
    "typewriter-reveal": "光标闪着，一个字一个字把句子打出来，打完光标继续闪。打字机标题。",
}


def main() -> None:
    rows = json.loads(bz2.open(SNAPSHOT).read())["selected"]

    bases: dict[str, list[dict]] = {}
    for row in rows:
        bases.setdefault(row["base"], []).append(row)

    kept = {b for b, rs in bases.items() if any(r["status"] == "keep" for r in rs)}
    maybe_only = {
        b
        for b, rs in bases.items()
        if b not in kept and any(r["status"] == "maybe" for r in rs)
    }
    rejected = set(bases) - kept - maybe_only

    keep_rows = sum(1 for r in rows if r["status"] == "keep")

    lines = [
        "# Layouts — 版式库（导航）",
        "",
        "Locomotion 的版式模板。**这里没有代码**——上游没有 LICENSE 文件，",
        "授权状态是 `reference_only`（见 [`../legal/license-tracker.yml`](../legal/license-tracker.yml)），",
        "所以只能导航过去，不能把实现搬进来。",
        "",
        f"链接全部钉在上游 commit [`{COMMIT[:7]}`]({UPSTREAM}/tree/{COMMIT})，上游改动了也不会失效。",
        "「看片」直接在 GitHub 页面里播，不用下载。",
        "",
        f"- 候选 {len(rows)} 个 = {len(bases)} 个版式 × 7 套皮肤",
        f"- 留下 **{keep_rows}** 个，分布在 **{len(kept)}** 个版式里",
        "",
        "> 皮肤只是换色换质感，版式和节奏在 7 套之间是一样的——所以同一个版式下",
        "> 留哪几套皮肤，读的是配色偏好，不是版式偏好。",
        "",
        "> 留下的 20 个版式各写了一句描述，是**逐帧看渲染结果**写的——上游源码不能读，",
        "> 所以描述里说的都是画面上看得见的动作，不是代码里的实现。待定和全否的没写。",
        "",
        "---",
        "",
        "## 留下的版式",
        "",
    ]

    for base in sorted(kept):
        lines += render_base(base, bases[base])

    if maybe_only:
        lines += [
            "---",
            "",
            "## 待定的版式",
            "",
            "没有一套皮肤被留下，但也没有全否——版式本身还没定。",
            "",
        ]
        for base in sorted(maybe_only):
            lines += render_base(base, bases[base])

    lines += [
        "---",
        "",
        "## 全否的版式",
        "",
        f"以下 {len(rejected)} 个版式的 7 套皮肤全部否决。负样本保留在",
        "[`../curation/locomotion-2026-08-19.json.bz2`](../curation/locomotion-2026-08-19.json.bz2)，",
        "是给未来预筛新素材用的下调依据，不要删。",
        "",
        "  ".join(f"`{b}`" for b in sorted(rejected)),
        "",
    ]

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"{len(bases)} bases -> {OUT.relative_to(REPO)}")
    print(f"  keep {len(kept)} | maybe-only {len(maybe_only)} | all-reject {len(rejected)}")


def render_base(base: str, rows: list[dict]) -> list[str]:
    lines = [f"### {base}", ""]
    if base in DESCRIPTIONS:
        lines += [DESCRIPTIONS[base], ""]
    lines += [f"[上游代码 →]({SOURCE}/{base}/Composition.tsx)", ""]
    by_status: dict[str, list[dict]] = {}
    for row in sorted(rows, key=lambda r: (ORDER[r["status"]], r["style"])):
        by_status.setdefault(row["status"], []).append(row)

    for status, label in (("keep", "留下"), ("maybe", "待定")):
        picked = by_status.get(status, [])
        if picked:
            marks = ", ".join(
                f"`{r['style']}` [看片]({PREVIEW}/{r['file']})" for r in picked
            )
            lines.append(f"- **{label}** {marks}")
    if by_status.get("reject"):
        styles = ", ".join(f"`{r['style']}`" for r in by_status["reject"])
        lines.append(f"- 否决 {styles}")
    lines.append("")
    return lines


if __name__ == "__main__":
    main()
