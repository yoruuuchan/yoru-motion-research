# Aozora 青空

> 夏日天空、液态玻璃、清透蓝白——适合轻盈数据展示和产品介绍镜头

| | |
|---|---|
| 目录 | `D:\DESIGN\Aozora 青空 Design System` |
| 明暗 | 只有浅色 |
| 质感 | glass |
| 字体 | Inter (显示/正文) · PingFang SC / 思源黑体 (中文) · Bebas Neue (海报) |

## 它是什么感觉

宝矿力广告里那种蓝天白云的清凉感。所有面板都是毛玻璃，浮在天空渐变上面，阳光从顶部打下来、在边缘留一道白色高光。颜色只有天蓝和纯白，偶尔一笔太阳黄。版式是海报语法——超大标题配极小标注，中间几乎没有过渡字号。整体情绪是"夏天的午后，拿着冰汽水看数据"。

## Palette

```ts
export const aozoraLight: Palette = {
  id: 'aozora-light',
  mode: 'light',
  bg: '#F7FAFD',        // --neutral-50 (colors.css:30) ⚠️ 这是决定不是测量：--surface-page 是 #FFFFFF，但系统说页面底"几乎从不用纯色"而是天空渐变；#F7FAFD 是中性色阶里最浅的带蓝偏色值，用来近似"天光纸"的感觉
  surface: '#FFFFFF',    // --neutral-0 = --surface-elevated (colors.css:29, semantic.css:28)
  surfaceAlt: '#EEF3F8', // --neutral-100 (colors.css:31)
  ink: '#232C36',        // --neutral-700 = --text-body (colors.css:37, semantic.css:17)
  inkMuted: '#5C6B7C',   // --neutral-500 = --text-muted (colors.css:35, semantic.css:18)
  inkFaint: '#8A9AAB',   // --neutral-400 = --text-faint (colors.css:34, semantic.css:19)
  line: '#DCE5EF',       // --neutral-200 (colors.css:32) ⚠️ 这是决定不是测量：系统用 rgba(10,68,140,0.08) 做 hairline (semantic.css:41)，hex 近似约 #EBF0F6，取 neutral-200 以获得可见的分隔效果
  lineStrong: '#232C36', // = ink，同 --text-body (colors.css:37)
  accent: '#0A84FF',     // --blue-500 = --brand (colors.css:12, semantic.css:7)
  accentInk: '#FFFFFF',  // --neutral-0 = --text-on-brand (colors.css:29, semantic.css:20)
  accentSoft: '#CFE8FF', // --blue-100 = --brand-soft (colors.css:8, semantic.css:11)
  positive: '#34C759',   // --success-500 (colors.css:51)
  negative: '#FF453A',   // --danger-500 (colors.css:53)
  ramp: [
    '#BCC9D6',           // --neutral-300 (colors.css:33)
    '#8A9AAB',           // --neutral-400 (colors.css:34)
    '#5C6B7C',           // --neutral-500 (colors.css:35)
    '#232C36',           // --neutral-700 (colors.css:37)
  ],
};
```

## 质感 skin

选 **glass**。理由：

| 参数 | glass skin 值 | Aozora 实际值 | 来源 |
|---|---|---|---|
| 圆角 (大) | 18 | 20 (`--radius-lg`, radius.css:11) | 接近，不需要改 |
| 圆角 (小) | 10 | 14 (`--radius-md`, radius.css:10) | 差 4px，可接受 |
| 边框宽度 | 0 | 0 — 实际用 glass stroke 而非实线 (glass.css:51) | 完全匹配 |
| 阴影 | `0 24px 64px rgba(0,0,0,0.12)` | `0 6px 18px rgba(10,68,140,0.12)` (`--shadow-md`, shadow.css:9) | 扩散值不同但都是大柔影；skin 的黑色阴影与系统的蓝调阴影有色偏差，不影响结构匹配 |
| 大写标签 | false | false — Title Case + Sentence case (readme.md "Casing") | 匹配 |
| 等宽正文 | false | false — Inter 为主体 (typography.css) | 匹配 |

如果需要更精确：把 `radius` 从 18 调到 20，`radiusSmall` 从 10 调到 14。

## 动效规则

系统**有**动效 token，全部来自 `tokens/motion.css`：

**时长**

| token | 值 | 用途 | 出处 |
|---|---|---|---|
| `--dur-instant` | 80ms | 按压反馈 | motion.css:7 |
| `--dur-fast` | 140ms | hover、轻触 | motion.css:8 |
| `--dur-base` | 240ms | 通用过渡 | motion.css:9 |
| `--dur-slow` | 420ms | 页面/模态/玻璃折射 | motion.css:10 |
| `--dur-slower` | 640ms | 大型编排 | motion.css:11 |

