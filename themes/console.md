# yoru-and-akari Console

> 软质感 AI 伴侣控制台，冷瓷白/午夜靛蓝双主题，柔影新拟态，状态密度高

| | |
|---|---|
| 目录 | `D:\DESIGN\yoru-and-akari Console Design System2` |
| 明暗 | 双套（akari 浅色 / yoru 深色） |
| 质感 | glass |
| 字体 | Geist / Geist / Zen Kaku Gothic New |

## 它是什么感觉

一个你每天打开很多次的东西。冷瓷白底上漂着柔软的双向阴影，卡片靠影子浮出来而不是靠线框——看第一眼会觉得它是个原生 app 而不是网页。设置行密密地排列着 model、temperature、proactive toggle，每行 44px 触控高度配 13px 紧凑字号，密而不挤。消息气泡也是新拟态的，用户侧是实心皇家蓝，companion 侧是浮在底色上的柔影灰。整个色调始终在一族蓝色里——从 akari 的沉稳皇家蓝到 yoru 的提亮靛蓝。暗色模式深到接近纯黑（#0B1020），饱和度故意降低，两点钟看不刺眼。

## Palette

### akari（浅色）

```ts
export const consoleAkari: Palette = {
  id: 'console-akari',
  mode: 'light',
  bg: '#E8ECF3',        // --bg-base                    colors_and_type.css:95
  surface: '#EFF2F8',    // --bg-surface                 colors_and_type.css:96
  surfaceAlt: '#DEE3EC', // --bg-sunken                  colors_and_type.css:98
  // 决定，不是测量：系统将 bg-sunken 定义为「凹陷输入底色」，这里取其
  // 「比 surface 暗一阶的次级表面」视觉角色，用于交替行和次级面板。
  // 系统无专门的 zebra/alt-surface token。
  ink: '#0E1525',        // --ink-1                      colors_and_type.css:108
  inkMuted: '#6B7793',   // --ink-3                      colors_and_type.css:110
  // 决定，不是测量：系统有四级墨色（ink-1→ink-4），Palette 只有三个槽。
  // 跳过 ink-2 (#394560, 系统的 body 正文色)，将 ink-3（caption/tertiary）
  // 映射到 inkMuted，因为在数据图表里 inkMuted 的角色是轴标签而非正文。
  inkFaint: '#A1ABBF',   // --ink-4                      colors_and_type.css:111
  line: '#D9DCE3',       // colors_and_type.css:116 + :96
  // 决定，不是测量：--line-2 rgba(14,21,37, 0.10) 合成在 --bg-surface
  // #EFF2F8 上的不透明等效值。系统用半透明 hairline，Palette 需要实色。
  lineStrong: '#0E1525', // colors_and_type.css:108
  // 决定，不是测量：取 --ink-1 作为最强边框，沿用其他 palette 的
  // lineStrong = ink 惯例。系统自身的 --line-strong 是 rgba(14,21,37,0.18)
  // 即 18% 不透明度，太浅做不了「强边框」。
  accent: '#4F6CE8',     // --primary-500                colors_and_type.css:125
  accentInk: '#FFFFFF',  // --ink-on-primary             colors_and_type.css:112
  accentSoft: '#DCE3FE', // --primary-100                colors_and_type.css:121
  positive: '#2BA672',   // --success-500                colors_and_type.css:145
  negative: '#D45D5D',   // --error-500                  colors_and_type.css:153
  ramp: ['#A1ABBF', '#6B7793', '#394560', '#0E1525'],
  // 决定，不是测量：系统无数据梯度 token。取 ink-4 → ink-3 → ink-2 → ink-1
  // 作为浅底上从低到高强调的明度梯度。
  // ink-4 :111 → ink-3 :110 → ink-2 :109 → ink-1 :108
};
```

### yoru（深色）

