# RIFT

> 冷色系赛博玻璃控制台，蓝光 + 色差边缘 + CRT 扫描线

| | |
|---|---|
| 目录 | `D:\DESIGN\RIFT Design System` |
| 明暗 | 双套（dark 默认，light 纯 token 翻转，叫 daybreak / 黎明） |
| 质感 | glass |
| 字体 | Space Grotesk / Rajdhani / Zen Kaku Gothic New |

## 它是什么感觉

凌晨四点的机房监控台。画面全是深蓝玻璃面板，叠着 72px 网格底纹和若隐若现的 CRT 扫描线。文字边缘有一道天蓝 × 宝蓝的色差裂缝——整个系统唯一的「装饰」就是这条缝。浅色模式把玻璃底翻成冰蓝，结构不变，像屏幕从深夜切到破晓。没有温色，没有插画，没有 emoji，只有状态点的微光和 `裂隙` 两个汉字。

## Palette

RIFT 的分隔线 token 是半透明 rgba 值（为玻璃面板设计），展平为 hex 时以 `--bg-surface` 作为合成底色。`accentSoft` 在系统里没有对应 token，以 royal 色 15% 透明度覆盖在 `--bg-surface` 上推导。

```ts
export const riftDark: Palette = {
  id: 'rift-dark',
  mode: 'dark',
  bg: '#070C1B',        // tokens/theme-dark.css:12  --bg-base
  surface: '#0E1830',   // tokens/theme-dark.css:13  --bg-surface
  surfaceAlt: '#15233F',// tokens/theme-dark.css:14  --bg-elevated
  ink: '#EDF2FF',       // tokens/theme-dark.css:18  --ink-1
  inkMuted: '#A7B4D2',  // tokens/theme-dark.css:19  --ink-2
  inkFaint: '#6B7896',  // tokens/theme-dark.css:20  --ink-3
  line: '#24314B',      // 决定：--line-2 rgba(184,220,255,0.13) 展平到 --bg-surface #0E1830 上
  lineStrong: '#374762',// 决定：--line-strong rgba(184,220,255,0.24) 展平到 --bg-surface #0E1830 上
  accent: '#5C7BFF',    // tokens/palette.css:9  --royal
  accentInk: '#FFFFFF', // components.css:83  .rift-btn--primary color
  accentSoft: '#1A274F',// 决定：royal #5C7BFF 15% 透明度展平到 --bg-surface #0E1830 上，无对应 token
  positive: '#4DCB97',  // tokens/palette.css:18  --ok
  negative: '#FF7480',  // tokens/palette.css:19  --bad
  ramp: ['#3E4866', '#6B7896', '#A7B4D2', '#EDF2FF'],
  // ramp 取 ink 四级：ink-4 → ink-3 → ink-2 → ink-1（tokens/theme-dark.css:21→18）
  // 系统全色谱为冷蓝，ink 级本身就带蓝色调，符合「不用色相编码数据」规则
};
```

```ts
export const riftLight: Palette = {
  id: 'rift-light',
  mode: 'light',
  bg: '#EAF1FC',        // tokens/theme-light.css:11  --bg-base
  surface: '#F4F8FF',   // tokens/theme-light.css:12  --bg-surface
  surfaceAlt: '#DCE7F8',// tokens/theme-light.css:14  --bg-sunken
  ink: '#0A1430',       // tokens/theme-light.css:17  --ink-1
  inkMuted: '#3E4F76',  // tokens/theme-light.css:18  --ink-2
  inkFaint: '#6B7896',  // tokens/theme-light.css:19  --ink-3
  line: '#D2DAE7',      // 决定：--line-2 rgba(20,45,95,0.15) 展平到 --bg-surface #F4F8FF 上
  lineStrong: '#B1BBCF',// 决定：--line-strong rgba(20,45,95,0.30) 展平到 --bg-surface #F4F8FF 上
  accent: '#3F5BE6',    // tokens/theme-light.css:23  --royal（浅色模式加深以保持可读性）
  accentInk: '#FFFFFF', // components.css:83  .rift-btn--primary color
  accentSoft: '#D9E0FB',// 决定：light royal #3F5BE6 15% 透明度展平到 --bg-surface #F4F8FF 上，无对应 token
  positive: '#4DCB97',  // tokens/palette.css:18  --ok（系统未按明暗分化状态色）
  negative: '#FF7480',  // tokens/palette.css:19  --bad（系统未按明暗分化状态色）
  ramp: ['#A6B6D4', '#6B7896', '#3E4F76', '#0A1430'],
  // ramp 取 ink 四级：ink-4 → ink-3 → ink-2 → ink-1（tokens/theme-light.css:20→17）
};
```

## 质感 skin

选 **glass**。

证据：

- 圆角：RIFT `--r-lg: 18px`（`tokens/spacing.css:19`），glass skin `radius: 18` — 完全吻合。`--r-sm: 10px`（`tokens/spacing.css:17`），glass `radiusSmall: 10` — 完全吻合。
- 边框：glass skin `borderWidth: 0`，但 RIFT 所有玻璃面板带 `1px solid var(--glass-border)`（`components.css:8-9`），readme 称这是「the system's most repeated detail」。需要把 `borderWidth` 覆盖为 `1`。
- 阴影：glass skin 的阴影 `0 24px 64px rgba(0,0,0,0.12), 0 2px 8px rgba(0,0,0,0.06)` 是四个 skin 里最重的，方向正确。但 RIFT 实际阴影更重：`--shadow-lg` 的 alpha 到 0.45（`tokens/theme-dark.css:39`）。
- 无偏移阴影（`offsetShadow: 0`）— 吻合。
- 不全大写（`upperLabels: false`）— 吻合：RIFT 只在状态标签用全大写等宽，正文不用。
- 正文不用等宽（`monoBody: false`）— 吻合：正文用 Rajdhani。

