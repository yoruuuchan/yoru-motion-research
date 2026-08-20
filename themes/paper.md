# PAPER

> 暖纸底+锈红墨迹+零圆角 -- 摄影集、访谈长文、个人作品集的编辑系统，editorial / analog / dark 三种声调

| | |
|---|---|
| 目录 | `D:\DESIGN\PAPER Design System` |
| 明暗 | 双套浅色（editorial + analog）+ film-base 暗板 |
| 质感 | hairline（需 radius -> 0） |
| 字体 | EB Garamond (显示+正文) / IBM Plex Sans (标签/UI) / Noto Serif SC (中文) |

## 它是什么感觉

一本摊在桌上的独立摄影杂志。所有东西放在暖奶白纸面上——ink 是温暖的炭灰而不是纯黑，唯一的色彩是印章般的锈红，在一页里最多出现两次。排版完全靠文字层级和留白做分隔，几乎没有卡片；圆角是零。切到 analog 模式，纸面变得更黄、照片多一层棕褐调、偶尔歪 0.55 度模拟暗房冲洗的不精确。dark 不是常规深色主题，而是底片基——接触印样、胶片条、全出血暗图。

## Palette

### Editorial（默认浅色）

```ts
export const paperEditorial: Palette = {
  id: 'paper-editorial',
  mode: 'light',
  bg: '#F4F1EA',        // --paper-200 = --surface-page (colors.css:5, colors.css:30)
  surface: '#FCFBF8',   // --paper-100 = --surface-raised (colors.css:4, colors.css:31)
  surfaceAlt: '#EDE6D7', // --paper-300 = --surface-sunken (colors.css:6, colors.css:32)
  ink: '#26241E',        // --ink-800 = --text-body (colors.css:12, colors.css:39)
  inkMuted: '#847D6E',   // --ink-400 = --text-muted (colors.css:14, colors.css:41)
  inkFaint: '#B3AB9A',   // --ink-200 = --text-faint (colors.css:15, colors.css:42)
  line: '#D6CFBF',       // --ink-100 = --rule-hair (colors.css:16, colors.css:48)
  lineStrong: '#26241E', // --ink-800 = --rule-strong (colors.css:12, colors.css:50)
  accent: '#B8543A',     // --rust-500, 系统唯一强调色 (colors.css:25)
  accentInk: '#FCFBF8',  // --paper-100 (colors.css:4) | 这是决定不是测量：系统不定义 accent 上的文字色；取最浅纸色，在 rust-500 上对比度约 6:1
  accentSoft: '#F1DCD2', // --rust-100 (colors.css:27)
  positive: '#536D46',   // 这是决定不是测量：系统无 positive/success 语义色（只有 paper/ink/slate/rust 四族，readme "no other hues"）；取暖调橄榄绿 HSL(100,22%,35%)，与纸面暖底色同温区
  negative: '#8E3A24',   // --rust-700 (colors.css:24) | 这是决定不是测量：系统无独立 negative hue，此值是 rust 族已有 token；比 accent 暗两级可区分语义，但同色相——accent 和 negative 同时出现时需消费方覆盖
  ramp: ['#B3AB9A', '#847D6E', '#4E4941', '#26241E'],
    // ink-200 -> ink-400 -> ink-600 -> ink-800 (colors.css:15,14,13,12)
};
```

### Analog（暖浅色）

