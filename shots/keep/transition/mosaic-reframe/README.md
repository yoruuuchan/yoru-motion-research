# mosaic-reframe

**转场**

12 张瓦片在规则网格、feature mosaic、对角瀑布串三种排版间连续变形，位置宽高各自插值、逐片微错峰，段间留 hold

- **适用** "同一批内容多种看法"的陈列转场：作品集/模板库/相册产品的布局能力展示
- **时长** 约 6.0s（180f@30fps；浮现 0–0.6s · A→B 1.6–2.5s · hold · B→C 3.7–4.8s）
- **能量** 中（连续流动的重排，无爆点，气质从容）

## 我的判断

| 变体 | 判断 | 分数 | 预览 |
|---|---|---:|---|
| `mosaic-reframe` | keep |  | [看片](https://vincentwei1021.github.io/video-shotcraft/media/mosaic-reframe.mp4) |

## 意图

让观众看见"布局本身在思考"：同样 12 张内容，从整齐档案态（网格）变成有主次的策展态（feature mosaic），再变成有态度的动态态（对角瀑布）。三段排版是三种叙事语气，变形过程即产品能力。

## 参数表

| 参数 | 典型值 | 调节手感 |
|------|--------|----------|
| 段窗口 | 每段变形 0.16–0.18，hold ≥0.2 | hold 是读版面的呼吸位，压缩到 <0.1 三段糊成一段 |
| 微 stagger | 0.007/片（≈2 帧） | 0 = 整版机械闪变；>0.02 波浪太明显抢过版面本身 |
| 瀑布参数 | 间距 6.4/7.6%，rot −15°+3°/片 | 旋转递增是"串"的灵魂；等角会退化成斜排网格 |
| mosaic 大位 | 首片 3×2 单元格 | 换 slots 表可重排主次；保证有一块 ≥2×2 的锚点位 |
| 浮现节奏 | 0.012/片 + 0.14 时长 | 12 片合计约 0.27 进完；作转场用时可砍掉浮现直接从 A 态起 |
| 瓦片内容 | 渐变底 + 圆点 + 双信息条（占位） | 换真实截图/图片时保留 overflow:hidden 圆角容器，宽高插值不裁坏内容 |

## 已知坑

- 五通道独立插值意味着**不能**换成 `transform: scale`——宽高动画会引发子元素重排，占位内容用了百分比定位可自适应，换成真实图片要用 `object-fit: cover`
- C 段瓦片有意越出画框（y 从 −7% 到 91%），画框裁切是构图的一部分，别加 padding "修复"
- 三套坐标表都以 92% 内容区 + 4% 边距为基准，改画幅比例需整表重算
- 段窗口与 stagger 叠加后末片 B→C 到 0.887 才结束，再加段落需压缩前段而不是顺延（保证 t=1 前全部落定）

## 出处

- 参数卡原文 [mosaic-reframe.md](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/references/shots/transition/mosaic-reframe.md)
- 上游实现 [transition/mosaic-reframe](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/demos/transition/mosaic-reframe)
- 授权 Apache-2.0，可改可用，见 [`../../../LICENSE`](../../../LICENSE) 与 [`../../../NOTICE.md`](../../../NOTICE.md)
