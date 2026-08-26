# YORU Motion Research

Yoru 筛选过的 Remotion 动效参考库。做片子的时候来这里找参考。

---

## 如果你是 AI（GPT / Claude / 其他），先读这一段

**第 0 步 · 分流。你现在要做什么？**

| 任务 | 去哪 | 规矩 |
|---|---|---|
| 做 Yoru 以前做过的东西（问题卡 / 章节卡 / 字卡…） | [`gold/`](gold/) | 有同族成片就直接当母版，只换内容。**禁止重新设计。** |
| 做一条完整短片 | [`AGENTS.md`](AGENTS.md) 末尾 production rules | 先写能量曲线，镜头宁少勿多 |
| 给片子找单个镜头动效 | [`shots/`](shots/) | 提案前必查判决：reject 一票否决，「文字与字卡」默认排最后 |
| 定风格 / 配色 / 质感 | [`themes/`](themes/) | 按下面的两步走 |

**优先级（冲突时从上往下压）**：
`gold/` 同族成片 > `shots/keep`（先查 curation 判决）> `themes/` 禁令 > 一切通用规则。
走到任何一层，都不包括"自由发挥一版试试"。

**两个禁区**

- `yoru-motion-system` 已搁置。除非明确要复用它的某个模板，否则不读、不引用它的 timing 数字。
- 不许绕过本库直接抽上游 video-shotcraft 的卡。那 209 条 Yoru 已经判过票；
  2026-08-26 的翻车就是这么来的——agent 从上游抽了 `paper-title-card`，而它在这里是 reject。

**阅读顺序（要系统了解这个库时）**

0. [`gold/README.md`](gold/README.md) — Yoru 认可过的自己的成片，优先级最高的一层
1. [`themes/README.md`](themes/README.md) — 八套设计系统，以及每套能用库里哪些东西
2. `themes/<系统名>.md` — 具体某套的配色、质感、动效规则、禁忌
3. [`shots/README.md`](shots/README.md) — 137 条镜头，代码就在旁边
4. [`layouts/README.md`](layouts/README.md) — 41 个版式，只有链接没有代码

**三条硬规矩**

- `shots/` 是 Apache-2.0，代码可以直接抄改，保留 [`shots/NOTICE.md`](shots/NOTICE.md) 的署名。
- `layouts/` 指向的 Locomotion 仓库**没有 LICENSE**。只能看预览和链接，
  **不要把它的源码抄进任何地方，也不要去读它的源码**。这个库里所有动效数字
  都是从渲染结果一帧帧量出来的、刻意绕开源码，就是为了来源干净；
  读了它会追溯性地毁掉这份干净。
- 镜头 README 里的时长和参数都是逐帧量出来的。**不要自己编动效数字**——
  找不到就说找不到，或者在注释里写明这是假设。

**打分怎么读**

`keep` 里有的写了分（3–5），有的没写。**没写分不等于差**，等于 Yoru 认可但懒得排名；
写了分的优先级更高。`maybe` 是待定，`reject` 是负样本，留着做预筛依据，不是垃圾。

**被问「XX 风格该用什么镜头」时**，按 [`themes/README.md`](themes/README.md) 的两步走：
先按皮肤查版式（[`data/layout-keeps.tsv`](data/layout-keeps.tsv)），
再按结构性禁令过滤镜头（[`data/shot-traits.tsv`](data/shot-traits.tsv)）。

---

## 来龙去脉

