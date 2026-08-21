# Claude Guide

## What this repo is for

**This repo is the deliverable, not the notes.** It is a curated motion-reference library meant to stay findable and readable straight from GitHub, not a localhost-only tool or a parallel runnable framework.

Judge any proposal by "does this make something easier to find later?" If the honest answer is only "it makes something easier to run", that work probably belongs elsewhere.

## Current phase

`library_assembled` → both sources are curated and published as browsable libraries.

Read first:

1. `shots/README.md` — 137 kept Video Shotcraft shots, code included (Apache-2.0)
2. `layouts/README.md` — 41 kept Locomotion templates, navigation only (`reference_only`)
3. `themes/README.md` — the eight local design-system sources, and which library entries survive each
4. `evaluation/video-shotcraft-preference-profile.md`
5. `evaluation/locomotion-preference-profile.md`
6. `legal/license-tracker.yml` — decides copy-vs-link for anything new
7. `curation/*.json.bz2` + `*.meta.json` — source of truth for every verdict
8. `evaluation/benchmark-a-results.md` — anonymized findings from real-material stress testing
9. `CATALOG.md`, `review/README.md`

### The licence line runs through everything

It decides the shape, not just the paperwork:

- **Video Shotcraft** — Apache-2.0. Implementations are copied into `shots/`, split `keep/` vs `maybe/`, rejects not copied at all. Obligations are recorded in `shots/NOTICE.md`.
- **Locomotion** — no LICENSE upstream, `reference_only`. `layouts/` links and never copies. Do not derive implementation code from unlicensed source; timing and layout observations in this project come from rendered references.

Both libraries are regenerated, never hand-edited: `scripts/build-shot-library.py` and `scripts/build-layout-index.py`.

### Open

- **Nine shot directories carry a README but no code** — not a build bug. Upstream published a spec and preview but no implementation. Fix the generator if their pages need clarification; do not invent missing source.
- **KUNLUN has no matching skin.** Its signature is a chamfered corner, while the four current skins only offer rounded or square geometry.
- **YORU Content has no motion spec at all.** Using it for video means borrowing rhythm from elsewhere; that rule is still undecided.
- **`yoruDark` in `yoru-motion-system` needs correction**: the current dark palette contains values that are not traceable to the source design tokens and has contrast/collision issues. See `themes/yoru-content.md`.
- The undecided and all-rejected Locomotion templates intentionally have no descriptions.

Screening happens in `review/` — one dataset-driven console for every source. Locomotion and Video Shotcraft are both loaded there; neither source's preview media is copied into this repository.

For both sources the compressed JSON snapshot is the source of truth. The `liked` / `maybe` / `rejected` Markdown files are generated readable views; do not edit them as independent decision stores.

## When practical testing starts

Only test candidates kept in the JSON / generated `liked.md`, or candidates explicitly promoted from `maybe`.

For each candidate:

- preserve the stable ID, upstream source link and license status;
- use the same publishable benchmark fixture before making aesthetic rescue edits;
- render a real MP4, not only a Studio preview;
- report which parts are worth keeping: motion principle, layout, component API, or implementation;
- record failures explicitly;
- propose adaptation into the YORU taxonomy: `Style × Rhythm × Purpose × Palette × Format`.

Historical rejects are negative evidence, not disposable clutter. A future agent may pre-screen with the preference profile, but Yoru owns the final keep / maybe / reject decision.

Before assembling a **full video** from these shots, read the production rules at the end
of `AGENTS.md` — they exist because the first whole-video tests violated all of them.

The target is not to fork every upstream project. The target is a small, coherent motion vocabulary that survives real-material testing and can later feed the YORU Motion System.
