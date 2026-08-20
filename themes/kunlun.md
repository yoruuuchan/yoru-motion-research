# KUNLUN 昆仑

> 军工终端、深空控制台、切角青光、全等宽大写、CRT 扫描线

| | |
|---|---|
| 目录 | `D:\DESIGN\KUNLUN Design System` |
| 明暗 | 只有深色 |
| 质感 | 最接近 brutalist，但不完全匹配——见下方分析 |
| 字体 | 显示：Orbitron / 正文：JetBrains Mono / 中文：Noto Sans SC / CRT：VT323 |

## 它是什么感觉

深空指挥中心的操作界面。近乎纯黑的底色上只有青色的信号光，像 CRT 屏幕在暗室里亮着。所有文字都是等宽字体、大写字母、宽字距——不是在和你说话，是在显示系统状态。面板的角是切削过的，不是圆弧，像铣过的金属件。没有柔软的东西，没有弹跳，每个动画都是咔哒一声到位。

## Palette

```ts
export const kunlunDark: Palette = {
  id: 'kunlun-dark',
  mode: 'dark',
  bg: '#06080d',        // --bg-base                    (tokens/colors.css:9)
  surface: '#0d1320',   // --bg-panel                   (tokens/colors.css:12)
  surfaceAlt: '#131a2a',// --bg-elevated                (tokens/colors.css:13)
  ink: '#e3eaf3',       // --neutral-100 / --text-primary (tokens/colors.css:18, :73)
  inkMuted: '#95a3b4',  // --neutral-300 / --text-secondary (tokens/colors.css:20, :74)
  inkFaint: '#6c7a8c',  // --neutral-400 / --text-tertiary  (tokens/colors.css:21, :75)
  line: '#1a2540',      // --border                     (tokens/colors.css:84)
  lineStrong: '#2a3a5c',// --border-strong              (tokens/colors.css:85)
  accent: '#00b8ff',    // --cyan-500 / --accent         (tokens/colors.css:32, :90)
  accentInk: '#04060a', // --bg-void / --text-inverse    (tokens/colors.css:7, :77) — 决定不是测量：系统没有 "accent 上的文字色" token，--text-inverse 是语义上最近的深色文字角色
  accentSoft: '#00374e',// --cyan-900                    (tokens/colors.css:36) — 决定不是测量：系统没有 "accent 淡底" token，取 cyan 色阶最深一级作为深底上的微弱青色调
  positive: '#00e891',  // --green-500 / --success       (tokens/colors.css:63, :103)
  negative: '#ff3a3a',  // --red-500 / --danger          (tokens/colors.css:58, :100)
  ramp: ['#232c3d', '#4d5a6e', '#95a3b4', '#e3eaf3'],
  // --neutral-700, --neutral-500, --neutral-300, --neutral-100
  // (tokens/colors.css:23, :22, :20, :18)
  // 深底往亮了排，低→高强调
};
```

## 质感 skin

**最接近 `brutalist`，但不是它。**

匹配项：

| 属性 | brutalist 值 | KUNLUN 实测 | 匹配 |
|---|---|---|---|
| radius | 0 | 近 0（`--radius-none: 0`，圆角仅用于头像和状态点） | 近似 ✓ |
| upperLabels | true | UPPERCASE 用于 labels / status / buttons | ✓ |
| monoBody | true | 全等宽（JetBrains Mono + Orbitron） | ✓ |
| borderWidth | 2 | 1（`--border-w: 1px`，spacing.css:39） | ✗ |
| offsetShadow | 6 | 0——签名效果是霓虹辉光而非偏移阴影 | ✗ |
| shadow | null | 有 `--shadow-sm/md/lg` 但很弱；主力是 `--glow-cyan-sm/md/lg` | ✗ |

**关键差异**：