```ts
export const paperAnalog: Palette = {
  id: 'paper-analog',
  mode: 'light',
  bg: '#EDE6D7',        // --paper-300 = analog --surface-page (colors.css:6, modes.css:20)
  surface: '#FBF7EC',   // analog --surface-raised (modes.css:21, 硬编码值)
  surfaceAlt: '#E3D9C5', // --paper-400 = analog --surface-sunken (colors.css:7, modes.css:22)
  ink: '#26241E',        // --ink-800 = --text-body, analog 无覆盖 (colors.css:12)
  inkMuted: '#8B8168',   // analog --text-muted (modes.css:31, 硬编码值)
  inkFaint: '#B0A48A',   // analog --text-faint (modes.css:32, 硬编码值)
  line: '#D8CDB6',       // analog --rule-hair (modes.css:26, 硬编码值)
  lineStrong: '#26241E', // --ink-800 = --rule-strong, analog 无覆盖 (colors.css:12, colors.css:50)
  accent: '#B8543A',     // --rust-500 (colors.css:25)
  accentInk: '#FCFBF8',  // 同 editorial: 决定不是测量
  accentSoft: '#F1DCD2', // --rust-100 (colors.css:27)
  positive: '#536D46',   // 同 editorial: 决定不是测量
  negative: '#8E3A24',   // --rust-700 (colors.css:24) | 同 editorial: 决定不是测量
  ramp: ['#B3AB9A', '#847D6E', '#4E4941', '#26241E'],
    // 与 editorial 相同: ink 色阶不随 mode 变化 (colors.css:15,14,13,12)
};
```

### Dark（film-base 暗板）

readme 说 "It is a surface, not a theme"——用于接触印样、胶片条、全出血暗图段落，不是全站深色模式。tokens 覆盖较少，缺失的角色需要推导。

```ts
export const paperDark: Palette = {
  id: 'paper-dark',
  mode: 'dark',
  bg: '#15140F',        // --ink-900 = --surface-dark (colors.css:11, colors.css:34, modes.css:41)
  surface: '#1B1A16',   // 这是决定不是测量: dark 不覆盖 --surface-raised; 取 --film-base (colors.css:62), 系统中 "暗底上的介质" 最近的值
  surfaceAlt: '#26241E', // 这是决定不是测量: dark 不覆盖 --surface-sunken; 取 --ink-800 (colors.css:12), ink 色阶的下一级
  ink: '#E7E2D6',        // --text-on-dark (colors.css:44, modes.css:42)
  inkMuted: '#9A937F',   // --text-on-dark-muted (colors.css:45, modes.css:44)
  inkFaint: '#6E6857',   // modes.css:45 硬编码
  line: '#37352F',       // 这是决定不是测量: modes.css:46 原值 rgba(231,226,214,.16), 此为在 bg #15140F 上的合成近似 hex
  lineStrong: '#7E7B73', // 这是决定不是测量: modes.css:47 原值 rgba(231,226,214,.5), 此为在 bg #15140F 上的合成近似 hex
  accent: '#B8543A',     // --rust-500, 不随 mode 变化 (colors.css:25)
  accentInk: '#FCFBF8',  // 同 editorial: 决定不是测量
  accentSoft: '#3F1D14', // 这是决定不是测量: 系统无 "暗底 accent 淡底" token; 取 rust hue HSL(13,25%,16%), 与 yoruDark accentSoft 同明度层
  positive: '#83A970',   // 这是决定不是测量: editorial positive (#536D46) 的亮版, HSL(100,25%,55%), 暗底上可读
  negative: '#D9917A',   // --rust-300 (colors.css:26) | 这是决定不是测量: 系统无 negative token; 取 rust 族浅色, 暗底可读且与 accent 可区分
  ramp: ['#4E4941', '#847D6E', '#B3AB9A', '#E7E2D6'],
    // 暗底往浅排: ink-600 -> ink-400 -> ink-200 -> text-on-dark (colors.css:13,14,15,44)
};
```

### 和 yoru-motion-system 里的 `warmPaper` 什么关系

`warmPaper` 是从小二相机网站截图量出来的（palettes.ts:97-100 注释），不是从 PAPER Design System 提取的。两套在 "暖纸底+红系强调色" 这个大方向上重合——这个组合在摄影/印刷领域很常见——但具体色值不同：

| 角色 | warmPaper | paperEditorial | 差异 |
|---|---|---|---|
| bg | #EBE1D6 | #F4F1EA | warmPaper 深约 3 级、更黄橙 |
| accent | #C03C24 | #B8543A | warmPaper 偏正红 (hue 约 8 度), PAPER 偏橙锈 (hue 约 13 度) |
| ink | #2E261D | #26241E | 相近但 warmPaper 偏暖褐 |
| surface | #FCF8F4 | #FCFBF8 | 极接近 |

