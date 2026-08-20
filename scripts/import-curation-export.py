#!/usr/bin/env python3
"""Ingest a review-console export into curation/ as a new decision snapshot.

The console writes `yoru-motion-curation/v2`: one row per candidate, carrying the
provenance needed to trace a verdict back to its upstream shot. This validates the
export against the dataset it claims to come from, archives the uploaded bytes
byte-for-byte as bzip2, and regenerates the human-readable views.

    python scripts/import-curation-export.py ~/Downloads/video-shotcraft-curation-2026-08-20.json
    python scripts/import-curation-export.py --check curation/video-shotcraft-2026-08-20.json.bz2

Existing snapshots are never overwritten without --force: an earlier review is
evidence, not a draft.
"""

from __future__ import annotations

import argparse
import bz2
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURATION = ROOT / "curation"
DATASETS = ROOT / "review" / "datasets"

EXPECTED_SCHEMA = "yoru-motion-curation/v2"
ALLOWED_VERDICT = {"keep", "maybe", "reject", ""}

# Provenance every row must carry so an exported verdict stays traceable to the
# upstream shot it was made about.
REQUIRED_FIELDS = {
    "video-shotcraft": [
        "source", "upstreamRepo", "upstreamCommit", "card", "style",
        "category", "recipePath", "previewUrl", "verdict", "note",
    ],
    "locomotion": ["source", "base", "style", "file", "verdict", "note"],
}

VIEWS = [
    ("keep", "liked", "❤️ Liked", "明确保留、愿意进入下一轮实测的候选。"),
    ("maybe", "maybe", "○ Maybe", "有一部分喜欢、需要再看，或值得保留结构但视觉还需要筛选的候选。"),
    ("reject", "rejected", "× Rejected", "明确不喜欢 / 不适合当前工作流的候选。Reject 是有价值的负样本，必须保留。"),
]


def validate(raw: bytes) -> dict:
    data = json.loads(raw.decode("utf-8"))
    if data.get("schema") != EXPECTED_SCHEMA:
        raise SystemExit(f"unexpected schema: {data.get('schema')!r} (want {EXPECTED_SCHEMA})")

    key = data.get("dataset")
    dataset_path = DATASETS / f"{key}.json"
    if not dataset_path.exists():
        raise SystemExit(f"unknown dataset {key!r}: {dataset_path} not found")
    dataset = json.loads(dataset_path.read_text(encoding="utf-8"))

    rows = data.get("selected")
    if not isinstance(rows, list):
        raise SystemExit("selected must be a list")
    expected_total = dataset["totalCandidates"]
    if data.get("totalCandidates") != expected_total or len(rows) != expected_total:
        raise SystemExit(
            f"expected {expected_total} candidates, got totalCandidates="
            f"{data.get('totalCandidates')} selected={len(rows)}"
        )

    dataset_ids = {c["id"] for c in dataset["candidates"]}
    required = REQUIRED_FIELDS.get(key)
    if required is None:
        raise SystemExit(f"no required-field contract defined for dataset {key!r}")

    seen: set[str] = set()
    for index, row in enumerate(rows):
        missing = [f for f in ["id", *required] if f not in row]
        if missing:
            raise SystemExit(f"row {index} missing fields: {missing}")
        if row["verdict"] not in ALLOWED_VERDICT:
            raise SystemExit(f"row {row['id']} has invalid verdict {row['verdict']!r}")
        if row["id"] in seen:
            raise SystemExit(f"duplicate stable id: {row['id']}")
        seen.add(row["id"])
        if row["id"] not in dataset_ids:
            raise SystemExit(f"row {row['id']} is not a candidate in dataset {key!r}")
    if seen != dataset_ids:
        raise SystemExit(f"export is missing {len(dataset_ids - seen)} dataset candidates")

    upstream = data.get("upstream") or {}
    if key == "video-shotcraft" and not (upstream.get("repo") and upstream.get("commit")):
        raise SystemExit("upstream repo/commit missing from the export envelope")

    return data


