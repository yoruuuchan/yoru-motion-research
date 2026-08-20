# Locomotion Preference Profile — 2026-08-19

> Agent-readable analysis of Yoru's complete manual review of the Locomotion candidate set.
> Source of truth: [`../curation/locomotion-2026-08-19.json.bz2`](../curation/locomotion-2026-08-19.json.bz2). Metadata/checksum: [`../curation/locomotion-2026-08-19.meta.json`](../curation/locomotion-2026-08-19.meta.json).
> This document summarizes the dataset; it never overrides an individual JSON decision.

## Dataset facts

- Schema: `yoru-motion-curation/v1`
- Upstream source: `locomotion-pro/locomotion`
- Exported at: `2026-08-19T10:19:06.373Z`
- Candidates: **427** = **61 template families × 7 styles**
- Stable IDs: **427 unique**
- Fields retained: `id`, `file`, `base`, `style`, `status`, `score`, `note`
- Uncompressed uploaded JSON SHA-256: `f0b3254bfc67f6dbd947f1b7ec2ef1a14cd6116071808a201b1697965afb2e54`
- All 427 `score` values are `0` and all 427 `note` values are empty. The analysis therefore uses explicit `status` labels only; it does not invent reasons that were not recorded.

## Overall decisions

| Status | Count | Share |
|---|---:|---:|
| `keep` | 41 | 9.6% |
| `maybe` | 123 | 28.8% |
| `reject` | 263 | 61.6% |

The dataset is intentionally negative-heavy. Rejects are useful preference evidence and must remain available to future agents.

## Style preference distribution

Each style appears 61 times.

| Style | Keep | Maybe | Reject | Keep rate | Non-reject rate |
|---|---:|---:|---:|---:|---:|
| `default` | 10 | 26 | 25 | 16.4% | 59.0% |
| `dark` | 9 | 19 | 33 | 14.8% | 45.9% |
| `brutalist` | 8 | 15 | 38 | 13.1% | 37.7% |
| `glass` | 7 | 14 | 40 | 11.5% | 34.4% |
| `minimal` | 3 | 13 | 45 | 4.9% | 26.2% |
| `neo` | 2 | 16 | 43 | 3.3% | 29.5% |
| `rounded` | 2 | 20 | 39 | 3.3% | 36.1% |

**Data-supported reading:** `default` is the safest starting style in this batch, followed by `dark`. `minimal`, `neo`, and `rounded` are weak automatic recommendations. `brutalist` and `glass` can work very well on the right structure but are strongly family-dependent.

## Every template family's overall performance

The groups below cover all 61 families. Tuple format is `(keep / maybe / reject)`.

| Result | Template families |
|---|---|
| **5 / 2 / 0** | `appointment-booking` |
| **4 / 3 / 0** | `changelog` |
| **4 / 2 / 1** | `bar-chart-reveal` |
| **3 / 2 / 2** | `before-after`, `patient-journey` |
| **2 / 4 / 1** | `concept-breakdown` |
| **3 / 1 / 3** | `countdown-timer` |
| **2 / 3 / 2** | `day-summary` |
| **1 / 5 / 1** | `portfolio-breakdown` |
| **0 / 7 / 0** | `agenda-reveal`, `cart-animation`, `pricing-comparison` |
| **2 / 2 / 3** | `staggered-words` |
| **0 / 6 / 1** | `onboarding-flow` |
| **2 / 1 / 4** | `screen-showcase` |
| **0 / 5 / 2** | `drag-drop-demo`, `metric-card`, `stats-dashboard` |
| **2 / 0 / 5** | `typewriter-reveal` |
| **1 / 2 / 4** | `app-feature-callout`, `product-reveal`, `social-post` |
| **0 / 4 / 3** | `property-tour`, `saas-hero`, `stock-ticker`, `team-intro`, `ui-walkthrough` |
| **1 / 1 / 5** | `step-explainer` |
| **0 / 3 / 4** | `quiz-result`, `quote-card`, `sales-card`, `virtual-walkthrough` |
| **1 / 0 / 6** | `bento-grid`, `feature-showcase`, `modal-explainer`, `payment-flow` |
| **0 / 2 / 5** | `flashcard-flip`, `intro-outro`, `job-posting` |
| **0 / 1 / 6** | `collab-card`, `discount-countdown`, `launch-day`, `listing-card`, `profile-card`, `speaker-card`, `spring-scale-in`, `testimonial-card`, `wellness-stats` |
| **0 / 0 / 7** | `achievement-unlock`, `bold-text-punch`, `culture-reel`, `fade-slide-up`, `gradient-text`, `leaderboard`, `lesson-intro`, `level-up`, `logo-reveal`, `meme-card`, `milestone-counter`, `product-hunt`, `toggle-switch` |