**缓动**

| token | 值 | 出处 |
|---|---|---|
| `--ease-out-quart` | `cubic-bezier(0.25, 1, 0.5, 1)` | motion.css:14 |
| `--ease-out-expo` | `cubic-bezier(0.16, 1, 0.3, 1)` | motion.css:15 |
| `--ease-in-out` | `cubic-bezier(0.65, 0, 0.35, 1)` | motion.css:16 |
| `--ease-spring` | `cubic-bezier(0.34, 1.56, 0.64, 1)` | motion.css:17 |
| `--ease-bounce` | `cubic-bezier(0.68, -0.6, 0.32, 1.6)` | motion.css:18 |

**组合**

| token | 值 | 出处 |
|---|---|---|
| `--transition-hover` | `all 140ms ease-out-quart` | motion.css:21 |
| `--transition-press` | `transform 80ms ease-out-quart` | motion.css:22 |
| `--transition-glass` | `backdrop-filter + background 420ms ease-out-expo` | motion.css:23-24 |

**明令禁止**
- 不用 fade-to-black，穿越白色做交叉淡化（readme.md "Animation"）
- 不用无限装饰循环（readme.md "Animation"）
- 不用线性插值——所有曲线都是 spring / expo / quart（motion.css 注释 line 1-2）

## 硬规则（违反了就不像它了）

- 玻璃面板**必须**放在有颜色的背景上；纯白底上玻璃会消失（readme.md "Glass"）
- 阴影必须带蓝调 `rgba(10,68,140,…)`，不用纯黑（shadow.css 注释 line 1-2, readme.md "Shadows"）
- 产品界面内禁止 emoji，用品牌图标或 Unicode 符号代替（readme.md "No emoji", SKILL.md）
- 标题 ≤ 5 个词，正文 ≤ 2 句/段（readme.md "Content fundamentals"）
- 直角 90° 仅限海报版式的编辑块，UI 元素一律圆角（radius.css 注释 line 1-4, readme.md "Corners"）
- 不用真实照片，只用抽象 3D 玻璃/液态/水滴插画（readme.md "Imagery"）
- 不用纹理、噪点、摄影背景——背景必须是天空渐变或产品渐变（readme.md "Backgrounds"）
- 穿越白色，不穿越黑色（readme.md "Animation"）

## 不适合的镜头

- **淡入/淡出黑场** — 系统明确要求穿越白色交叉淡化，黑场过渡会破坏天空感
- **线性匀速运动** — 所有曲线都是弹簧/指数/四次方出，线性运动会显得机械、不像液态
- **无限循环装饰动画** — 系统明令禁止
- **直角硬切 + 偏移阴影**（brutalist 类镜头）— 与圆角玻璃语言完全冲突
- **暗色调/夜景氛围** — 系统只有浅色模式，整体情绪是夏日正午
- **真实摄影素材叠加** — 系统只接受抽象 3D 玻璃/液态图形
- **多色相数据系列**（彩虹条、分色散点）— ramp 规则要求用明度梯度，不用色相编码
- **频闪黑帧 / 故障效果** — 与"calm, springy, water-like"的动效性格完全相反
- **厚重投影（纯黑阴影）** — 阴影必须蓝调，纯黑阴影破坏天空场景的统一感

## 出处

| 文件 | 路径 |
|---|---|
| 设计系统说明 | `D:\DESIGN\Aozora 青空 Design System\readme.md` |
| Agent Skill | `D:\DESIGN\Aozora 青空 Design System\SKILL.md` |
| 色彩 token | `D:\DESIGN\Aozora 青空 Design System\tokens\colors.css` |
| 语义别名 | `D:\DESIGN\Aozora 青空 Design System\tokens\semantic.css` |
| 动效 token | `D:\DESIGN\Aozora 青空 Design System\tokens\motion.css` |
| 圆角 token | `D:\DESIGN\Aozora 青空 Design System\tokens\radius.css` |
| 阴影 token | `D:\DESIGN\Aozora 青空 Design System\tokens\shadow.css` |
| 玻璃 token | `D:\DESIGN\Aozora 青空 Design System\tokens\glass.css` |
| 系统清单 | `D:\DESIGN\Aozora 青空 Design System\_ds_manifest.json` |
| palette 参考 | `E:\remotion\yoru-motion-system\src\themes\palettes.ts` |
| skin 参考 | `E:\remotion\yoru-motion-system\src\themes\skins.ts` |