- 上游是两个素材库：[Video Shotcraft](https://github.com/Vincentwei1021/video-shotcraft)
  （Apache-2.0，209 个可预览镜头样式）和 Locomotion（无 LICENSE，427 个渲染变体，
  因此只链接不复制）。
- Yoru 对全部 636 个候选逐条人工评审（keep / maybe / reject，负样本保留），
  脚本再从评审快照生成这个可浏览的库。每一条 keep 都是一次真实的人工判断，
  不是自动聚合的 awesome list。
- 你看到的是 **2026-08-20 从私有工作库脱敏重建的公开版**，供分享 + 日常自用。
  私人工作档案（真实项目素材的原始测试记录、内部交接文档）不发布；
  `evaluation/benchmark-a-results.md` 等涉及文件已匿名化改写，工程结论完整保留。
## Current phase

**Library assembled.** Both curated sources are published as browsable libraries, and
the eight local design-system sources are crossed against them in [`themes/`](themes/).

The licence line decides the shape: Video Shotcraft is Apache-2.0, so `shots/` copies the
implementations in; Locomotion ships no LICENSE, so `layouts/` links and never copies.
Yoru's manual decisions stay as machine-readable preference data so future agents can
pre-screen new material before human review.

## Workflow

1. **Inventory — Akari**: collect and classify relevant repositories, galleries, templates, component libraries, editors and agent workflows.
2. **Preview / screening — Yoru**: review candidates in a local HTML preview and mark each stable ID as `keep`, `maybe`, or `reject`.
3. **Export**: export the complete decision set as JSON, including negative samples.
4. **Ingest — Akari / agent**: preserve the complete JSON snapshot as the source of truth; regenerate human-readable curation views and a preference profile from it.
5. **Pre-screen future material — agent**: use historical exact IDs, template-family patterns, style patterns and rejects to rank new material, then return uncertain / novel cases to Yoru.
6. **Practical tests — Claude**: run shortlisted assets against the same benchmark material and inspect visual quality, parameterization and code ergonomics.
7. **Acceptance — GPT / Akari**: verify render stability, aspect-ratio behavior, dependencies, licensing and whether the result actually matches the intended style.
8. **Integration**: only then adapt selected ideas/components into the future `YORU Motion System`.

`candidate material → local HTML preview → stable ID → keep / maybe / reject → full JSON export → repository ingest → generated readable views + preference profile → agent pre-screen → Yoru final decision`

**Reject is valuable data.** Do not delete negative samples or silently collapse the dataset to keep-only.

## Entry points

- [`shots/`](shots/) — **the browsable shot library**: one directory per kept reference, each with a Chinese summary, the measured parameter table, the known pitfalls, a preview link and the Apache-2.0 implementation. Readable straight from GitHub; no local server needed.
- [`layouts/`](layouts/) — **the layout index**: Locomotion's kept templates. Navigation only — upstream ships no LICENSE, so nothing is copied, but every kept variant links to a preview that plays in the browser and to the source that made it, pinned to an upstream commit.
- [`themes/`](themes/) — **the design-system cross**: one profile per local design system (palette in the library's token shape, texture, motion rules, what it forbids), plus the index that joins them to `shots/` and `layouts/`.
- [`CATALOG.md`](CATALOG.md) — human-facing click-through research list.
- [`review/`](review/) — the local screening console (`python review/serve.py`) and the machine-readable candidate datasets it loads.
- [`data/repos.yml`](data/repos.yml) — machine-readable repository inventory.
- [`categories/`](categories/) — research grouped by role.
- [`curation/locomotion-2026-08-19.json.bz2`](curation/locomotion-2026-08-19.json.bz2) — complete 427-record Locomotion JSON review snapshot, bzip2-compressed without changing its contents; source of truth for this batch.
- [`curation/locomotion-2026-08-19.meta.json`](curation/locomotion-2026-08-19.meta.json) — visible schema/source/date/count plus the SHA-256 of the uncompressed uploaded JSON.
- [`curation/liked.md`](curation/liked.md), [`curation/maybe.md`](curation/maybe.md), [`curation/rejected.md`](curation/rejected.md) — generated human-readable views of the JSON decisions.
- [`curation/video-shotcraft-2026-08-20.json.bz2`](curation/video-shotcraft-2026-08-20.json.bz2) — complete 209-record Video Shotcraft review snapshot, with its `.meta.json` checksum and generated `-liked` / `-maybe` / `-rejected` views alongside it.
- [`evaluation/locomotion-preference-profile.md`](evaluation/locomotion-preference-profile.md), [`evaluation/video-shotcraft-preference-profile.md`](evaluation/video-shotcraft-preference-profile.md) — agent-readable statistics, patterns and pre-screening rules for each source.
- [`evaluation/`](evaluation/) — taste vocabulary, benchmark plan and acceptance matrix.
- [`legal/license-tracker.yml`](legal/license-tracker.yml) — upstream license status and reuse notes.
- [`scripts/sync-locomotion-curation.py`](scripts/sync-locomotion-curation.py) — validates the snapshot and regenerates/checks the Markdown views.
- [`scripts/build-review-datasets.py`](scripts/build-review-datasets.py) — builds `review/datasets/*.json` from the upstream sources.
- [`scripts/import-curation-export.py`](scripts/import-curation-export.py) — validates a console export and ingests it into `curation/`.

## Screening console

`review/index.html` is the single screening surface for every source. It is
dataset-driven: `review/datasets/*.json` carry the candidates, the preview URLs
and the provenance that ends up in an export, so a new upstream library needs an
adapter in `scripts/build-review-datasets.py`, not a second page.

```bash
python review/serve.py                       # serve the parent dir, open the console
python scripts/build-review-datasets.py      # regenerate the candidate datasets
python scripts/import-curation-export.py <exported.json>
```

| dataset | candidates | unit of review |
| --- | --- | --- |
| `locomotion` | 427 | one rendered style variant |
| `video-shotcraft` | 209 | one previewable style/shot across 152 shot cards |

Preview media is never copied into this repository: Locomotion plays from the
sibling `locomotion-free/` checkout, Video Shotcraft from the sibling
`video-shotcraft/` checkout with the upstream GitHub Pages URL as fallback.

See [`review/README.md`](review/README.md) for the full loop.

## Stable IDs

Video Shotcraft records use `video-shotcraft/<card>/<style>`, for example
`video-shotcraft/beat-cut-moves/paparazzi-flash`. Exported rows additionally keep
the upstream repo and commit, category, source recipe path and preview URL, so a
verdict stays resolvable without this checkout.

## Locomotion stable IDs

Locomotion records use `locomotion/<template>/<style>`, for example `locomotion/bar-chart-reveal/glass`.

The source record keeps the exact `base` template, `style`, MP4 `file`, `status`, `score`, and `note`. Human-readable descriptions are supplemental and must never become the only index.

## Proposed motion taxonomy

- **Style**: Editorial / Fresh / Playful / Kinetic / Tech / Experimental / Cinematic / Documentary / Fashion-Pop
- **Rhythm**: Slow / Medium / Fast
- **Purpose**: Intro / Outro / Transition / Title / Lower Third / Image Motion / Caption / Data / SFX
- **Palette**: reusable color presets with background, surface, primary, secondary, accent, text, muted and line tokens
- **Format**: 16:9 / 9:16 / 1:1, ideally from responsive compositions rather than separate hard-coded templates

## Ground rules

- A good demo is not proof that a component will still look good with ordinary work material.
- Visual screening comes before engineering validation.
- The Locomotion JSON snapshot is the source of truth; generated Markdown must not drift into a parallel fact source.
- Rejects are retained as negative evidence.
- Agents may pre-screen; Yoru owns the final keep / maybe / reject decision.
- No silent fallback or weakened acceptance criteria during testing.
- Third-party code is only imported after its license is verified and attribution requirements are recorded.
- Audio, fonts, images and other bundled assets are tracked separately from source-code licensing.

## Curation maintenance

The snapshot is stored as standard bzip2 so the uploaded JSON bytes remain exact while keeping the repository diff small. `scripts/sync-locomotion-curation.py` decompresses it with Python's standard library.

```bash
python scripts/sync-locomotion-curation.py
python scripts/sync-locomotion-curation.py --check
```

The check verifies the uncompressed SHA-256, schema, 427-record count, required fields, unique stable IDs, status values, and `locomotion/<base>/<style>` traceability before comparing generated Markdown.
