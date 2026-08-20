# Benchmark A — anonymized practical-test results

First real-material sweep. The goal was to replace flattering demo content with ordinary production material **without rescuing the design first**, then record what broke.

19 templates × landscape/portrait = 38 stills rendered successfully. The original benchmark used private interview material; names, local paths, source sites, screenshots, and production-specific numbers are intentionally not published here.

---

## Component failures found by the sweep

### 1. TypewriterLine — CJK layout is not robust

The English-first implementation breaks under ordinary Chinese copy:

- kicker and body do not stay on the same axis;
- the body block changes width while typing and visibly drifts;
- forcing a mono family does not guarantee mono metrics once CJK fallback occurs;
- character-based wrapping can split semantic units badly.

**Conclusion:** the CJK version needs its own layout treatment. This is not a one-number tuning fix.

### 2. BarChartReveal — labels are sized from series count, not text width

Longer CJK category labels wrap unexpectedly. The original short labels never exposed the problem.

**Conclusion:** chart geometry must account for label width or provide a deliberate label strategy.

### 3. Data lightness ramp is index-based

`BarChartReveal` and `DonutBreakdown` assign shades by array position. Demo data happened to be ordered in the same direction as value magnitude, so the rule looked semantically meaningful when it may only have been positional.

**Status:** unresolved. Re-check the rendered reference before changing behavior.

### 4. ModalExplainer — overlay recipe depends too much on palette hue

Using `palette.ink` at a fixed alpha works on near-neutral palettes but can turn dirty on warm palettes. One internal element also uses a hard-coded white instead of a theme token.

**Conclusion:** dimming should be designed independently from the ink hue.

---

## Material-level failures

These are useful because they show where a template is technically valid but semantically wrong for ordinary footage.

### 5. Full-page screenshots become unreadable at video scale

A whole product/web page shrunk into a browser frame becomes texture rather than information.

**Need:** crop / pan / local magnification as a separate primitive. Do not pretend a full-page screenshot is legible.

### 6. One palette cannot always absorb heterogeneous source material

Real production material may arrive with incompatible native colour worlds. A single global palette can make one source feel integrated and another feel pasted on.

### 7. Avatar slots require avatar-shaped material

A small circular identity slot cannot safely accept arbitrary landscape screenshots.

### 8. ProductReveal carries e-commerce semantics

Props such as `price` / `comparePrice` are not neutral containers. Reusing them for unrelated documentary or editorial values makes the template read incorrectly even if the layout fits.

---

## Portrait finding

All templates rendered in 9:16, but "renders" is weaker than "has a portrait layout". The first sweep showed a systematic pattern: landscape compositions were rearranged into portrait canvases while still occupying only the upper portion of the frame.

**Conclusion:** portrait needs explicit composition rules, not only responsive dimensions.

---

## What survived

A substantial set of information-first templates accepted longer Chinese copy and ordinary material without structural failure. That supports the main curation finding: Yoru tends to keep motion that carries information rather than motion whose action is the content.

---

## Public benchmark rule

Future examples committed to this repository must use synthetic or redistributable fixtures. Private client/interview material may be used locally for stress testing, but identifying names, paths, screenshots, URLs, metrics, and unpublished copy stay outside Git.
