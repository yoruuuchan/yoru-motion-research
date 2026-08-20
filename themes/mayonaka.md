# Mayonaka 真夜中

> 深夜蒸汽波电台——霓虹、像素、故障艺术、扫描线、CRT 余晖

| | |
|---|---|
| 目录 | `D:\DESIGN\Mayonaka Design System` |
| 明暗 | 只有深色 |
| 质感 | brutalist |
| 字体 | Press Start 2P / VT323 / DotGothic16 |

## 它是什么感觉

凌晨三点，便利店对面那间没有招牌的唱片店。落地窗透出品红和青色的光，扫描线在 CRT 显示器上慢慢漂移。所有字都是像素点阵，棱角分明，没有圆角，没有模糊。两套光：UI 用硬阴影（像素级、无模糊、偏移 4px），强调用霓虹辉光（大范围 blur 的品红/青/蓝色发光）。英文和日文混排在同一个画面里，不翻译，叠。整体克制——过渡 120-240ms，故障特效默认是静态的。

## Palette

```ts
export const mayonakaDark: Palette = {
  id: 'mayonaka-dark',
  mode: 'dark',
  bg: '#100225',         // --midnight (--bg-base)                tokens/colors.css:4
  surface: '#1c0838',    // --aubergine (--bg-raised)             tokens/colors.css:5
  surfaceAlt: '#0a1654', // --deep-blue (--bg-card)               tokens/colors.css:23
  ink: '#f0eaff',        // --chrome (--text-primary)             tokens/colors.css:25
  inkMuted: '#c8bce0',   // --silver (--text-secondary)           tokens/colors.css:26
  inkFaint: '#7a6ba0',   // --dusk (--text-muted)                 tokens/colors.css:27
  line: '#202F62',       // DECISION: --border-default 是 rgba(74,163,255,0.28)，palette 需要不透明值，按 alpha composite 在 bg (#100225) 上算出    tokens/colors.css:43
  lineStrong: '#f0eaff', // DECISION: 系统的 --border-strong 是品红色 rgba(255,43,214,0.6)，但 lineStrong 是结构性强边框（轴线、表格头），不是装饰强调；取 ink 值以保持中性    tokens/colors.css:25,44
  accent: '#ff2bd6',     // --magenta (--accent-primary)          tokens/colors.css:9
  accentInk: '#07000f',  // DECISION: 无 text-on-accent token；--void 是系统最深黑，在亮品红上给出最大对比    tokens/colors.css:3
  accentSoft: '#2d0a55', // DECISION: 无 accent-soft token；--plum 是系统 token 中最接近 magenta@10% on midnight 的值（理论值 #280637）    tokens/colors.css:6
  positive: '#6dffb5',   // --success                             tokens/colors.css:54
  negative: '#ff3860',   // --danger                              tokens/colors.css:56
  ramp: ['#4a1a8a', '#7a6ba0', '#c8bce0', '#f0eaff'],
  // DECISION: 系统没有数据 ramp token；从现有颜色阶梯中选取四档明度：
  // orchid (#4a1a8a) -> dusk (#7a6ba0) -> silver (#c8bce0) -> chrome (#f0eaff)
  // 全部是系统 token，但"用这四个做数据梯度"是决定不是测量
  // tokens/colors.css:7,27,26,25
};
```

## 质感 skin

选 **brutalist**。

证据：
- 圆角：系统默认 `--radius-none: 0`（`tokens/spacing.css:16`），readme 写 "Pixel UI is **sharp**. Default radius is `0`"。brutalist 的 `radius: 0` 完全匹配。
- 边框：`--bw-default: 2px`（`tokens/spacing.css:23`）。brutalist 的 `borderWidth: 2` 匹配。
- 阴影：系统用硬偏移阴影 `--shadow-pixel: 4px 4px 0`（`tokens/effects.css:15`），不用柔影。brutalist 的 `shadow: null` + `offsetShadow: 6` 概念一致。
- 大写标签：readme 写 "Display headlines and UI labels: ALL CAPS"。brutalist 的 `upperLabels: true` 匹配。
- 等宽正文：body 字体是 VT323（等宽终端字体，`tokens/fonts.css:11`）。brutalist 的 `monoBody: true` 匹配。

需要调整的参数：
- `offsetShadow`：系统像素阴影是 4px 偏移（`tokens/effects.css:15`），brutalist 默认 6。**改 6 -> 4**。
- `radiusSmall`：系统偶尔用 `--radius-sm: 2px` 在输入框上（`tokens/spacing.css:17`），brutalist 默认 0。如果渲染输入框，**可改 0 -> 2**，否则保持 0。

## 动效规则

