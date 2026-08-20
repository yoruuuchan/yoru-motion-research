#!/usr/bin/env python3
"""Build the machine-readable candidate datasets consumed by review/index.html.

One adapter per upstream source. The review console itself stays source-agnostic:
everything source-specific (stable id shape, preview URLs, provenance fields that
end up in the export) is decided here and baked into review/datasets/*.json.

    python scripts/build-review-datasets.py
    python scripts/build-review-datasets.py --check

Sibling checkouts are expected next to this repository:

    <parent>/locomotion-free/public/videos/*.mp4
    <parent>/video-shotcraft/gallery/api/library.json
"""

from __future__ import annotations

import argparse
import bz2
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PARENT = ROOT.parent
DATASETS = ROOT / "review" / "datasets"

DATASET_SCHEMA = "yoru-motion-review-dataset/v1"

# Media lives outside this repository. Paths are relative to review/index.html so
# the console works when the parent directory is served (see review/serve.py).
LOCOMOTION_DIR = PARENT / "locomotion-free" / "public" / "videos"
LOCOMOTION_MEDIA_BASE = "../../locomotion-free/public/videos/"
LOCOMOTION_SNAPSHOT = ROOT / "curation" / "locomotion-2026-08-19.json.bz2"
LOCOMOTION_STYLES = ["default", "brutalist", "dark", "glass", "minimal", "neo", "rounded"]

SHOTCRAFT_DIR = PARENT / "video-shotcraft"
SHOTCRAFT_MEDIA_BASE = "../../video-shotcraft/gallery/media/"
SHOTCRAFT_REPO = "https://github.com/Vincentwei1021/video-shotcraft"
SHOTCRAFT_PAGES = "https://vincentwei1021.github.io/video-shotcraft/"

# Resolved 2026-08-20 against the GitHub API: main HEAD, and the blob sha1 of
# gallery/api/library.json at that commit. The local library.json is compared
# against the blob sha1 on every build, so a refreshed checkout that no longer
# matches this commit is reported instead of silently mislabelled.
SHOTCRAFT_COMMIT = "0d6f0b57f0d4d6700761644c07f7ef03c3e50234"
SHOTCRAFT_COMMIT_DATE = "2026-08-14T04:17:12Z"
SHOTCRAFT_LIBRARY_BLOB_SHA1 = "fcbc96b2b8a08959ace510460988cc012291caa3"


def git_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def build_locomotion() -> dict:
    """427 rendered variants, one candidate per mp4, id = locomotion/<base>/<style>."""
    files = sorted(p.name for p in LOCOMOTION_DIR.glob("*.mp4"))
    if not files:
        raise SystemExit(f"no locomotion mp4s under {LOCOMOTION_DIR}")

    candidates = []
    for name in files:
        stem = name[: -len(".mp4")]
        style = "default"
        for candidate_style in LOCOMOTION_STYLES:
            if candidate_style != "default" and stem.endswith("-" + candidate_style):
                style = candidate_style
                stem = stem[: -len("-" + candidate_style)]
                break
        stable_id = f"locomotion/{stem}/{style}"
        candidates.append(
            {
                "id": stable_id,
                "title": stem.replace("-", " "),
                "badge": style,
                "subtitle": name,
                "group": stem,
                "facet": style,
                "primary": style == "default",
                "search": " ".join([stem, style, name, stable_id]),
                "sources": [LOCOMOTION_MEDIA_BASE + name],
                "meta": [["template", stem], ["style", style]],
                "links": [],
                # Fields copied verbatim into every exported row.
                "export": {
                    "source": "locomotion",
                    "file": name,
                    "base": stem,
                    "style": style,
                },
            }
        )

    # The 2026-08-19 review is the source of truth for this batch: it seeds the
    # console so historical verdicts stay visible, and it doubles as validation
    # that the candidate list still resolves to exactly those stable ids.
    snapshot = json.loads(bz2.decompress(LOCOMOTION_SNAPSHOT.read_bytes()))
    seed = {
        record["id"]: {
            "status": record["status"],
            "score": record.get("score", 0),
            "note": record.get("note", ""),
        }
        for record in snapshot["selected"]
    }
    built = {c["id"] for c in candidates}
    if built != set(seed):
        raise SystemExit(
            f"locomotion candidates drifted from the snapshot: "
            f"+{sorted(built - set(seed))[:5]} -{sorted(set(seed) - built)[:5]}"
        )

    return {
        "schema": DATASET_SCHEMA,
        "key": "locomotion",
        "label": "Locomotion",
        "source": "locomotion",
        "storageKey": "yoru-locomotion-curation-v1",
        "totalCandidates": len(candidates),
        "facetLabel": "style",
        "facetOptions": [{"value": s, "label": s} for s in LOCOMOTION_STYLES],
        "primaryLabel": "default only",
        "allLabel": "all variants",
        "defaultMode": "primary",
        "hint": (
            "stable id 固定为 <code>locomotion/模板名/style</code>。"
            "2026-08-19 的 427 条判断已作为底稿载入，你改动的部分会覆盖它并存在本浏览器。"
        ),
        "upstream": {
            "repo": "https://github.com/locomotion-pro/locomotion",
            "snapshot": "curation/locomotion-2026-08-19.json.bz2",
        },
        "seed": seed,
        "candidates": candidates,
    }


