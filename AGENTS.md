# Agent Instructions

This repository is a **motion-design research and curation workspace**, not yet the production motion-system repository.

## Phase boundary

Current phase: `research_inventory_and_taste_curation`.

Do not treat upstream repositories as approved dependencies or approved visual styles merely because they are listed here. Yoru's curation is the gate for practical testing.

## Source priority when producing

When Yoru asks for something she has made before, `gold/` outranks everything:
same-family gold exemplar > `shots/keep` (check the curation verdict first — a
reject is a veto, and 文字与字卡 ranks last by default) > `themes/` prohibitions >
any general rule. Never design from scratch while a same-family gold exemplar
exists, and never pull cards from upstream video-shotcraft directly — the 209
verdicts here already cover it (2026-08-26: an agent pulled `paper-title-card`
from upstream; it is a reject here).

## Source of truth

- Approved own deliverables (positive exemplars): `gold/`
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

## Production rules — when a full video is being made from this library

Learned from the first whole-video tests (2026-08-20), where every one of these was violated:

1. **Never re-implement a shot by visual approximation.** If the exact implementation in
   `shots/` cannot run in the current environment, switch environments or deliver
   composition code only. A lookalike rewritten from memory (e.g. in OpenCV) is not the
   curated shot and must not be presented as one.
2. **Design the energy curve before picking shots.** Write down the intended
   build → peak → rest structure for the whole piece first, and mark it as an assumption —
   no gold-standard films exist yet to measure one from. Uniform segment length and
   uniform density read as flat; that is the documented failure mode.
3. **No fake filler content.** Invented tech-flavour strings (`NODE-01`, `SYSTEM READY`,
   made-up metrics) are the content-level equivalent of invented timing numbers, and the
   same rule applies: use real material, or state explicitly that a value is a placeholder.
4. **Pick fewer shots than you want to.** Scored keeps outrank unscored ones — start from
   the eight 5-scores, fill with 4s. A 30-second piece that shows off many library entries
   is optimizing for the library, not the film.
