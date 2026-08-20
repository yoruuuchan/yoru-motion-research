# YORU Content

> 铅字房：冷调青白纸、宋体铅字、文武线、汉字页码、月相报头。自排技术周刊质感。

| | |
|---|---|
| 目录 | `D:\DESIGN\YORU Content Design System (2)` |
| 明暗 | 只有浅色（内容层）；图表子系统定义了暗色 token（diagram.css:64-75） |
| 质感 | hairline |
| 字体 | 思源宋体 / Inter+思源黑体 / 仿宋 STFangsong |

## 它是什么感觉

冷调青白纸 #F2F5F5 上的宋体铅字，墨色偏海军蓝不走暖灰。页面家具是月相行 + 文武线 + 汉字页码 + 直排书脊——没有 logo、没有文字字标、没有图标，识别度全靠排版节奏。强调靠着重号和荧光笔（每页各限一条），不靠颜色。四个子变体（Signal / Lab / Studio / Special）只在强调色和装饰细节上分开，母语言完全一致。内容里没有动效，画面是静止的纸。

## Palette

浅色套（内容层直接有 token 支撑）：

```ts
const yoruContentLight: Palette = {
  id: 'yoru-light',
  mode: 'light',
  bg: '#F2F5F5',         // colors.css:32 --surface-page
  surface: '#FFFFFF',    // colors.css:5  --paper-1
  surfaceAlt: '#E9EFF0', // colors.css:5  --paper-3
  ink: '#1B2127',        // colors.css:3  --ink-1（via --text-title, :25）
  inkMuted: '#7B8798',   // colors.css:3  --ink-4（via --text-muted, :27）
  inkFaint: '#A9B4C4',   // colors.css:3  --ink-5（via --text-faint, :28）
  line: '#DEE5E8',       // colors.css:7  --line-1（--border-hair, :37）
  lineStrong: '#1B2127', // colors.css:7  --line-3（= ink-1, --border-strong, :39）
  accent: '#3186FF',     // colors.css:14 --accent（Signal 默认；variants.css:9 确认）
  accentInk: '#FFFFFF',  // colors.css:30 --text-inverse
                         // ← 这是决定不是测量：Palette 的 accentInk = "压在 accent 上的文字色"，
                         // 系统的 --accent-ink (#1B5FC7) 语义不同（accent 色调的文字，用在浅底上），
                         // 此处取 --text-inverse 做映射。
  accentSoft: '#D0E8FF', // colors.css:16 --accent-soft
  positive: '#1E8A66',   // colors.css:20 --ok
  negative: '#A62733',   // colors.css:22 --stop
  ramp: ['#A9B4C4', '#7B8798', '#4A5566', '#1B2127'],
  // ink-5, ink-4, ink-3, ink-1（全部来自 colors.css:3 墨阶）
  // diagram.css 注释明确："Eight roles never become eight hues"；
  // variants.css 的四变体 accent 是一次一个，不是同屏数据系列。
  // 故 ramp 遵循筛选结论的明度梯度规则，浅底上低→高 = 浅→深。
};
```

暗色套（该系统没有页面级暗色模式——readme.md:133「深色只出现在代码块和 tone="ink" 封面」。以下值取自图表子系统暗色 token + 推导）：