def build_shotcraft() -> dict:
    """209 previewable styles across 152 shot cards, id = video-shotcraft/<card>/<style>."""
    library_path = SHOTCRAFT_DIR / "gallery" / "api" / "library.json"
    raw = library_path.read_bytes()
    blob_sha1 = git_blob_sha1(raw)
    commit_verified = blob_sha1 == SHOTCRAFT_LIBRARY_BLOB_SHA1
    if not commit_verified:
        print(
            f"warning: local library.json blob {blob_sha1} != pinned {SHOTCRAFT_LIBRARY_BLOB_SHA1};"
            f" the recorded upstream commit may no longer describe this data",
            file=sys.stderr,
        )

    library = json.loads(raw.decode("utf-8"))
    categories = library["categories"]
    source_base = f"{SHOTCRAFT_REPO}/blob/{SHOTCRAFT_COMMIT}/"

    candidates = []
    for card in library["cards"]:
        card_name = card["name"]
        category = card.get("category", "")
        cat_label = categories.get(category, {})
        category_label = f"{category} · {cat_label.get('zh', '')}".strip(" ·")
        recipe_path = card.get("source", "")
        for style_index, style in enumerate(card.get("styles", [])):
            media = style.get("media") or {}
            url = media.get("url")
            if not url:
                continue  # not previewable, so not a review candidate
            file_name = url.split("/")[-1].split("?")[0]
            style_key = style["key"]
            stable_id = f"video-shotcraft/{card_name}/{style_key}"
            preview_url = SHOTCRAFT_PAGES + "media/" + file_name
            description = style.get("description") or card.get("summary") or ""
            use = style.get("use") or card.get("use") or ""
            meta = [
                ["card", card_name],
                ["style", style_key],
                ["category", category_label],
            ]
            if description:
                meta.append(["描述", description])
            if use:
                meta.append(["用途", use])
            if card.get("duration"):
                meta.append(["时长", card["duration"]])
            if card.get("energy"):
                meta.append(["能量", card["energy"]])
            candidates.append(
                {
                    "id": stable_id,
                    "title": style.get("label") or style_key,
                    "badge": category,
                    "subtitle": f"{card_name} · {file_name}",
                    "group": card_name,
                    "facet": category,
                    "primary": style_index == 0,
                    "search": " ".join(
                        [card_name, style_key, category, file_name, stable_id, description, use]
                    ),
                    # Local checkout first, upstream GitHub Pages as fallback; the
                    # mp4s are never copied into this repository.
                    "sources": [SHOTCRAFT_MEDIA_BASE + file_name, preview_url],
                    "meta": meta,
                    "links": [["recipe", source_base + recipe_path]] if recipe_path else [],
                    "export": {
                        "source": "video-shotcraft",
                        "upstreamRepo": SHOTCRAFT_REPO,
                        "upstreamCommit": SHOTCRAFT_COMMIT,
                        "card": card_name,
                        "style": style_key,
                        "styleLabel": style.get("label") or style_key,
                        "category": category,
                        "categoryLabel": cat_label.get("zh", "") or category,
                        "recipePath": recipe_path,
                        "previewUrl": preview_url,
                        "file": file_name,
                    },
                }
            )

    ids = [c["id"] for c in candidates]
    if len(ids) != len(set(ids)):
        raise SystemExit("duplicate stable id in video-shotcraft candidates")

    return {
        "schema": DATASET_SCHEMA,
        "key": "video-shotcraft",
        "label": "Video Shotcraft",
        "source": "video-shotcraft",
        "storageKey": "yoru-shotcraft-curation-v1",
        "totalCandidates": len(candidates),
        "facetLabel": "category",
        "facetOptions": [
            {"value": key, "label": f"{key} · {value.get('zh', '')}".strip(" ·")}
            for key, value in categories.items()
        ],
        "primaryLabel": "one per card",
        "allLabel": "all styles",
        "defaultMode": "all",
        "hint": (
            "stable id 固定为 <code>video-shotcraft/卡名/style</code>，一个可预览 style 一条候选。"
            "预览优先走本地 <code>video-shotcraft/gallery/media/</code>，失败时回落到上游 GitHub Pages。"
        ),
        "upstream": {
            "repo": SHOTCRAFT_REPO,
            "commit": SHOTCRAFT_COMMIT,
            "commitDate": SHOTCRAFT_COMMIT_DATE,
            "commitVerified": commit_verified,
            "libraryRevision": library.get("revision", ""),
            "libraryBlobSha1": blob_sha1,
            "libraryGeneratedAt": library.get("generatedAt", ""),
            "previewBase": SHOTCRAFT_PAGES + "media/",
            "sourceBase": source_base,
        },
        "seed": {},
        "candidates": candidates,
    }


BUILDERS = {"locomotion": build_locomotion, "video-shotcraft": build_shotcraft}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if committed datasets differ")
    args = parser.parse_args()

    DATASETS.mkdir(parents=True, exist_ok=True)
    built = {key: builder() for key, builder in BUILDERS.items()}
    index = {
        "schema": DATASET_SCHEMA,
        "datasets": [
            {
                "key": key,
                "label": data["label"],
                "file": f"{key}.json",
                "totalCandidates": data["totalCandidates"],
            }
            for key, data in built.items()
        ],
    }

    outputs = {DATASETS / "index.json": index}
    outputs.update({DATASETS / f"{key}.json": data for key, data in built.items()})

    mismatches = []
    for path, payload in outputs.items():
        text = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
        if args.check:
            current = path.read_text(encoding="utf-8") if path.exists() else None
            if current != text:
                mismatches.append(path)
        else:
            path.write_text(text, encoding="utf-8")

    if mismatches:
        for path in mismatches:
            print(f"out of sync: {path.relative_to(ROOT)}", file=sys.stderr)
        return 1

    for key, data in built.items():
        print(f"ok: {key} candidates={data['totalCandidates']} seeded={len(data['seed'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