与 glass 的差异：只有 `borderWidth` 需要从 0 改为 1。其余三个 skin 的偏差都更大（hairline 圆角偏 4px 且阴影太轻；brutalist 直角零圆角；flat 无阴影无边框）。

## 动效规则

RIFT 有完整的动效 token（`tokens/motion.css`）：

- `--ease-out: cubic-bezier(0.22, 1, 0.36, 1)` — 收回/退出（`tokens/motion.css:4`）
- `--ease-rise: cubic-bezier(0.16, 1, 0.30, 1)` — 肯定性状态变化：悬停上浮、滑入（`tokens/motion.css:5`）
- `--dur-fast: 140ms` — 按钮按下（`tokens/motion.css:7`）
- `--dur-base: 320ms` — 悬停、聚焦环（`tokens/motion.css:8`）
- `--dur-slow: 720ms` — 挂载过渡（`tokens/motion.css:9`）
- 悬停上浮量：按钮 `-1px`，卡片 `-3px`（`components.css:76, 42`）
- 按下回弹 `translateY(0)`（`components.css:77`）— 无颜色变化，反馈由色差涟漪提供（`readme.md:59`）
- **禁止弹簧和回弹**：「No bounces, no spring overshoot」（`readme.md:57`）
- 唯一的无限动画：色差撕裂循环 3.6-7s（`effects.css:34-36`）和可选的呼吸光晕 3.2s（`effects.css:66`）

## 硬规则（违反了就不像它了）

- 全色谱只能在冷色区间内：midnight → slate → steel → royal → cobalt → sky → ice → aqua → aurora。没有暖色。（`readme.md:43`）
- 没有 emoji，没有图标字体。视觉符号只有：状态点（7px 发光圆点）、Unicode 等宽符号（`▲ ▼ — → ← ↑ ↓ · //`）、汉字 `裂隙`。（`readme.md:83-88`）
- 系统建立在玻璃上。文字必须在模糊面板之上，不能在模糊之后。不要用 `opacity:0.5` 做禁用态。（`readme.md:62-63`）
- 色差边缘（天蓝 × 宝蓝双色调分裂）是整个系统的核心视觉想法。（`readme.md:7-8`）
- 每屏最多一个 `.rift-frame`（战术 L 角括号）、一个 `.rift-scan`（CRT 扫描线）、一个 `.rift-mark`（汉字水印）。（`readme.md:73-75`）
- 没有插画，没有网格以外的纹理。如果需要照片，色温必须像凌晨四点的机房——不能是日落，不能是产品照。（`readme.md:49, 65`）
- 品牌标点：em-dash（—）、双斜杠（//）、裂隙、角括号箭头（→）。每屏不超过两个。（`readme.md:30`）
- 正文句子大小写，状态/标签/技术元数据全大写等宽。（`readme.md:28`）

## 不适合的镜头

- **弹簧回弹 / spring overshoot** — 明令禁止，RIFT 的运动只有上浮和复位，没有过冲。
- **纸质翻页 / 材质肌理** — 系统建立在玻璃面板上，纸张和有机质感与它冲突。
- **暖色调画面** — 橙/黄/红主调的实拍素材或渐变，和冷色谱直接打架。
- **多色相数据系列**（如彩虹条形图）— 系统是单色谱冷蓝，数据标记用明度梯度。
- **有机曲线 / 气泡 / blob** — RIFT 是几何玻璃 + 精确圆角，不是流体形态。
- **emoji 动画 / 卡通图标动画** — 系统没有 emoji 和插画，不可能放进去。
- **随机/混沌 glitch** — RIFT 的色差是受控的（可调 off / subtle / signature / heavy），不是故障艺术的那种随机撕裂。
- **按下变色** — readme 明确说「No color shifts on press」，反馈靠色差涟漪而不是色变。

## 出处

- `D:\DESIGN\RIFT Design System\styles.css` — @import 顺序
- `D:\DESIGN\RIFT Design System\readme.md` — 视觉基础、内容基调、硬规则
- `D:\DESIGN\RIFT Design System\SKILL.md` — 系统入口说明
- `D:\DESIGN\RIFT Design System\tokens\palette.css` — 原始色谱 + 状态色
- `D:\DESIGN\RIFT Design System\tokens\theme-dark.css` — 暗色语义层
- `D:\DESIGN\RIFT Design System\tokens\theme-light.css` — 浅色语义层
- `D:\DESIGN\RIFT Design System\tokens\motion.css` — 缓动 + 时长 + 光晕
- `D:\DESIGN\RIFT Design System\tokens\typography.css` — 字族 + 字号
- `D:\DESIGN\RIFT Design System\tokens\spacing.css` — 间距 + 圆角
- `D:\DESIGN\RIFT Design System\base.css` — body reset + 画布网格
- `D:\DESIGN\RIFT Design System\components.css` — 按钮/卡片/玻璃/输入框/徽章/状态点
- `D:\DESIGN\RIFT Design System\effects.css` — 色差 glitch / 呼吸光晕 / 游标涟漪 / 战术框 / 扫描线 / 汉字水印
- `E:\remotion\yoru-motion-system\src\themes\palettes.ts` — 现有 palette 格式参考
- `E:\remotion\yoru-motion-system\src\themes\skins.ts` — 四个 skin 定义参考
