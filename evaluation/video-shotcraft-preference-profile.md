# Video Shotcraft Preference Profile — 2026-08-20

> Agent-readable analysis of Yoru's complete manual review of the Video Shotcraft candidate set.
> Source of truth: [`../curation/video-shotcraft-2026-08-20.json.bz2`](../curation/video-shotcraft-2026-08-20.json.bz2). Metadata/checksum: [`../curation/video-shotcraft-2026-08-20.meta.json`](../curation/video-shotcraft-2026-08-20.meta.json).
> This document summarizes the dataset; it never overrides an individual JSON decision.
> Companion profile for the other reviewed source: [`locomotion-preference-profile.md`](locomotion-preference-profile.md).

## Dataset facts

- Schema: `yoru-motion-curation/v2`
- Upstream source: `Vincentwei1021/video-shotcraft` at commit `0d6f0b57f0d4d6700761644c07f7ef03c3e50234` (2026-08-14)
- The commit was verified, not assumed: the reviewed `gallery/api/library.json` matches upstream blob sha1 `fcbc96b2b8a08959ace510460988cc012291caa3` byte-for-byte.
- Exported at: `2026-08-20T06:43:04.893Z`
- Candidates: **209 previewable styles across 152 shot cards**
- Stable IDs: **209 unique**, shaped `video-shotcraft/<card>/<style>`
- Fields retained per row: `id`, `source`, `upstreamRepo`, `upstreamCommit`, `card`, `style`, `styleLabel`, `category`, `categoryLabel`, `recipePath`, `previewUrl`, `file`, `verdict`, `score`, `note`
- Uncompressed uploaded JSON SHA-256: `3502f50c8b77a5d41073709bdedbb87495538b1656ffffbc3e353c5b0bee48cb`
- Every candidate was rated. `unrated` is **0**.
- **40** rows carry a non-zero `score`; **1** row carries a note.

## The axis here is not the Locomotion axis

This matters before reading any table below. In Locomotion, `style` is a *re-skin*: the same
template rendered as `default` / `dark` / `brutalist` / `glass` / `minimal` / `neo` / `rounded`,
a uniform 61 × 7 grid. A cross-style comparison there answers "which palette".

In Video Shotcraft, `style` is a *different shot*. A card is a motion idea, and its styles are
distinct executions of that idea — `shot-transitions` contains `flash-cut`, `whip-pan`,
`mask-wipe` and three numbered variants; those are not the same shot in different colors.
Card breadth is uneven:

| styles per card | cards |
|---:|---:|
| 1 | 113 |
| 2 | 26 |
| 3 | 10 |
| 4 | 2 |
| 6 | 1 |

So there is **no style-prior section** in this profile, because "style" carries no shared meaning
across cards. The axis that does generalize is `category`.

## Overall decisions

| Verdict | Count | Share |
|---|---:|---:|
| `keep` | 137 | 65.6% |
| `maybe` | 57 | 27.3% |
| `reject` | 15 | 7.2% |