`tokens/` 里**没有 motion.css 文件**。但动效 token 存在于 `tokens/effects.css:41-45`：

| token | 值 | 出处 |
|---|---|---|
| `--dur-fast` | `120ms` | `tokens/effects.css:43` |
| `--dur-med` | `240ms` | `tokens/effects.css:44` |
| `--dur-slow` | `480ms` | `tokens/effects.css:45` |
| `--ease-smooth` | `cubic-bezier(.2,.7,.2,1)` | `tokens/effects.css:42` |
| `--ease-pixel` | `steps(6, end)` | `tokens/effects.css:41` |

用法规则（`readme.md:82`）：
- `--dur-fast` 用于 hover，`--dur-med` 用于 tab 切换和过渡
- `--ease-smooth` 用于普通 UI，`--ease-pixel` 用于想要 8-bit 感的逐帧动画
- 故障特效**默认是静态的**，只在报错和入场时才动画化
- **明令禁止**：scale bounce、弹簧（spring）动画（`readme.md:82` "Never use scale bounces or playful springs"）

预置关键帧动画（`tokens/effects.css:49-87`）：`mnk-pulse-magenta`/`cyan`/`blue`（辉光呼吸），`mnk-flicker`（信号闪烁），`mnk-scanline-drift`（扫描线漂移），`mnk-marquee`（跑马灯），`mnk-glitch-shake`（故障抖动），`mnk-blink`（光标闪烁），`mnk-sun-spin`（色相旋转）。

## 硬规则（违反了就不像它了）

- **只有深色模式**，没有浅色。`--bg-base` 是 `--midnight`（`SKILL.md:17`）
- **像素字体必须关闭抗锯齿**：`font-smoothing: none`（`tokens/typography.css:34`）
- **默认直角**，圆角为 0，除非有明确理由（`SKILL.md:19`，`tokens/spacing.css:16`）
- **两套光不混用**：像素硬阴影给 UI，霓虹辉光给强调，同一元素不叠加（按钮例外）（`readme.md:66-71`）
- **英日混排不翻译**：Mix EN + JP on the same screen; never translate, layer（`SKILL.md:21`）
- **不用 emoji**，用 Lucide 图标或像素字形 `▶ ■ ◆ ★`（`SKILL.md:22`，`readme.md:100-103`）
- **不用 backdrop-blur**，边缘保持锐利；遮罩用实色 70-85% 面板（`readme.md:78`）
- **不用句式大小写**：UI 标签全大写或全小写，never sentence case（`readme.md:34`）
- **hover 是位移 + 阴影变化**，不是透明度；透明度只用在 disabled (0.4)（`readme.md:72-73`）

## 不适合的镜头

- **弹簧回弹 / scale bounce**：系统明确禁止（`readme.md:82`）
- **亮白大底 / 浅色背景**：系统只有深色模式
- **圆角毛玻璃 / glassmorphism**：系统默认直角，禁止 backdrop-blur
- **彩色数据系列**：ramp 是单色相明度梯度，不用色相编码数据
- **柔和高斯模糊过渡**：系统美学是锐利和像素化的，边缘必须 crisp
- **anti-aliased 平滑字体飞入**：像素字体必须关闭抗锯齿，平滑渲染直接破坏美感
- **企业感极简白 / 干净留白**：蒸汽波的杂味（扫描线、网格地板、霓虹）是核心，干净画面没有这套系统的味道
- **缓慢大幅度位移动画（>480ms）**：最长时长 token 是 480ms，再慢就拖沓

## 出处

| 文件 | 路径 |
|---|---|
| SKILL.md | `D:\DESIGN\Mayonaka Design System\SKILL.md` |
| readme.md | `D:\DESIGN\Mayonaka Design System\readme.md` |
| tokens/colors.css | `D:\DESIGN\Mayonaka Design System\tokens\colors.css` |
| tokens/effects.css | `D:\DESIGN\Mayonaka Design System\tokens\effects.css` |
| tokens/fonts.css | `D:\DESIGN\Mayonaka Design System\tokens\fonts.css` |
| tokens/typography.css | `D:\DESIGN\Mayonaka Design System\tokens\typography.css` |
| tokens/spacing.css | `D:\DESIGN\Mayonaka Design System\tokens\spacing.css` |
| guidelines/motion.html | `D:\DESIGN\Mayonaka Design System\guidelines\motion.html` |
| guidelines/borders-radii.html | `D:\DESIGN\Mayonaka Design System\guidelines\borders-radii.html` |
| palettes.ts (参考) | `E:\remotion\yoru-motion-system\src\themes\palettes.ts` |
| skins.ts (参考) | `E:\remotion\yoru-motion-system\src\themes\skins.ts` |