## Strong positive and unresolved families

No family has seven `keep` variants. The closest things to “overall liked” are:

- `appointment-booking` — **5 keep / 2 maybe / 0 reject**
- `changelog` — **4 keep / 3 maybe / 0 reject**
- `bar-chart-reveal` — **4 keep / 2 maybe / 1 reject**
- `before-after` and `patient-journey` — **3 keep / 2 maybe / 2 reject** each
- `concept-breakdown` — **2 keep / 4 maybe / 1 reject**

Three families are uniformly unresolved rather than disliked: `agenda-reveal`, `cart-animation`, and `pricing-comparison` are **0 keep / 7 maybe / 0 reject**. An agent should return them to human review rather than force a binary label.

## Seven-variant total rejects

The following **13** families have all seven variants rejected:

`achievement-unlock`, `bold-text-punch`, `culture-reel`, `fade-slide-up`, `gradient-text`, `leaderboard`, `lesson-intro`, `level-up`, `logo-reveal`, `meme-card`, `milestone-counter`, `product-hunt`, `toggle-switch`

This is strong evidence that changing only the Locomotion visual style is unlikely to rescue these structures for the current preference profile.

## Default-reject counterexamples

Only **three** families have `default = reject` but a non-default variant reaches `keep`:

- `bento-grid` — default reject; `brutalist` keep
- `feature-showcase` — default reject; `brutalist` keep
- `step-explainer` — default reject; `glass` keep; `minimal` maybe

Therefore a default rejection is useful evidence, but must not become a family-wide hard reject when style-specific evidence exists.

## Structure worth keeping, visual variant worth filtering

The cleanest “structure survives, variant matters” cases have at least two keeps and at least one reject:

- `bar-chart-reveal` — 4 / 2 / 1
- `before-after` — 3 / 2 / 2
- `patient-journey` — 3 / 2 / 2
- `concept-breakdown` — 2 / 4 / 1
- `countdown-timer` — 3 / 1 / 3
- `day-summary` — 2 / 3 / 2
- `staggered-words` — 2 / 2 / 3
- `screen-showcase` — 2 / 1 / 4
- `typewriter-reveal` — 2 / 0 / 5

These should be modeled at `template + style` granularity instead of collapsing the whole family into one verdict.

## Data-supported rules for future agents

1. Keep the three-way label. `maybe` is **28.8%** of the dataset and is meaningful uncertainty, not missing work.
2. Use exact stable-ID history first. A recommendation should resolve to `locomotion/<template>/<style>` and preserve the matching MP4 filename and judgment.
3. Weight template-family evidence heavily. Thirteen families fail in all seven styles; only three default-reject families contain a kept alternate style.
4. Use style only as a prior. `default` and `dark` are relatively safer; `minimal`, `neo`, and `rounded` require stronger family-specific evidence.
5. Preserve negative samples. Close structural analogues of the all-seven-reject families should be strongly down-ranked, not forgotten.
6. Keep interaction effects. A useful family can contain rejected styles, so family and style must be evaluated together.
7. Novel or ambiguous cases go back to Yoru. Historical data is for pre-screening, never for silently replacing her final decision.

## Inferences — lower confidence than the facts above

These are hypotheses suggested by template names and label patterns, not recorded reasons:

- Several strongest families involve information reveal, comparison, progress, UI/state change, or structured explanation. This **may** indicate that motion with a clear communicative job survives screening more often than motion whose primary value is decorative impact.
- Generic hype/reveal/badge-like structures occur repeatedly in the all-reject set. The underlying composition or content role may matter more than merely increasing or decreasing animation intensity.
- `brutalist` and `glass` occasionally rescue rejected defaults, so visual boldness itself is not a reliable negative signal; context is decisive.

Future review tools should collect optional reason tags/notes if we want to distinguish layout, typography, rhythm, palette, motion primitive, and content-fit causes without inference.