def render_view(data: dict, verdict: str, title: str, intro: str, archive_name: str) -> str:
    rows = [r for r in data["selected"] if r["verdict"] == verdict]
    lines = [
        f"# {data['dataset']} — {title}",
        "",
        intro,
        "",
        f"> Generated from [`{archive_name}`]({archive_name}). "
        "The compressed JSON snapshot is the source of truth; do not edit this list independently.",
        "> Regenerate/check with `python scripts/import-curation-export.py --check "
        f"curation/{archive_name}`.",
        "",
        f"Total: **{len(rows)}**",
        "",
    ]
    grouped: dict[str, list[str]] = {}
    for row in rows:
        grouped.setdefault(row.get("card") or row.get("base", ""), []).append(row["style"])
    for group, styles in grouped.items():
        lines.append(f"- `{group}`: " + ", ".join(f"`{s}`" for s in styles))
    lines.append("")
    return "\n".join(lines)


def write_outputs(data: dict, raw: bytes, archive: Path, check: bool) -> int:
    counts = {v: sum(1 for r in data["selected"] if r["verdict"] == v) for v in ("keep", "maybe", "reject")}
    counts["unrated"] = sum(1 for r in data["selected"] if not r["verdict"])

    meta = {
        "schema": data["schema"],
        "dataset": data["dataset"],
        "source": data["source"],
        "upstream": data.get("upstream", {}),
        "exportedAt": data["exportedAt"],
        "totalCandidates": data["totalCandidates"],
        "counts": counts,
        "archive": archive.name,
        "compression": "bzip2",
        "uncompressedSha256": hashlib.sha256(raw).hexdigest(),
        "note": "Decompressing the archive yields the exported JSON byte-for-byte. "
                "Verdicts are authoritative and must not be rewritten by inference.",
    }
    meta_path = archive.with_suffix("").with_suffix(".meta.json")
    outputs = {meta_path: json.dumps(meta, ensure_ascii=False, indent=2) + "\n"}
    for verdict, slug, title, intro in VIEWS:
        outputs[CURATION / f"{data['dataset']}-{slug}.md"] = render_view(
            data, verdict, title, intro, archive.name
        )

    mismatches = []
    for path, text in outputs.items():
        if check:
            current = path.read_text(encoding="utf-8") if path.exists() else None
            if current != text:
                mismatches.append(path)
        else:
            path.write_text(text, encoding="utf-8")

    if mismatches:
        for path in mismatches:
            print(f"out of sync: {path.relative_to(ROOT)}", file=sys.stderr)
        return 1

    print(
        f"ok: dataset={data['dataset']} total={data['totalCandidates']} "
        f"keep={counts['keep']} maybe={counts['maybe']} reject={counts['reject']} unrated={counts['unrated']}"
    )
    print(f"    archive: {archive}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("export", help="exported JSON from the console, or an archived .json.bz2 with --check")
    parser.add_argument("--check", action="store_true", help="re-validate an archive and verify generated views")
    parser.add_argument("--date", help="snapshot date for the archive name (default: the export date)")
    parser.add_argument("--force", action="store_true", help="allow overwriting an existing archive")
    args = parser.parse_args()

    path = Path(args.export).resolve()
    raw = bz2.decompress(path.read_bytes()) if path.suffix == ".bz2" else path.read_bytes()
    data = validate(raw)

    if args.check:
        return write_outputs(data, raw, path, check=True)

    date = args.date or data["exportedAt"][:10]
    archive = CURATION / f"{data['dataset']}-{date}.json.bz2"
    if archive.exists() and not args.force:
        raise SystemExit(f"{archive.relative_to(ROOT)} already exists; pass --force to replace it")
    archive.write_bytes(bz2.compress(raw, 9))
    return write_outputs(data, raw, archive, check=False)


if __name__ == "__main__":
    raise SystemExit(main())