warmPaper 的 bg 更接近 paperAnalog 的 bg (#EDE6D7)，但仍有可见差异。**两者不可互换。** warmPaper 承载的是某个特定摄影师网站的实测色温，PAPER 系列是设计系统的规定色值。混用会在色温和强调色上产生可见差异。

## 质感 skin

选 **hairline**，需将 radius 改为 0。

| 参数 | hairline skin 值 | PAPER 实际值 | 来源 | 匹配 |
|---|---|---|---|---|
| 大圆角 | 14 | 0 | `--radius-0:0` (space.css:21) | 需改 -> 0 |
| 小圆角 | 8 | 0 | 同上 | 需改 -> 0 |
| 边框宽度 | 1 | 1px | `--border-hair:1px` (space.css:25) | 完全匹配 |
| 边框色调 | `line` | `--rule-hair = --ink-100` | colors.css:48 | 匹配: hairline 的 line tone = palette.line |
| 阴影 | `0 1px 2px rgba(0,0,0,.04), 0 8px 24px rgba(0,0,0,.06)` | editorial: `--shadow-none` (modes.css:11); analog: `--shadow-print` = `0 1px 2px rgba(38,36,30,.11), 0 12px 26px -16px rgba(38,36,30,.42)` (material.css:14) | material.css:12-14, modes.css:11,25 | 结构相似; editorial 无阴影, analog 的 print shadow 与 hairline 同形态但更沉 |
| 偏移阴影 | 0 | 0 | readme.md:99 "printing, not elevation" | 完全匹配 |
| 大写标签 | false | false | readme.md:59 "Sentence case everywhere except labels" | 完全匹配 |
| 等宽正文 | false | false | typography.css:5 body = EB Garamond | 完全匹配 |

brutalist 在 radius 上精确匹配 (0) 但 offsetShadow=6、upperLabels=true、monoBody=true 全错（PAPER 阴影是写实印刷阴影而非几何偏移，标题 sentence case，正文 serif）。hairline 只需改两个 radius 值，其余 5 项精确或接近匹配。

## 动效规则

系统**有**动效 token。

**注意**: 目录里有 `tokens/motion.css`，但 `styles.css` 没有 @import 它。实际生效的动效 token 在 `tokens/space.css`（被 styles.css 导入）。两份文件的缓动和时长数值不同；readme.md 的描述与 space.css 一致。以下全部从 space.css 摘录。

**时长**

| token | 值 | 出处 |
|---|---|---|
| `--dur-1` | 120ms | space.css:32 |
| `--dur-2` | 220ms | space.css:33 |
| `--dur-3` | 420ms | space.css:34 |
| `--dur-4` | 800ms | space.css:35 |

**缓动**

| token | 值 | 出处 |
|---|---|---|
| `--ease-paper` | `cubic-bezier(.2,.6,.2,1)` | space.css:30 |
| `--ease-out` | `cubic-bezier(.16,1,.3,1)` | space.css:31 |

**明令禁止**

- 只有 color 和 border-color 可以 transition，不动 transform、不动 opacity（readme.md:103, base.css:24）
- 没有入场动画（readme.md:103）
- 没有视差，没有滚动效果（readme.md:103）
- hover 只变色（ink -> rust），不位移、不缩放、不淡入（readme.md:105）
- press 只加深一级色阶（ink-800 -> ink-900 或 rust-500 -> rust-700），不缩放（readme.md:105）
- prefers-reduced-motion 时全部归零到 0.01ms（base.css:37）

## 硬规则（违反了就不像它了）

- **圆角为零。** 2px 仅限胶带和印章元素，999px 仅限模式切换圆盘。（space.css:21-23, readme.md:95）
- **只有一个强调色。** 锈红 `--rust-500` 在一页内最多出现两次：图号、日期戳、链接 hover、偶尔的章节号。（readme.md:85, SKILL.md:23）
- **"结构先于质感"。** 每个跨页最多一两个 analog 材质细节。如果你能在读内容之前就叫出那个质感的名字，该把它调低。（readme.md:31, SKILL.md:22）
- **照片方角 + 1px 内嵌边框。** 所有照片经 `--frame-edge: rgba(38,36,30,.14)` 嵌线和统一色调滤镜。（readme.md:93, colors.css:51）
- **正文缩进不空行。** 首段之后的段落用 `text-indent:1.5em`，不用 margin-top。（readme.md:87, base.css:16）
- **不用 emoji，不用图标字体。** 导航用 Unicode 字符（箭头、段落符号、罗马数字），需要图标时用 Lucide 1.5px 描边标注为外来元素。（readme.md:124）
- **不用渐变背景。** 渐变只出现在摄影占位色和扫描边缘唇。（readme.md:91）
- **标题 sentence case。** 大写仅限元数据标签（WORDS, PHOTOGRAPHS, PUBLISHED）和 wordmark。（readme.md:59）
- **中文并行不翻译每一句**——每节一句中文，小一号，行高 1.9，不用斜体。（readme.md:76-77）
- **标题不超过 8 个词**以保证显示尺寸够大。（readme.md:60）

## 不适合的镜头

- **弹跳/回弹缓动**（spring / bounce / elastic）-- "Paper does not bounce"（readme.md:103, space.css:29 注释）
- **入场动画 / 元素飞入** -- 系统明确无入场动画（readme.md:103）
- **视差滚动 / 滚动驱动动效** -- 系统明确禁止（readme.md:103）
- **缩放变换**（scale up / down / pulse）-- "Nothing scales"（readme.md:105）
- **透明度渐变作装饰** -- hover/press 只变色不变透明度（readme.md:105）
- **渐变背景 / 霓虹辉光** -- 系统无渐变（readme.md:91），唯一色相是暖中性 + 锈红
- **彩色数据系列**（彩虹条、分色散点）-- ramp 规则要求明度梯度不用色相
- **频闪黑帧 / 故障效果** -- 与安静编辑质感完全对立
- **3D 相机飞行 / 透视翻转** -- 2D 编辑系统，无深度；唯一的倾斜是 analog 模式的 -0.55 度微斜（modes.css:28）
- **毛玻璃叠加**（backdrop-filter 做内容遮罩）-- 透明模糊只允许出现在吸顶导航条，不用于内容层（readme.md:101）
- **偏移阴影**（brutalist 风格几何硬影）-- 阴影是写实印刷阴影 rgba(38,36,30,...)，从不做几何偏移（material.css:13-16）
- **纯黑阴影** -- 阴影始终带暖调 rgba(38,36,30,...)，不用纯 rgba(0,0,0,...)（material.css:13-16）

## 出处

| 文件 | 路径 |
|---|---|
| 设计系统说明 | `D:\DESIGN\PAPER Design System\readme.md` |
| Agent Skill | `D:\DESIGN\PAPER Design System\SKILL.md` |
| 入口样式表 | `D:\DESIGN\PAPER Design System\styles.css` |
| 色彩 token（生效） | `D:\DESIGN\PAPER Design System\tokens\colors.css` |
| 色彩 token（未导入，旧版） | `D:\DESIGN\PAPER Design System\tokens\color.css` |
| 排版 token | `D:\DESIGN\PAPER Design System\tokens\typography.css` |
| 间距 / 栅格 / 动效 token | `D:\DESIGN\PAPER Design System\tokens\space.css` |
| 材质 token | `D:\DESIGN\PAPER Design System\tokens\material.css` |
| 模式切换 | `D:\DESIGN\PAPER Design System\tokens\modes.css` |
| 元素默认 | `D:\DESIGN\PAPER Design System\tokens\base.css` |
| 动效 token（未导入，旧版） | `D:\DESIGN\PAPER Design System\tokens\motion.css` |
| palette 参考 | `E:\remotion\yoru-motion-system\src\themes\palettes.ts` |
| skin 参考 | `E:\remotion\yoru-motion-system\src\themes\skins.ts` |