```ts
export const consoleYoru: Palette = {
  id: 'console-yoru',
  mode: 'dark',
  bg: '#0B1020',         // --bg-base                    colors_and_type.css:185
  surface: '#131A2E',    // --bg-surface                 colors_and_type.css:186
  surfaceAlt: '#1B2340', // --bg-elevated                colors_and_type.css:187
  // 决定，不是测量：系统将 bg-elevated 定义为「tooltip/popover 底色」，
  // 这里取其「比 surface 亮一阶」的结构角色。暗色主题的 surfaceAlt 需要
  // 比 surface 更亮（与浅色主题相反），bg-elevated 是系统中最近的一阶。
  ink: '#E6EAF6',        // --ink-1                      colors_and_type.css:196
  inkMuted: '#6B7691',   // --ink-3                      colors_and_type.css:198
  inkFaint: '#434D67',   // --ink-4                      colors_and_type.css:199
  line: '#2B3143',       // colors_and_type.css:203 + :186
  // 决定，不是测量：--line-2 rgba(255,255,255, 0.10) 合成在 --bg-surface
  // #131A2E 上的不透明等效值。
  lineStrong: '#E6EAF6', // colors_and_type.css:196
  // 决定，不是测量：取 --ink-1 作为最强边框，与浅色版同理。
  accent: '#7A95FA',     // --primary-500                colors_and_type.css:211
  accentInk: '#0B1020',  // --ink-on-primary             colors_and_type.css:200
  accentSoft: '#1F2A55', // --primary-100                colors_and_type.css:207
  positive: '#3FCB94',   // --success-500                colors_and_type.css:228
  negative: '#F08484',   // --error-500                  colors_and_type.css:236
  ramp: ['#434D67', '#6B7691', '#A8B2CC', '#E6EAF6'],
  // 决定，不是测量：暗底上从低到高强调 = 从暗到亮。
  // ink-4 :199 → ink-3 :198 → ink-2 :197 → ink-1 :196
};
```

## 质感 skin

选 **glass**。

证据：

- **圆角**：系统卡片 `--radius-lg = 16px`（colors_and_type.css:72），glass skin radius = 18。差 2px，是四个 skin 里最接近的（hairline 14，flat 8，brutalist 0）。
- **边框**：系统明确规定「卡片由阴影定义，绝不用 1px 描边」（README.md:131）。glass 的 `borderWidth = 0` 完全吻合。hairline 的 `borderWidth = 1` 直接违反。
- **阴影**：系统核心是新拟态双向阴影 `--shadow-raised: -4px -4px 12px highlight, 4px 4px 14px shadow`（colors_and_type.css:167），glass 的单向落影形状不同，但「无边框 + 大柔影」的整体气质是四个里最近的。flat 和 brutalist 完全没有阴影。
- **大写**：系统全局小写（SKILL.md:23），glass 的 `upperLabels = false`。brutalist 强制大写，不合格。
- **等宽正文**：系统正文用 Geist sans-serif，mono 只用于日志和数字（README.md:107），glass 的 `monoBody = false`。brutalist 强制等宽正文，不合格。

不完美之处：glass 的 radius 应从 18 调到 16 以匹配系统，shadow 应替换为系统的双向新拟态公式。如果未来 skin 支持自定义 shadow 形状，Console 值得一个专属变体。

## 动效规则

系统**有动效 token**，直接引用：

| token | 值 | 用途 | 出处 |
|---|---|---|---|
| `--dur-fast` | 140ms | toggle、press state、hover | colors_and_type.css:84 |
| `--dur-base` | 220ms | toggle 滑块、drawer 展开、tab 切换 | colors_and_type.css:85 |
| `--dur-slow` | 420ms | sheet 进场、focus halo 展开 | colors_and_type.css:86 |
| `--ease-out` | `cubic-bezier(0.22, 1, 0.36, 1)` | 入场动效 | colors_and_type.css:81 |
| `--ease-in-out` | `cubic-bezier(0.65, 0, 0.35, 1)` | 通用 | colors_and_type.css:82 |
| `--ease-spring` | `cubic-bezier(0.34, 1.4, 0.42, 1)` | **仅限**两处（见下） | colors_and_type.css:83 |

