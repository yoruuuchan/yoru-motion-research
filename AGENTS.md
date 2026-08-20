# Agent Instructions

This repository is a **motion-design research and curation workspace**, not yet the production motion-system repository.

## Phase boundary

Current phase: `research_inventory_and_taste_curation`.

Do not treat upstream repositories as approved dependencies or approved visual styles merely because they are listed here. Yoru's curation is the gate for practical testing.

## Source of truth

- Repository inventory: `data/repos.yml`
- Screening console + candidate datasets: `review/` (see `review/README.md`)
- Human screening list: `CATALOG.md`
- Locomotion decision snapshot: `curation/locomotion-2026-08-19.json.bz2`
- Snapshot metadata/checksum: `curation/locomotion-2026-08-19.meta.json`
- Generated human views: `curation/liked.md`, `curation/maybe.md`, `curation/rejected.md`
- Video Shotcraft decision snapshot: `curation/video-shotcraft-2026-08-20.json.bz2`
- Agent-readable preference profiles: `evaluation/locomotion-preference-profile.md`, `evaluation/video-shotcraft-preference-profile.md`
- Test plan: `evaluation/benchmark-plan.md`
- Acceptance criteria: `evaluation/validation-matrix.md`
- License state: `legal/license-tracker.yml`

For every batch, the compressed JSON snapshot is the decision source of truth. The Markdown curation files are generated views. Never rewrite Yoru's historical `keep` / `maybe` / `reject` labels from inference, and never discard rejects.

Stable IDs use `locomotion/<template>/<style>` and must remain sufficient to resolve template, style, MP4 filename and user judgment.

Video Shotcraft stable IDs use `video-shotcraft/<card>/<style>`, one per previewable
style (209 across 152 shot cards). Its exports carry upstream repo, commit, category,
source recipe path and preview URL, so a verdict stays resolvable without a local
checkout. Ingest exports with `scripts/import-curation-export.py`; it writes a new
dated snapshot and refuses to overwrite an existing one.

## Future pre-screening

Use exact historical IDs first, then the patterns in the two preference profiles. Locomotion generalizes by template family and re-skin style; Video Shotcraft generalizes by category only, because its `style` names a different shot rather than a re-skin. Pre-screening may rank or down-rank new material, but ambiguous or novel cases go back to Yoru for the final decision.

## Future implementation rule

When a candidate is promoted for testing, keep the upstream reference explicit, test one layer at a time, render in the real target format, and report unresolved problems rather than weakening acceptance criteria.
