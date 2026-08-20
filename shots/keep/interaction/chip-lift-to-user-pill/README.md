# chip-lift-to-user-pill

**交互与功能演示**

网格里的目标 chip 先 3 帧硬切反色成黑底白字，其余 chip 按到它的曼哈顿距离交错淡出缩小；黑 chip 左缘锚定向右生长成药丸，内部逐字打出人名并点亮绿点，再拉一条 1px 连接线接到圆形徽标

- **适用** "从一堆候选里选中并展开这一个"的交互链路；协作/通讯录/收件人类产品的功能演示；选中→详情的转场
- **时长** 约5.0s（150f@30fps）
- **能量** 中（选中那一下是硬爆点，之后全是从容的生长与打字）

## 我的判断

| 变体 | 判断 | 分数 | 预览 |
|---|---|---:|---|
| `chip-lift-to-user-pill` | keep | 4 | [看片](https://vincentwei1021.github.io/video-shotcraft/media/chip-lift-to-user-pill.mp4) |

## 意图

让"选中"这件事有**两段完全不同的质感**：选中瞬间是硬的（3 帧台阶化反色，
像真实 UI 的 `:active`），选中之后是软的（药丸生长、逐字打字、绿点点亮）。
其余 chip 按距离交错淡出，是在告诉观众"注意力从这里开始收拢"——
距离排序比时间排序重要，因为它给出了空间上的因果。

## 参数表

| 参数 | 典型值 | 调节手感 |
|------|--------|----------|
| 反色时长 | t 0.04→0.085，台阶化成 3 档 | **不要给它缓动**：连续插值读作"渐变高亮"，台阶才读作按下 |
| 距离间隔 | 0.022 / 曼哈顿距离 | 按 index 排序也能错峰，但按距离才有"从选中点扩散"的空间因果 |
| 余项退场 | 各 0.075、opacity→0 + scale→0.9 | 只淡出不缩小会显得"被擦掉"；缩到 0.9 才像退到后面 |
| 药丸生长 | width 40→190px，t 0.26→0.44 outCubic，左缘锚定 | 双向生长（居中扩张）会把它读成弹窗，不是同一个 chip 长大 |
| 逐字打字 | 以 g 为自变量，间隔 0.062、各 0.05 | 挂在 g 上而不是 t 上：改生长时长时打字节奏自动跟随 |
| 绿点 | 7px + 0 0 8px 辉光，g 的 0.85→1 段 outBack | 必须在生长收尾才亮：早了就成了"已在线"，不是"刚接上" |
| 连接线 | 0→90px，t 0.47→0.57 outQuad | 线要在药丸完全定型后才起笔，否则读作药丸在被拽 |
| 徽标 | 26px，0.56→0.63 outCubic，scale 0.8→1 | 与连接线抵达重叠 0.01，才有"线到即物到"的交棒 |

## 已知坑

- 目标 chip 必须在动画前提到 DOM 最上层，否则生长时被右侧 chip 盖住
- 药丸内的人名容器 `left:13px` 是按 24px 高的 chip 配的内边距；
  改 chip 高度要同改，否则文字贴边
- 绿点的 `left = w − 15` 每帧重算——写死坐标后一改 PW1 就飞出药丸
- 连接线与徽标的坐标全部基于 `PX + PW1`（药丸终态右缘），
  改生长终值必须同改这两处
- 占位内容：12 个双字母标签 + 人名 "Casey Doe" + 字幕
  "Starting with Casey"，落地全部替换；人名字符数变化会改变打字总时长
  （间隔 0.062 × 字符数必须留在 g 的 1.0 以内）

## 出处

- 参数卡原文 [chip-lift-to-user-pill.md](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/references/shots/interaction/chip-lift-to-user-pill.md)
- 上游实现 [interaction/chip-lift-to-user-pill](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/demos/interaction/chip-lift-to-user-pill)
- 授权 Apache-2.0，可改可用，见 [`../../../LICENSE`](../../../LICENSE) 与 [`../../../NOTICE.md`](../../../NOTICE.md)
