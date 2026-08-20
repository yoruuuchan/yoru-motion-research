#!/usr/bin/env python3
"""Generate human-readable Locomotion curation views from the compressed JSON source of truth."""

from __future__ import annotations

import argparse
import bz2
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "curation" / "locomotion-2026-08-19.json.bz2"
EXPECTED_SCHEMA = "yoru-motion-curation/v1"
EXPECTED_TOTAL = 427
EXPECTED_RAW_SHA256 = "f0b3254bfc67f6dbd947f1b7ec2ef1a14cd6116071808a201b1697965afb2e54"
ALLOWED_STATUS = {"keep", "maybe", "reject"}

VIEWS = {
    "keep": (ROOT / "curation" / "liked.md", "❤️ Liked", "Yoru 明确保留、愿意进入下一轮实测的 Locomotion 候选。"),
    "maybe": (ROOT / "curation" / "maybe.md", "○ Maybe", "有一部分喜欢、需要再看，或值得保留结构但视觉 variant 还需要筛选的 Locomotion 候选。"),
    "reject": (ROOT / "curation" / "rejected.md", "× Rejected", "Yoru 明确不喜欢 / 不适合当前工作流的 Locomotion 候选。Reject 是有价值的负样本，必须保留，避免 Agent 反复推荐同类内容。"),
}


def load_and_validate() -> dict:
    raw = bz2.decompress(SOURCE.read_bytes())
    raw_sha256 = hashlib.sha256(raw).hexdigest()
    if raw_sha256 != EXPECTED_RAW_SHA256:
        raise SystemExit(f"raw snapshot sha256 mismatch: {raw_sha256}")

    data = json.loads(raw)
    if data.get("schema") != EXPECTED_SCHEMA:
        raise SystemExit(f"unexpected schema: {data.get('schema')!r}")

    records = data.get("selected")
    if not isinstance(records, list):
        raise SystemExit("selected must be a list")
    if data.get("totalCandidates") != EXPECTED_TOTAL or len(records) != EXPECTED_TOTAL:
        raise SystemExit(
            f"expected {EXPECTED_TOTAL} candidates, got totalCandidates={data.get('totalCandidates')} selected={len(records)}"
        )

    ids: set[str] = set()
    required = {"id", "file", "base", "style", "status", "score", "note"}
    for index, record in enumerate(records):
        missing = required - set(record)
        if missing:
            raise SystemExit(f"record {index} missing fields: {sorted(missing)}")
        if record["status"] not in ALLOWED_STATUS:
            raise SystemExit(f"record {record['id']} has invalid status {record['status']!r}")
        if record["id"] in ids:
            raise SystemExit(f"duplicate stable id: {record['id']}")
        ids.add(record["id"])

        expected_id = f"locomotion/{record['base']}/{record['style']}"
        if record["id"] != expected_id:
            raise SystemExit(f"stable id mismatch: {record['id']!r} != {expected_id!r}")

    return data


def render(data: dict, status: str, title: str, intro: str) -> str:
    records = [record for record in data["selected"] if record["status"] == status]
    lines = [
        f"# {title}",
        "",
        intro,
        "",
        "> Generated from [`locomotion-2026-08-19.json.bz2`](locomotion-2026-08-19.json.bz2). The compressed JSON snapshot is the source of truth; do not edit this list independently.",
        "> Regenerate/check with `python scripts/sync-locomotion-curation.py` / `python scripts/sync-locomotion-curation.py --check`.",
        "",
        f"Total: **{len(records)}**",
        "",
    ]
    grouped: dict[str, list[str]] = {}
    for record in records:
        grouped.setdefault(record["base"], []).append(record["style"])
    for base, styles in grouped.items():
        lines.append(f"- `{base}`: " + ", ".join(f"`{style}`" for style in styles))
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if committed Markdown views differ from generated output")
    args = parser.parse_args()

    data = load_and_validate()
    mismatches: list[Path] = []
    for status, (path, title, intro) in VIEWS.items():
        generated = render(data, status, title, intro)
        if args.check:
            current = path.read_text(encoding="utf-8") if path.exists() else None
            if current != generated:
                mismatches.append(path)
        else:
            path.write_text(generated, encoding="utf-8")

    if mismatches:
        for path in mismatches:
            print(f"out of sync: {path.relative_to(ROOT)}", file=sys.stderr)
        return 1

    counts = {status: sum(1 for record in data["selected"] if record["status"] == status) for status in ("keep", "maybe", "reject")}
    print(f"ok: total={len(data['selected'])} keep={counts['keep']} maybe={counts['maybe']} reject={counts['reject']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