语义约束（README.md:148-157）：

- 默认安静，不弹跳（"Calm, no bounces by default"）
- `--ease-spring` **仅限**主动消息「now」指示器和灯泡头像呼吸脉冲两处使用
- 内容不能从无中淡入——必须滑动 4-8px 或从 `scale(0.97)` 起步
- 禁止旋转加载器；用 3 点打字指示器或 7px 主色脉冲点

## 硬规则（违反了就不像它了）

- UI 文字全部小写。ALL CAPS 仅限 eyebrow 标签（`letter-spacing: 0.08em`）。（SKILL.md:23，README.md:63-64）
- 对操作者说「你/you」，companion 内部用「我/I」，永远不用「我们/we」或「the assistant」。（README.md:66-74）
- UI chrome 里没有 emoji。没有 🌙 没有 ✨ 没有 💬。用 Lucide 图标或状态圆点。（SKILL.md:25，README.md:87）
- 日志默认折叠。只在有错误时才出现红色 error dot。（SKILL.md:26，README.md:169）
- 时间轴是真正的竖线轨道（垂直线 + 点状事件），不是堆叠卡片。（SKILL.md:27，README.md:170-171）
- 输入框用 inset shadow；选中项用 1.5px primary 描边（不是染色底色）。（SKILL.md:28）
- 卡片由阴影定义，绝不用 1px 描边或彩色左边框条。（SKILL.md:29，README.md:131）
- 24 小时制；canonical model id（`claude-sonnet-4-5` 不是营销名）；token 数用细分隔符。（SKILL.md:30，README.md:83）
- 视觉丰富度来自 shadow + glass，不来自装饰性渐变、插画或满幅摄影。（README.md:114）
- Glass 只出现在背后有内容透出的地方，永远不在平面上做纯装饰。（README.md:128）

## 不适合的镜头

- **弹簧回弹 / 弹性过冲**——系统明确限制 `ease-spring` 仅用于 2 个特定位置，默认「安静无弹跳」（README.md:149,155）
- **旋转 / 自旋过渡**——「永远不要旋转加载器」（README.md:157），旋转动作与整体静谧语气冲突
- **纸质翻页 / 拟物翻转**——这是瓷器 + 玻璃质感，不是纸
- **霓虹辉光 / 光轨拖尾**——系统禁止装饰性渐变（README.md:114），glow 仅限 ember 小点
- **3D 相机飞行 / 透视旋转**——平面新拟态表面不适合 3D 变换，双向阴影在透视下会穿帮
- **粒子爆炸 / 五彩纸屑**——与「calm, no bounces」基调直接冲突
- **逐字打字机揭示**——系统要求内容用滑动 4-8px 或 `scale(0.97)` 入场，不做逐字符动画（README.md:157）
- **故障 / 失真 / 色差效果**——与冷静、自信的控制台美学矛盾
- **硬切零时长跳转**——系统最短时长 `--dur-fast = 140ms`，不存在 0ms 的设计意图

## 出处

### 读过的文件

- `colors_and_type.css` — 全部 token（双主题色板、字体栈、间距、圆角、阴影、动效）
- `styles.css` — 仅一行 `@import`，无额外 token
- `SKILL.md` — agent 技能清单，含硬规则摘要
- `README.md` — 完整设计基础文档（品牌概念、内容基调、视觉基础、行为清单）
- `_ds_manifest.json` — 机器可读 token 清单，确认了所有 token 的 kind 和 scope
- `briefs/cc-multi-device-and-ios26.md` — 多端适配 brief（断点、桌面布局、iOS 26 token 补强）

### 看过的截图

- `screenshots/console-chat.jpg` — akari 主题聊天界面：消息气泡上的新拟态阴影、实心皇家蓝用户气泡、冷瓷白底色、紧凑的全小写排版
- `screenshots/console-views.jpg` — akari 主题控制台设置页：密集的设置行（model、temperature、proactive toggle）、Lucide 图标、eyebrow 大写标签、44px 行高