1. **边框宽度 1px 而非 2px** — Panel: `border: 1px solid var(--border-strong)` (Surfaces.css:8)；Card: `border: 1px solid var(--border)` (Surfaces.css:84)。来源：`--border-w: 1px` (spacing.css:39)。
2. **霓虹辉光代替偏移阴影** — 品牌标志性效果是 `box-shadow` 青色辉光而非几何偏移：`--glow-cyan-sm: 0 0 8px rgba(0,184,255,0.18)` / `--glow-cyan-md: 0 0 16px rgba(0,184,255,0.45), 0 0 2px #1fc8ff` / `--glow-cyan-lg: 0 0 32px rgba(0,184,255,0.45), 0 0 8px #5fd9ff` (tokens/effects.css:15-17)。
3. **切角 clip-path，不是直角 radius 0** — Panel 用 `clip-path: var(--clip-chamfer-md)` (Surfaces.css:10)，Card 用 `--clip-chamfer-sm` (Surfaces.css:88)。切角尺寸：`--chamfer-xs: 6px` / `--chamfer-sm: 8px` / `--chamfer-md: 12px` / `--chamfer-lg: 18px` / `--chamfer-xl: 24px` (spacing.css:50-54)。四个 skin 里都没有 chamfered corners 的概念——这是 KUNLUN 独有的。

**结论**：如果必须选一个，选 brutalist（upperLabels + monoBody + 近零圆角），然后把 `borderWidth` 改为 1、`offsetShadow` 改为 0、补充辉光和切角逻辑。但更诚实的说法是：KUNLUN 需要一个第五种 skin，或在 brutalist 基础上增加 `glow` 和 `chamfer` 参数。

## 动效规则

KUNLUN 的动效 token 在 `tokens/motion.css` 里定义得很明确。

**时长**（motion.css:6-10）：

| token | 值 |
|---|---|
| `--dur-instant` | 60ms |
| `--dur-fast` | 120ms |
| `--dur-normal` | 180ms |
| `--dur-slow` | 320ms |
| `--dur-glacial` | 640ms |

**缓动**（motion.css:13-17）：

| token | 值 |
|---|---|
| `--ease-linear` | `linear` |
| `--ease-out` | `cubic-bezier(0.2, 0.7, 0.2, 1)` |
| `--ease-in` | `cubic-bezier(0.7, 0, 0.84, 0)` |
| `--ease-step` | `steps(8, end)` |
| `--ease-step-2` | `steps(2, end)` |

**默认过渡**（motion.css:19-23）：

```css
--transition-base: background var(--dur-fast) var(--ease-out),
                   color      var(--dur-fast) var(--ease-out),
                   border     var(--dur-fast) var(--ease-out),
                   box-shadow var(--dur-fast) var(--ease-out),
                   opacity    var(--dur-fast) var(--ease-out);
```

即 UI 状态变化一律 120ms + sharp ease-out。

**内置关键帧动画**（motion.css:28-81）：

| 名称 | 行为 |
|---|---|
| `kl-blink` | 50% 占空比方波闪烁（光标/状态灯） |
| `kl-pulse` | opacity 1→0.4→1 呼吸（加载状态） |
| `kl-pulse-glow` | box-shadow 在 `--glow-cyan-sm` 和 `--glow-cyan-lg` 间呼吸 |
| `kl-flicker` | 不规则 CRT 闪烁（20%/24%/55% 处 opacity 降到 0.6 + text-shadow 关闭） |
| `kl-scanline-sweep` | translateY 从 -100% 到 100vh 的扫描线 |
| `kl-typewriter` | width 从 0 到 100%（打字机效果） |
| `kl-caret` | 同 blink，用于光标 |
| `kl-marquee` | translateX 从 0 到 -50%（滚动字幕） |
| `kl-spin` | rotate 360deg |
| `kl-rise` | opacity 0 + translateY(8px) → opacity 1 + translateY(0) |

**明令禁止**：

- "sharp and stepped, not bouncy"（motion.css:1-2）
- "Avoid ease-out-back / spring physics"（motion.css:2）
- 装饰性循环动画仅限状态指示器和 HUD 装饰物，不得用于整个内容区块（README.md:84）
- `prefers-reduced-motion: reduce` 时一律杀掉所有动画（motion.css:84-89）

## 硬规则（违反了就不像它了）

