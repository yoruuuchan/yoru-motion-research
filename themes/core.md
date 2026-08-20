# core

> weirdcore · poolcore · dreamcore · Y2K · 池核 · 后室 · 梦核 · 像素拼接 · 千禧复古

| | |
|---|---|
| 目录 | `D:\DESIGN\core Design System` |
| 明暗 | 只有浅色（冰霜底） |
| 质感 | brutalist |
| 字体 | Pixelify Sans（显示）/ Tinos（正文）/ 系统无衬线（UI 铬）|

## 它是什么感觉

不是中性底座。core 是一套有强烈视觉身份的风格系统，模拟一个从 1999 年运行至今、没换过布局的迷因考古站。页面底是泛蓝的冰霜纸而不是白色，墨色带着冷蓝调，主英雄色是 iMac Bondi 蓝。三种互相冲突的字体（像素显示、衬线正文、系统 sans）是有意为之——不要统一它们。所有窗口和卡片是直角、1px 墨色边框、无模糊硬偏移阴影、Win98 斜面高光。7/10 的诡异度：看得出来哪里不对，但永远可读。

## Palette

只有浅色模式。v2 把底色从暖黄 sodium 翻到了冷蓝 frost，暖色降级为点缀。

```ts
export const coreLight: Palette = {
  id: 'core-light',
  mode: 'light',
  bg: '#eaf4f8',          // --paper → --frost-100        (tokens/colors.css:39,86)
  surface: '#f5fafd',     // --surface-card → --frost-50   (tokens/colors.css:37,113)
  surfaceAlt: '#dde4ec',  // --surface-sunk → --chrome-100 (tokens/colors.css:27,114)
  ink: '#0c1a26',         // --ink                         (tokens/colors.css:90)
  inkMuted: '#4a5e72',    // --ink-muted                   (tokens/colors.css:92)
  inkFaint: '#7a8c9e',    // --ink-faint                   (tokens/colors.css:93)
  line: '#0c1a26',        // --line → var(--ink)            (tokens/colors.css:122)
  lineStrong: '#0c1a26',  // 同上——这套系统所有边框都是 ink 色，没有更强一级
  accent: '#009de0',      // --bondi-500（iMac 蓝）        (tokens/colors.css:19)
  accentInk: '#ffffff',   // --titlebar-fg                  (tokens/colors.css:119)
  accentSoft: '#bce8f6',  // --surface-pool → --bondi-100   (tokens/colors.css:16,115)
  positive: '#356f87',    // 无对应——这是决定不是测量：取 --tile-600 作安全绿替代，因为系统无语义正面色，tile 蓝绿最接近"正常/安全"的意味 (tokens/colors.css:51)
  negative: '#ff7eb6',    // --text-warn → --bubblegum-500  (tokens/colors.css:60,109)——系统唯一的警示语义色
  ramp: [                 // 这是决定不是测量：系统无数据标记规范，从 chrome 明度梯度取四阶中性灰
    '#c8d2dd',            // --chrome-200                   (tokens/colors.css:28)
    '#97a4b3',            // --chrome-400                   (tokens/colors.css:30)
    '#6c7886',            // --chrome-600                   (tokens/colors.css:31)
    '#2d3744',            // --chrome-800                   (tokens/colors.css:32)
  ],
};
```

**注意**：`line` 和 `lineStrong` 都等于 `ink`。在这套系统里，所有分隔线都是 1px 满墨边框——这不是遗漏，这就是 Y2K 面貌。如果镜头需要更柔和的分隔，系统有 `--line-soft`（`#4a5e72`，同 `ink-muted`，`tokens/colors.css:123`），但那不是默认行为。

### 和 neutralLight / neutralDark 的关系

完全不同的东西。neutralLight 是纯灰无色倾向的中性底（bg `#FAFAFA`、accent = ink = `#0A0A0A`、分隔线 `#E4E4E7`），core 是有强烈色彩身份的冰蓝体系（bg `#eaf4f8`、accent `#009de0` Bondi 蓝、分隔线即墨色 `#0c1a26`）。不存在可复用关系——如果一个镜头用了 neutralLight 效果很好，换成 core 需要从头调色，不能微调。

## 质感 skin

**选择：brutalist**

| 属性 | brutalist 定义 | core 实际值 | 出处 |
|---|---|---|---|
| radius | 0 | `--radius-none: 0` | tokens/spacing.css:24 |
| borderWidth | 2 | `--border-w: 1px` | tokens/spacing.css:33 |
| borderTone | strong (ink) | `--line: var(--ink)` | tokens/colors.css:122 |
| shadow | null + offsetShadow 6 | `--shadow-card: 2px 2px 0 var(--ink)` | tokens/effects.css:18 |
| upperLabels | true | false（lowercase by default） | readme.md:45 |
| monoBody | true | false（Tinos 衬线正文） | readme.md 「Body: Tinos」 |

