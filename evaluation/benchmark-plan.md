# Benchmark Plan — practical tests with publishable fixtures

## Why use the same material

A polished demo may owe most of its quality to the source material. Candidates should be compared with the same ordinary copy, image shapes, colours and durations so the motion language itself is being tested.

**Repository rule:** committed benchmark fixtures must be synthetic, self-authored, or explicitly redistributable. Private production material can be used locally for stress testing, but identifying names, local paths, screenshots, URLs, business metrics and unpublished copy do not enter Git.

## Benchmark A — editorial / maker interview

- Canvas: 1920×1080
- FPS: 30
- Target duration: intro 4–6s / transition 0.3–1.0s / outro 2–4s
- Subject: fictional maker / creator
- Material: four synthetic project images with mixed aspect ratios
- Copy: ordinary sentence-length Chinese plus short English labels
- Palette: warm-paper or another declared palette
- Audio: one minimal SFX set / no BGM

Purpose: validate Editorial / Experimental / Fresh / Medium rhythm, CJK typography, screenshot legibility and material fit.

## Benchmark B — AI / software product

- Canvas: 1920×1080
- FPS: 30
- Material: synthetic product screenshots + short screen recording
- Copy: fixed title / feature / metric
- Palette: electric-blue or a unified neutral palette

Purpose: validate Tech / Kinetic / UI / Product motion.

## Benchmark C — portrait creator content

- Canvas: 1080×1920
- FPS: 30
- Material: synthetic portrait + three short clips
- Target: intro ≤3s

Purpose: determine whether a component has a genuine portrait composition rather than merely rendering inside a portrait canvas.

## First sweep: replace content, do not rescue the design

If a component becomes ugly or unreadable after the fixture swap, record the failure before redesigning it. The first pass should separate:

1. structural weakness in the component;
2. demo-content dependence;
3. language / aspect-ratio assumptions;
4. material-semantic mismatch.

Only candidates that survive or teach something useful move to a second-pass redesign.