- Cyan/blue 是唯一的信号色。Amber + red 只用于 warning/danger 状态，不用于强调或装饰（SKILL.md:20, README.md:33-36）
- **不准用紫色。** 不准紫色渐变、紫色高亮、紫色任何东西（SKILL.md:22, README.md:70）
- **全等宽字体。** Orbitron 显示、JetBrains Mono 正文、VT323 CRT 场景、Noto Sans SC 中文。不用比例字体、不用衬线体（SKILL.md:23, typography.css:10-14）
- **切角而非圆角。** 面板和卡片用 `clip-path` chamfer，不用 `border-radius`。圆角仅允许用于 Avatar(round) 和状态点（SKILL.md:24, README.md:50-54, spacing.css:44-47）
- UPPERCASE 用于 labels / status / buttons；正文用 sentence case（SKILL.md:25, README.md:13）
- **不用 emoji。** 只用操作员符号 `▸ ▣ ▮ ⨯ ⚠ ✓ ◰ ⌬ ⌕` 等（SKILL.md:26, README.md:19）
- 不用渐变背景（尤其不用紫色渐变）。页面底色是 flat dark，装饰靠叠加层：scanlines / grid / grain / 径向青色光晕（README.md:65-70）
- 数字必须精确、表格化、带前导零：`142.3 MW`，不写"大约 140"；`08.4 ms`，`NODE-07`（README.md:17）
- 图像是附属的——KUNLUN 的画面主要是 chrome、符号和数据。出现图像时做冷色/去饱和处理（README.md:37）

## 不适合的镜头

以下动作类型会和 KUNLUN 的系统约束冲突：

- **弹簧回弹 / ease-out-back 过冲** — 系统明令禁止 spring physics 和 ease-out-back（motion.css:2），所有动效必须 sharp/stepped
- **圆角卡片、药丸形按钮、大圆角面板** — 品牌用 chamfered clip-path 切角，radius 保留给头像和状态点（spacing.css:44-47, SKILL.md:24）
- **彩色数据系列（多色相编码）** — 数据标记只用中性明度梯度（ramp），信号色只有 cyan，不存在第二个色相用于系列区分
- **紫色任何东西** — 紫色渐变、紫色高亮、紫色背景，全部禁止（SKILL.md:22）
- **比例字体 / 衬线体排版** — 全等宽规则不可破（SKILL.md:23）
- **柔和渐变背景、暖色调底色** — 底色必须是近黑冷色调 void（colors.css:7-14），不接受浅色或暖色
- **装饰性循环动画用在内容区块上** — 循环动画只能出现在 HUD 装饰物和状态指示器上（README.md:84）
- **emoji 图标、pictographic 插图** — 只能用操作员符号和 ASCII 框线（SKILL.md:26）
- **频闪黑帧（全屏闪烁）** — 系统自带的 flicker 是 opacity 0.6 的微弱抖动（motion.css:44-52），不是全黑全亮的硬切；全屏频闪会破坏 reduced-motion 承诺
- **慢动作淡入淡出（>640ms 的渐变过渡）** — 最长时长 token 是 `--dur-glacial: 640ms`（motion.css:10），超过这个值就不像这套系统了
- **有机 / 手写 / 手绘风格** — 系统是工业 / 军工 / 终端审美，手写笔触和有机曲线格格不入

## 出处

读过的文件（全部位于 `D:\DESIGN\KUNLUN Design System`）：

- `tokens/colors.css` — 色板、语义别名
- `tokens/typography.css` — 字体族、字号阶梯、字重
- `tokens/spacing.css` — 4px 网格、chamfer 尺寸、边框宽度、圆角
- `tokens/effects.css` — 阴影、辉光、clip-path chamfer、纹理
- `tokens/motion.css` — 时长、缓动、关键帧动画
- `tokens/base.css` — 全局重置、滚动条、链接样式
- `tokens/components.css` — 组件 CSS 桶文件
- `components/surfaces/Surfaces.css` — Panel / Card 的边框、clip-path、辉光实测
- `SKILL.md` — Claude Skill 清单、品牌硬规则
- `README.md` — 设计指南全文

参考文件（`E:\remotion\yoru-motion-system\src\themes`）：

- `palettes.ts` — palette 类型形状、已有实例的注释风格
- `skins.ts` — 四种 skin 的参数定义