```ts
const yoruContentDark: Palette = {
  id: 'yoru-dark',
  mode: 'dark',
  bg: '#111827',         // diagram.css:65 --dg-surface [data-dg-theme="dark"]
  surface: '#1E2739',    // diagram.css:66 --dg-surface-2
  surfaceAlt: '#18202F', // diagram.css:67 --dg-surface-3
  ink: '#EDF7FF',        // diagram.css:68 --dg-fg
  inkMuted: '#C1D7EF',   // diagram.css:69 --dg-fg-2（= colors.css:3 --ink-6）
  inkFaint: '#7B8798',   // diagram.css:70 --dg-fg-3（= colors.css:3 --ink-4）
  line: '#2C3644',       // diagram.css:71 --dg-line
  lineStrong: '#EDF7FF', // diagram.css:72 --dg-line-strong
  accent: '#3186FF',     // colors.css:14 —— 暗色下不变
  accentInk: '#FFFFFF',  // 无对应 — 这是决定不是测量：同浅色套，取 --text-inverse
  accentSoft: '#23394F', // 无对应 — 这是决定不是测量：
                         // diagram.css:107 用 color-mix(in oklch, accent 20%, surface) 做类似推导，
                         // 此值方向一致但为手算，需校验
  positive: '#45C496',   // 无对应 — 这是决定不是测量：
                         // --ok #1E8A66 在 #111827 上对比度约 3.1:1，不够；
                         // 提亮至 #45C496 达约 7.5:1（恰好 = Studio 变体 accent，巧合）
  negative: '#C15A52',   // 无对应 — 这是决定不是测量：
                         // --stop #A62733 在 #111827 上约 2.4:1；
                         // 改用 --warn 色阶 #C15A52（colors.css:21）达约 4.5:1
  ramp: ['#2C3644', '#7B8798', '#C1D7EF', '#EDF7FF'],
  // dg-line, dg-fg-3, dg-fg-2, dg-fg（diagram.css:68-71）
  // 暗底上低→高 = 深→浅
};
```

## 和已有 yoruLight / yoruDark 的差异

### yoruLight（palettes.ts:55-72）

大多数值完全一致。差异两处：

**1. ramp 前两步**

| | ramp[0] | ramp[1] | ramp[2] | ramp[3] |
|---|---|---|---|---|
| 已有 | #B9C7CC | #8695A6 | #4A5566 | #1B2127 |
| 本文 | #A9B4C4 | #7B8798 | #4A5566 | #1B2127 |

#B9C7CC 和 #8695A6 不在 token 文件中——位于 ink-5 和 ink-6 之间的插值。本文改用 ink-5 和 ink-4，全部来自 colors.css:3。已有版本的起点更浅（视觉范围略宽），但引入了非 token 值。建议用 token 值——四步已经覆盖足够的明度跨度。

**2. accentInk 语义**

值一致（#FFFFFF），但出处需要说清楚。系统 token 里叫 `--accent-ink` 的是 #1B5FC7（accent 色调的文字，用在浅底上），和 Palette 里 `accentInk`（压在 accent 底上的文字）含义不同。正确的映射源是 `--text-inverse: #FFFFFF`（colors.css:30）。

### yoruDark（palettes.ts:74-91）

该设计系统没有页面级暗色模式。已有 yoruDark 用内容层墨阶反转构建；本文用图表子系统暗色 token 构建。逐项比对：