This is the mirror image of the Locomotion distribution (9.6% / 28.8% / 61.6%). See
[Cross-source reading](#cross-source-reading) — the two rates are not in conflict, and the
difference is not evidence that the standard moved.

## Category preference distribution

| Category | Total | Keep | Maybe | Reject | Keep rate |
|---|---:|---:|---:|---:|---:|
| 交互与功能演示 (interaction & feature demo) | 19 | 18 | 1 | 0 | **94.7%** |
| 运镜与空间 (camera & space) | 16 | 15 | 1 | 0 | **93.8%** |
| 界面登场与陈列 (UI entrance & display) | 31 | 25 | 6 | 0 | 80.6% |
| 开场与品牌 (opening & brand) | 10 | 8 | 1 | 1 | 80.0% |
| 数据与指标 (data & metrics) | 16 | 12 | 2 | 2 | 75.0% |
| 光效与强调 (light & emphasis) | 29 | 18 | 9 | 2 | 62.1% |
| 转场 (transitions) | 29 | 15 | 10 | 4 | 51.7% |
| 节奏与蒙太奇 (rhythm & montage) | 20 | 10 | 9 | 1 | 50.0% |
| 收尾 (closing) | 8 | 4 | 4 | 0 | 50.0% |
| 文字与字卡 (type & title cards) | 31 | 12 | 14 | 5 | **38.7%** |

**Data-supported reading:** two categories are near-unanimous positives — anything that
demonstrates an interaction or moves a camera through space. The weakest category by keep rate is
`文字与字卡`, which also supplies **5 of the 15 rejects** — a third of all rejections from 15% of
the dataset.

Four categories carry no rejects at all, but they do not mean the same thing. `交互与功能演示`,
`运镜与空间` and `界面登场与陈列` are zero-reject *and* high-keep. `收尾` is zero-reject at only
50% keep — 4 keep, 4 maybe, no scores at all across 8 candidates. Read that as nothing offensive
and nothing compelling, not as endorsement.

## Score is a partial ranking inside `keep`

| Verdict | Rows | Scored | Score distribution |
|---|---:|---:|---|
| `keep` | 137 | 39 (28%) | 5×8, 4×26, 3×4, 2×1 |
| `maybe` | 57 | 1 (2%) | 3×1 |
| `reject` | 15 | 0 (0%) | — |

Scores appear almost exclusively on `keep`, and on only a quarter of those. Yoru stated directly
what this means (2026-08-20, in session — attested, not inferred):

> keep 但 0 分：意思是我懒得打分，但是内容是我认可的。打分的是我觉得比这些没打分的更好的。
>
> *A keep with score 0 means I could not be bothered to score it, but I do approve of the content.
> The ones I scored are the ones I think are better than the unscored ones.*

So `keep` is not a flat set. It is two tiers:

1. **Scored keeps (39)** — approved *and* judged better than the baseline. The number orders them.
2. **Unscored keeps (98)** — approved, unranked. Full endorsements, but she did not place them above the rest.

Both readings a future agent might reach for are wrong. Score 0 is **not** a rejection or a weak
keep in the sense of "barely acceptable" — all 137 are approved material. But it is also **not**
merely absent annotation: a scored keep genuinely outranks an unscored one. Preserve that ordering
when shortlisting; do not collapse the 137 into one bucket, and do not promote an unscored keep
over a scored one without new evidence.

Scoring behavior per category is therefore a ranking signal, not just an attention signal —
it says where the above-baseline work concentrates:

| Category | Scored | Mean score (scored only) |
|---|---:|---:|
| 运镜与空间 | 9/16 (56%) | 4.3 |
| 交互与功能演示 | 7/19 (37%) | 3.7 |
| 转场 | 7/29 (24%) | 3.7 |
| 光效与强调 | 6/29 (21%) | 4.2 |
| 开场与品牌 | 2/10 (20%) | 4.5 |
| 数据与指标 | 3/16 (19%) | 4.0 |
| 界面登场与陈列 | 5/31 (16%) | 4.0 |
| 节奏与蒙太奇 | 1/20 (5%) | 4.0 |
| 文字与字卡 | 0/31 (0%) | — |
| 收尾 | 0/8 (0%) | — |

`运镜与空间` leads on both axes: **more than half** of all camera shots were ranked above the
baseline keep, at the highest mean in the set. At the other end, `文字与字卡` and `收尾` have
**zero** scored rows across 39 combined candidates — of the 16 keeps in those two categories, not
one was placed above baseline.

### The eight 5-scores

`dashboard-glow-highlight-pill`, `dataviz-landscape-open`, `deck-deal-flyin`, `graze-face-tour`,
`runway-ground-skim`, `shot-transitions/shot-transitions-5`, `steep-tilt-glide`, `terminal-3d`.

Three of the eight (`graze-face-tour`, `steep-tilt-glide`, `terminal-3d`) are camera work, and
two more (`dataviz-landscape-open`, `runway-ground-skim`) move through space to open a scene.

## Card-level evidence

### Cards kept in every variant (≥2 styles, all `keep`) — 17

`canvas-materialize-moves`, `chart-live-moves` (3), `collab-cursor-moves`, `depth-layer-moves`,
`element-body-moves`, `gauge-readout-moves`, `icon-performance-moves`, `impact-feedback`,
`input-trigger-moves`, `overhead-camera-moves`, `paper-craft-moves`, `scroll-brake-moves`,
`space-camera-moves`, `spotlight-sweep-moves` (3), `theme-switch-moves`, `typewriter-moves`,
`wall-reveal-moves` (3)

The motion idea survived regardless of which execution she saw. These are the safest structures
to build on.

### Cards rejected in every variant — 8

| Card | Styles | Category |
|---|---:|---|
| `gradient-transition` | 1 | 转场 |
| `paper-title-card` | 1 | 文字与字卡 |
| `particle-celebrate-hits` | 2 | 数据与指标 |
| `pill-chip-slot-cycle-handled` | 1 | 文字与字卡 |
| `riso-print-hits` | 2 | 光效与强调 |
| `text-as-mask` | 1 | 开场与品牌 |
| `text-column-converge` | 1 | 文字与字卡 |
| `word-relay-geometry` | 1 | 文字与字卡 |

Two of these were rejected across *both* their variants (`particle-celebrate-hits`,
`riso-print-hits`), which is stronger evidence than a single-variant reject.

### Cards where the idea survives but the execution decides — 2

Only two cards contain both a `keep` and a `reject`. Both must be modeled at
`card + style` granularity, never collapsed to a card-level verdict:

**`shot-transitions`** (转场) — 3 keep / 1 maybe / 2 reject

| Style | Verdict | Score |
|---|---|---:|
| `shot-transitions-5` | keep | 5 |
| `flash-cut` | keep | 0 |
| `shot-transitions-4` | keep | 0 |
| `mask-wipe` | maybe | 0 |
| `shot-transitions-6` | reject | 0 |
| `whip-pan` | reject | 0 |

**`type-assembly-moves`** (文字与字卡) — 2 keep / 1 maybe / 1 reject

| Style | Verdict |
|---|---|
| `drift-assembly` | keep |
| `text-on-path` | keep |
| `split-text-stagger` | maybe |
| `tracking-expand` | reject |

### Unresolved multi-variant cards

`slam-entrance-moves` (光效与强调) is **0 keep / 3 maybe / 0 reject** — uniformly unresolved
rather than disliked. `transition-travel`, `type-entrance-moves` and `type-rhythm-sync` are each
0/2/0. Return these to human review rather than forcing a binary label.

## The 15 rejects in full

| Card / style | Category |
|---|---|
| `gradient-transition / gradient-transition` | 转场 |
| `paper-title-card / paper-title-card` | 文字与字卡 |
| `particle-celebrate-hits / confetti-crossfire` | 数据与指标 |
| `particle-celebrate-hits / counter-tick-sparks` | 数据与指标 |
| `pill-chip-slot-cycle-handled / pill-chip-slot-cycle-handled` | 文字与字卡 |
| `rhythm-interrupt-moves / strobe-black-frames` | 节奏与蒙太奇 |
| `riso-print-hits / misregistration-hit` | 光效与强调 |
| `riso-print-hits / beat-pump` | 光效与强调 |
| `shot-transitions / shot-transitions-6` | 转场 |
| `shot-transitions / whip-pan` | 转场 |
| `text-as-mask / text-as-mask` | 开场与品牌 |
| `text-column-converge / text-column-converge` | 文字与字卡 |
| `type-assembly-moves / tracking-expand` | 文字与字卡 |
| `wipe-transitions / blinds-slice` | 转场 |
| `word-relay-geometry / word-relay-geometry` | 文字与字卡 |

Rejects are preference evidence and must remain available to future agents.

## The one recorded note

`shot-transitions / shot-transitions-4` — `keep`, score 0 — **"色彩风格想改成冷色系"**
(*wants the color palette changed to a cool range*).

This is the only recorded reason in the entire dataset, and it is a *palette* note attached to a
*kept* shot. It says the motion was accepted and the color was not. Treat palette as separable
from motion when adapting this shot.

## Cross-source reading

### The two keep rates are not in conflict

Locomotion kept 9.6% of 427; Shotcraft kept 65.6% of 209. The candidate populations differ in
kind: Locomotion's 427 are 61 templates mechanically multiplied by 7 re-skins, so most rows are
near-duplicates of a row she already judged, and a rejected template drags six siblings down with
it. Shotcraft's 209 are hand-authored shots with far less internal redundancy. Do **not** conclude
that the screening standard loosened, and do not normalize the two rates against each other.

### Confirmed across both sources: typography-led motion is the weak spot

The Locomotion profile listed this as a low-confidence inference ("motion with a clear
communicative job survives screening more often than motion whose primary value is decorative
impact"). Two independent libraries now agree on the type-specific half of it:

- Locomotion: `gradient-text` and `bold-text-punch` were rejected in all 7 variants;
  `typewriter-reveal` 2/0/5; `staggered-words` 2/2/3.
- Shotcraft: `文字与字卡` is the lowest keep rate (38.7%), supplies a third of all rejects, and is
  one of only two categories that received zero emphasis scores.

This can be promoted from inference to a data-supported pattern. It is a statement about
*typography-led* shots specifically — the broader "decorative vs communicative" framing is still
an inference (see below).

### New axis Locomotion could not measure

Locomotion contains no camera movement at all; it is 2D UI templates end to end. `运镜与空间`
therefore had no prior evidence, and it lands at 93.8% keep with the highest scoring rate and
highest mean score in the set. This is a genuinely new region of the preference profile, not a
confirmation.

## Data-supported rules for future agents

1. Keep the three-way label. `maybe` is 27.3% here and is meaningful uncertainty, not unfinished work.
2. Resolve recommendations to the exact stable ID `video-shotcraft/<card>/<style>`, preserving the upstream repo, commit, recipe path and preview URL carried in the row.
3. Weight `category` heavily; it is the only axis that generalizes across cards. `style` does not — it names a different shot, not a re-skin.
4. Rank `交互与功能演示` and `运镜与空间` first when proposing candidates. Rank `文字与字卡` last, and require card-specific positive evidence before proposing anything from it.
5. Treat `keep` as two tiers, not one set: 39 scored keeps outrank 98 unscored keeps, and all 137 are approved. Score 0 is not a rejection and not a weak keep; it is approval without a ranking mark.
6. Prefer the 17 all-variant-keep cards as build targets — the idea survived independent of execution.
7. Model `shot-transitions` and `type-assembly-moves` at `card + style` granularity. They are the only cards containing both a keep and a reject.
8. Return the 0-keep/all-maybe cards (`slam-entrance-moves`, `transition-travel`, `type-entrance-moves`, `type-rhythm-sync`) to Yoru instead of guessing.
9. Preserve negative samples. The 8 all-reject cards, especially the two rejected across both variants, are down-ranking evidence for close structural analogues.
10. Historical data pre-screens; Yoru owns the final keep / maybe / reject decision.

## Inferences — lower confidence than the facts above

These are hypotheses suggested by names and label patterns, not recorded reasons. Only one note
exists in the whole dataset, so causes are not directly attested.

- Within the weak `文字与字卡` category, the 12 survivors skew toward text being *written into a
  real surface* — `document-typewriter-reveal`, `typewriter-moves/terminal-typewriter`,
  `typewriter-moves/error-retype`, `typing-code-block` — while the 5 rejects skew toward letters
  performing as a standalone title card: `paper-title-card`, `text-column-converge`,
  `word-relay-geometry`, `tracking-expand`, `pill-chip-slot-cycle-handled`. This **may** mean the
  objection is to typography-as-decoration rather than to animated text as such. Locomotion's
  `typewriter-reveal` at 2/0/5 is a partial counterweight, so treat this as a hypothesis to test,
  not a rule.
- Both all-variant reject cards outside the type category (`particle-celebrate-hits`,
  `riso-print-hits`) center on particulate or print-artifact texture layered over a shot. Combined
  with `strobe-black-frames` and `blinds-slice`, this **may** indicate low tolerance for effects
  that add visual noise without carrying content. Not directly attested.
- The strongest categories all involve a subject that is doing something legible — an interface
  responding, a camera revealing space, data changing. This is consistent with the Locomotion
  "communicative job" hypothesis but is still an inference here, since the category taxonomy is
  the upstream author's, not Yoru's.

The console records optional score and note fields; only 40 scores and 1 note were used. If we
want to separate layout, typography, rhythm, palette, motion primitive and content-fit causes
without inference, the next review pass needs reason tags, not more verdicts.
