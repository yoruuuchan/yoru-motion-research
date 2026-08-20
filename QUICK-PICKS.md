# Quick Picks — 不想翻库时从这里进

这页只做一件事：**把“我现在要做一条片子”快速路由到已有库。**

它不新增审美判断，不替代 `themes/`、`shots/`、`layouts/`，也不生成第二份数据源。
数字和结论都来自现有索引；要追根溯源，点回对应页面。

---

## 1 · 先按设计系统进

| 设计系统 | 版式先查 | 镜头结构性排除 | 101 条有代码 keep 中初筛剩余 | 细则 |
|---|---|---|---:|---|
| 青空 Aozora | `glass` | 无 | 101 | [`themes/aozora.md`](themes/aozora.md) |
| 昆仑 KUNLUN | `dark` | `spring` | 78 | [`themes/kunlun.md`](themes/kunlun.md) |
| 真夜中 Mayonaka | `brutalist` / `dark` | `spring blur` | 41 | [`themes/mayonaka.md`](themes/mayonaka.md) |
| PAPER | `default` | `spring blur 3d` | 33* | [`themes/paper.md`](themes/paper.md) |
| RIFT | `glass` / `dark` | `spring` | 78 | [`themes/rift.md`](themes/rift.md) |
| YORU Content | `default` | `spring blur 3d` | 33* | [`themes/yoru-content.md`](themes/yoru-content.md) |
| core | `brutalist` | `spring blur 3d` | 33 | [`themes/core.md`](themes/core.md) |
| Console | `glass` / `dark` | `spring 3d` | 55 | [`themes/console.md`](themes/console.md) |

\* `PAPER` 和 `YORU Content` 都不能只看这个数字。PAPER 的正式规则几乎排斥整套入场/缩放镜头；YORU Content 本身没有正式 motion spec。先读各自 theme 文件再决定。

完整逻辑和皮肤词汇映射见 [`themes/README.md`](themes/README.md)。

---

## 2 · 只想先拿个版式：从这些开始

这些是同一个版式在多套 Locomotion 皮肤下都被留下的，换设计系统时最省重新看片的时间。

| 版式 | 留下的皮肤数 | 适合拿来做什么 |
|---|---:|---|
| [`appointment-booking`](layouts/README.md#appointment-booking) | 5 | 选择、确认、表单类流程 |
| [`bar-chart-reveal`](layouts/README.md#bar-chart-reveal) | 4 | 数值对比、指标变化 |
| [`changelog`](layouts/README.md#changelog) | 4 | 更新、完成项、版本变化 |
| [`before-after`](layouts/README.md#before-after) | 3 | 改造前后、方案对比 |
| [`countdown-timer`](layouts/README.md#countdown-timer) | 3 | 倒计时、临近节点 |
| [`patient-journey`](layouts/README.md#patient-journey) | 3 | 分阶段流程、旅程叙事 |

这只是“跨皮肤稳定”，不是“任何主题都自动适配”。具体用哪套皮肤仍按上面的设计系统入口查。

---

## 3 · 只想先拿个镜头：五条结构最干净的 keep

`data/shot-traits.tsv` 目前跟踪八种手法：`spring / blur / 3d / blend / radius / gradient / glow / hue`。
下面五条 **keep** 在这八项里一项都没命中，所以很适合当“先别和设计系统打架”的起点：

- [`crash-zoom-punch`](shots/keep/camera/crash-zoom-punch/) — camera
- [`stroke-segment-build`](shots/keep/opening/stroke-segment-build/) — opening
- [`beat-cut-moves`](shots/keep/rhythm/beat-cut-moves/) — rhythm
- [`print-texture-transitions`](shots/keep/transition/print-texture-transitions/) — transition
- [`scramble`](shots/keep/typography/scramble/) — typography

**“八项都没命中”只代表结构过滤干净，不代表视觉上必然适合。** 颜色、emoji、频闪、大小写标签、实拍气质等仍要看 theme 文件里的人工规则。

---

## 4 · 已经知道自己缺哪一类镜头

直接跳到 [`shots/README.md`](shots/README.md)：

- 功能演示 → `interaction`
- 光效强调 → `effects`
- 转场 → `transition`
- 运镜 / 空间 → `camera`
- 文字 / 字卡 → `typography`
- 节奏 / 蒙太奇 → `rhythm`
- 数据 / 指标 → `data`
- 开场 / 品牌 → `opening`
- UI 登场 / 陈列 → `ui-entrance`

如果这里仍然没有答案，再去读完整的 [`themes/README.md`](themes/README.md)、[`shots/README.md`](shots/README.md) 和 [`layouts/README.md`](layouts/README.md)。