core 在形体上是 brutalist（直角零圆角、满墨边框、无模糊硬偏移阴影、Win98 斜面），但在排版声音上偏离——小写而非大写，衬线而非等宽。四个 skin 里 brutalist 是唯一能承载 0 radius + 偏移阴影的；用它时需要把 `upperLabels` 和 `monoBody` 覆盖为 `false`。

## 动效规则

这套系统**有动效 token**，定义在 `tokens/effects.css:51-61`。

### 缓动

| token | 值 | 用途 | 出处 |
|---|---|---|---|
| `--ease-step-2` | `steps(2, end)` | 抖动/卡顿 | effects.css:52 |
| `--ease-step-4` | `steps(4, end)` | GIF 循环感，**默认缓动** | effects.css:53 |
| `--ease-step-8` | `steps(8, end)` | 较细的阶梯 | effects.css:54 |
| `--ease-snap` | `cubic-bezier(0.2, 0.9, 0.3, 1)` | 弹性回弹 | effects.css:55 |
| `--ease-dream` | `cubic-bezier(0.4, 0, 0.2, 1)` | **仅限**光晕、辉光、淡入淡出 | effects.css:56 |

### 时长

| token | 值 | 出处 |
|---|---|---|
| `--dur-instant` | 60ms | effects.css:57 |
| `--dur-snap` | 120ms | effects.css:58 |
| `--dur-soft` | 500ms | effects.css:59 |
| `--dur-drift` | 2400ms | effects.css:60 |
| `--dur-marquee` | 18s | effects.css:61 |

### 明令禁止

- steps 缓动是**所有字面动画的默认**——不许用平滑缓动做位移/缩放/出入场（readme.md:98）
- 平滑缓动 `--ease-dream` **只能**用在光晕、辉光、淡入淡出（readme.md:99）
- hover 必须是 1px 偏移（表面被按入）或桃色光晕绽放——**禁止** "优雅的 200ms 颜色渐变"（readme.md:101）
- press 必须是完全内凹斜面（readme.md:102）

## 硬规则（违反了就不像它了）

- 纯 `#fff` 和 `#000` 禁用（readme.md:71）
- 禁用 emoji，Unicode 方块字符（░ ▒ ▓）和几何形状（◇ ◊ ◯）可以作为排版装饰（readme.md:54-55, 119）
- 卡片和窗口不允许圆角，按钮最多 2px 柔化（readme.md:87, spacing.css:25）
- 所有边框 1px solid ink，直角（readme.md:87）
- 阴影必须是硬偏移无模糊：`2px 2px 0`（readme.md:88）
- 禁用 `backdrop-filter` 模糊——美学是平的纸层叠纸，不是 iOS 毛玻璃（readme.md:105-106）
- 三种字体必须共存，不要统一成一种（readme.md:78, typography.css:6）
- 小写为默认，只在需要打破节奏时用句首大写（readme.md:45）
- 怪异度 7/10：看得出不对劲，但永远可读（readme.md:7）
- 32px 方格栅格（readme.md:93, spacing.css:21）
- 没有营销语言，读起来像 2003 年的个人博客 wiki（readme.md:46-47, 52）

## 不适合的镜头

- **毛玻璃/磨砂效果**：系统明确禁止 backdrop-filter blur
- **圆角卡片/圆角面板**：系统 radius 为 0，任何可见圆角都会破坏 Y2K 面貌
- **平滑缓动的位移/缩放/弹跳**：系统默认 steps 缓动，平滑运动会让画面"太正常"
- **优雅渐变色过渡**：系统禁止"200ms 颜色渐变"式 hover——要么硬切要么光晕
- **彩色数据系列**（色相编码）：ramp 是明度梯度，不允许用色相区分系列
- **霓虹辉光作为主视觉**：neon 色阶仅限 rainbow marquee 文字和 visited link 紫，不能涂大面积
- **全出血照片铺满边缘**：只允许在 hero 画面中使用，一般照片要 1px 墨框或桃色光晕
- **纯白/纯黑背景**：系统硬禁 `#fff` 和 `#000`
- **SaaS 仪表盘式整洁排版**：系统明确说"这不是 SaaS 仪表盘套件"——要么密集无间距要么大面积留白，禁止中间地带
- **3D 透视/相机飞行**：系统是平面纸层叠纸的美学，Z 轴深度与平面斜面冲突

## 出处

| 文件 | 路径 |
|---|---|
| SKILL.md | `D:\DESIGN\core Design System\SKILL.md` |
| readme.md | `D:\DESIGN\core Design System\readme.md` |
| tokens/colors.css | `D:\DESIGN\core Design System\tokens\colors.css` |
| tokens/effects.css | `D:\DESIGN\core Design System\tokens\effects.css` |
| tokens/typography.css | `D:\DESIGN\core Design System\tokens\typography.css` |
| tokens/spacing.css | `D:\DESIGN\core Design System\tokens\spacing.css` |
| palettes.ts（参考格式） | `E:\remotion\yoru-motion-system\src\themes\palettes.ts` |
| skins.ts（参考格式） | `E:\remotion\yoru-motion-system\src\themes\skins.ts` |