| 角色 | 已有 | 本文 | 差异与建议 |
|---|---|---|---|
| bg | #12171C | #111827 | 已有值不在任何 token 文件中。#111827 来自 diagram.css:65，是系统里唯一显式声明的暗色底。ΔE≈4。建议用 #111827。 |
| surface | #1B2127 | #1E2739 | 已有 = ink-1；本文 = diagram.css:66 --dg-surface-2。ink-1 在暗模式下同时充当了 lineStrong，两角色撞色。建议用 diagram 值。 |
| surfaceAlt | #2C3440 | #18202F | 已有 = ink-2，层次差更大（ΔL≈8）；本文 = diagram.css:67，层次差小（ΔL≈3）。两个都可以，取决于面板层次需求。 |
| ink | #F7FAFA | #EDF7FF | 已有 = paper-2（偏纯白）；本文 = diagram.css:68 --dg-fg（偏蓝）。dg-fg 和冷调墨阶更统一。微偏好 #EDF7FF。 |
| inkMuted | #A9B4C4 | #C1D7EF | 已有 = ink-5（在 #111827 上约 5.5:1）；本文 = ink-6/dg-fg-2（约 8.2:1）。已有版本偏弱。建议用 #C1D7EF。 |
| inkFaint | #4A5566 | #7B8798 | 已有 = ink-3（在 #111827 上约 2.5:1）；本文 = ink-4/dg-fg-3（约 4.0:1）。已有版本太暗。建议用 #7B8798。 |
| line | #2C3440 | #2C3644 | ΔE<2，差异可忽略。 |
| lineStrong | #C1D7EF | #EDF7FF | 已有 = ink-6；本文 = dg-line-strong。已有版本的 lineStrong 和本文的 inkMuted 撞色。建议用 #EDF7FF。 |
| accentSoft | #23394F | #23394F | 一致。均为推导值。 |
| positive | #45C496 | #45C496 | 一致。均为推导值。注意：该值 = Studio 变体 --accent（variants.css:37），这是巧合——如果 Studio 换色此处不应跟着变。 |
| negative | #C15A52 | #C15A52 | 一致。= --warn（colors.css:21），在暗底上替代 --stop。 |
| ramp | [#2C3440, #4A5566, #A9B4C4, #F7FAFA] | [#2C3644, #7B8798, #C1D7EF, #EDF7FF] | 已有用墨阶反转，本文用 diagram 暗色 token。中间两步的差异和 inkFaint/inkMuted 的修正一致——ink-3/ink-5 在暗底偏弱。建议用 diagram 值。 |

### 关于「数据 ramp 故意保持中性不走蓝色」的注释（palettes.ts:52-54）

部分准确，措辞有误导。token 文件自身描述墨阶为「cool, navy-tinted」（colors.css:2），墨阶本身就带海军蓝色调，并非纯中性灰。注释想表达的区分是「ramp 不用 accent blue #3186FF，而是走墨阶」——这是对的。diagram.css 确认图表不用多色相编码数据系列，variants.css 的四变体 accent 是一次一个不是同屏四色。但把墨阶叫「neutral」不精确，建议改为「ramp 走墨阶的冷色明度梯度，不走 accent 蓝」。

**该判断在 token 文件里有没有依据**：有。diagram.css 的注释（第 1-14 行）和角色定义明确说了「Eight roles never become eight hues」和「colour carries only three meanings (accent = machine, ink = human, semantic = status)」。颜色不编码数据系列是设计系统的显式规则，不是自由发挥。但「中性」这个词是不准确的——应该说「墨阶」。

## 质感 skin

**hairline**。

依据：该系统的核心视觉元素是 1px 发丝线（borders.css:2 `--hair: 1px`）和极细边框（`--rule: 2px`，borders.css:2），有微妙阴影（仅限 PromptBlock/CodeBlock 的内凹阴影 `--shadow-inset`，borders.css:20），整体是「细线+柔影」气质。四个 skin 里 hairline 最匹配。

排除理由：
- brutalist — 该系统有等宽大写标签但不是整体粗暴风格，默认有 2px 圆角不是 0
- glass — 明确没有玻璃拟态（readme.md:110）、没有透明模糊（readme.md:129）
- flat — 该系统有边框（发丝线是核心元素）和阴影（内凹阴影），flat 的「无边框无阴影」不对

**圆角不匹配**：hairline 的 `radius: 14` 远大于该系统的 `--radius-1: 2px`（borders.css:6）。该系统默认接近直角，圆角是 Studio/Special 的变体特权（readme.md:125「不要出现 8px/12px 的通用圆角卡片」）。如果 skin 的 radius 会覆写到渲染结果，需要在应用层压到 2。

证据数值：
- `--hair: 1px` — borders.css:2
- `--rule: 2px` — borders.css:2
- `--wu: 2.5px`（文武线粗线） — borders.css:4
- `--radius-1: 2px` — borders.css:6
- `--shadow-inset: inset 2px 2px 5px rgba(122,152,188,.26), inset -2px -2px 5px rgba(255,255,255,.92)` — borders.css:20
- `--shadow-media: 0 1px 2px rgba(17,24,39,.05), 0 8px 24px rgba(17,24,39,.07)` — borders.css:12

## 动效规则

readme.md:133——「动效：内容里没有动效。工具台交互 `.12s` 线性色彩过渡一档。」

没有缓动曲线 token，没有入场/退场时长，没有 transition-duration 变量。工具台的 0.12s linear 色彩过渡不适用于内容输出。这套系统的动效规则就是**没有**。

## 硬规则（违反了就不像它了）

- 页面底是青白纸 #F2F5F5，不是纯白；纯白只给卡片内局部面。（CLAUDE.md:31, readme.md:106）
- 不做左侧 accent bar、彩色 border-left、时间轴式竖线做版块装饰。结构交给排版层级和横线。（CLAUDE.md:24, readme.md:89-93）
- 阴影只在 PromptBlock 和 CodeBlock 上，且是内凹的；页面、卡片、Callout、表格一律无阴影。（CLAUDE.md:27-28, readme.md:94）
- 圆角默认 2px，8px/12px 通用圆角禁止；圆角是 Studio/Special 变体特权。（readme.md:125, borders.css:6）
- 没有渐变、没有玻璃拟态、没有发光边框、没有彩色阴影。（readme.md:110）
- 不用 emoji，一个都不用。状态用 StatusLabel，层级用编号。（readme.md:56）
- 没有文字字标，标识是月相行报头。（CLAUDE.md:36, readme.md:16）
- 没有黄色；注意用玫红 #C15A52，避坑用深红 #A62733。没有紫色、没有橙色。（readme.md:30, :109, colors.css:18-22）
- 一页最多一个强调色 + 一个语义色；正文永不着色。（readme.md:108）
- 着重号只打扛整句的两三个字；荧光笔每页一条；手写旁批每页一条且非承重。（CLAUDE.md:38-39, readme.md:78-82）
- 图表节点角色靠形状与描边区分，绝不变成多种颜色。颜色只有三种含义：墨/accent/语义。（readme.md:167-169, diagram.css:1-14）
- 背景纯色，不用图片背景、纹理、网格底纹。（readme.md:112）
- 内容完全不透明；导出物里没有任何透明或模糊。（readme.md:129）

## 不适合的镜头

- **霓虹辉光 / 发光描边 / 彩色阴影** — 明确没有发光边框和彩色阴影（readme.md:110）
- **多色数据系列（3+ 色相的饼图、折线、堆叠面积图）** — 图表只用三种颜色含义，角色靠形状编码不靠色相（readme.md:167-169）
- **频闪黑帧 / 高对比度闪烁** — 内容层完全没有动效，突然的黑帧和闪烁与静纸质感冲突
- **3D 相机飞行 / 透视旋转 / Z 轴运动** — 平面印刷气质，没有 z 轴概念
- **毛玻璃 / 磨砂叠层 / 半透明卡片** — 没有玻璃拟态（readme.md:110），导出物无透明无模糊（readme.md:129）
- **弹性动画 / 果冻变形** — 铅字房静气不兼容弹性形变
- **圆角卡片飘入（8px+ 圆角）** — 默认 2px，8px/12px 圆角禁止（readme.md:125）
- **emoji 粒子 / emoji 装饰** — 零 emoji 铁律（readme.md:56）
- **彩虹渐变 / 多色渐变文字** — 没有渐变，色板里没有紫/橙/黄（readme.md:30, :110）
- **左侧色条动画 / accent bar 滑入** — 明确禁止 accent bar 和彩色 border-left（readme.md:89-93）

## 出处

tokens 目录（`D:\DESIGN\YORU Content Design System (2)\tokens\`）：
- `colors.css` — 墨阶、纸阶、线阶、accent、状态色、语义别名
- `diagram.css` — 图表子系统色板（含暗色）、角色编码、边线
- `variants.css` — 四变体 accent 覆写、圆角、行高
- `borders.css` — 发丝线 / 文武线 / 阴影 / 圆角
- `fonts.css` — 字体栈、@font-face
- `typography.css` — 字号 / 行高 / 字距 / 字重
- `base.css` — 根元素样式
- `spacing.css` — 间距 scale
- `layout.css` — 画布尺寸 / 边距

设计系统根目录：
- `readme.md` — 完整设计指南（视觉基础、签名动作、图表子系统、内容基础）
- `CLAUDE.md` — 硬规则（CJK 栈、阴影限制、圆角限制、签名动作）
- `SKILL.md` — 技能入口

已有实现：
- `E:\remotion\yoru-motion-system\src\themes\palettes.ts` — yoruLight / yoruDark
- `E:\remotion\yoru-motion-system\src\themes\skins.ts` — 四种质感 skin
