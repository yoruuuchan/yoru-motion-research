# segmented-thumb-hero

**交互与功能演示**

分段控件 thumb 位移当主角特写——超大胶囊 segmented control 弹簧浮入，描边箭头光标画外滑入按下，白 thumb 8f ease-out 滑到另一段，到位瞬间新图标 spring 弹出、旧图标收起

- **适用** "模式切换/二选一"功能的宣告镜头（Ask→Computer、Chat→Agent 式）；一个 UI 微交互撑一整镜的特写拍法
- **时长** ~3.5s（demo 110f：浮入 18f + 光标 24f + 点击 + 滑动 8f + 图标弹出 + hold）
- **能量** 中（微交互特写，精致不轰）

## 我的判断

| 变体 | 判断 | 分数 | 预览 |
|---|---|---:|---|
| `segmented-thumb-hero` | keep |  | [看片](https://vincentwei1021.github.io/video-shotcraft/media/segmented-thumb-hero.mp4) |

## 意图

产品切到新模式，通常拍法是整个界面换掉。本卡反着来：把 segmented
control 放大到 1080px 宽拍特写，**thumb 那 8 帧位移本身就是叙事**——
"我们从 A 走到了 B"。没有任何页面上下文，控件即舞台。因果链完整：
光标滑入（有人来了）→ 按下+涟漪（做了决定）→ thumb 滑动（世界响应）
→ 新图标弹出（新身份确立）。四拍缺一不可，缺了光标就是 UI 自己在动，
缺了图标弹出就是切换没有奖励。

## 参数表

| 参数 | 典型值 | 调节手感 |
|------|--------|----------|
| 控件尺寸 | 1080×220，thumb 内缩 16px | 缩到 <600px 宽就不是特写了，thumb 位移读不出重量 |
| thumb 时长 | 8f Easing.out(cubic) | >14f 读作慢动作演示视频；<5f 读作瞬移，"滑"没了 |
| 光标滑入 | 24f 从画外，ease-out | linear 或 <14f 读作光标被扔进来；起点必须画外 |
| 按下 | scale 0.86 + 涟漪 12f | 无按下直接滑 thumb，因果链断，读作自动播放 |
| 图标弹出 | spring damping 10/stiffness 220 | damping <8 弹三下抢 thumb 的戏；旧图标不收起文字会挤出控件 |
| 收尾 hold | 新态静置 ≥30f | 切换完立刻切镜，"新模式"没被看清 |

## 已知坑

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
  首次实战须以真实素材回验
- 与 input-trigger-moves 分工：cursor-performance 是光标在完整页面里
  点击推近（有上下文），本卡是控件脱离页面拍无背景特写——同片可共存，
  但同一次点击别既拍页面版又拍特写版
- 图标塌缩用 width 归零而不是只 scale——只 scale 会留空位，文字不回流，
  控件内出现"幽灵缝"（demo 里 width 与 scale 同步驱动）
- 二段以上（3+ 段）控件慎用：thumb 跨多段滑行 8f 太快读不出停靠，
  拉长又破手感——本卡吃"二选一"最顺
- 涟漪圆环要 zIndex 压在 thumb 之上、圆心锁点击点——跟着 thumb 走
  就成了 thumb 的拖尾，语义变错
- 实战替换素材：段标签/图标换成真功能名即可，但"新段图标带表情"
  （demo 笑脸 laptop）是奖励感的一半，纯线框图标会淡不少

## 出处

- 参数卡原文 [segmented-thumb-hero.md](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/references/shots/interaction/segmented-thumb-hero.md)
- 上游实现 [interaction/segmented-thumb-hero](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/demos/interaction/segmented-thumb-hero)
- 授权 Apache-2.0，可改可用，见 [`../../../LICENSE`](../../../LICENSE) 与 [`../../../NOTICE.md`](../../../NOTICE.md)
