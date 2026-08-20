# row-embed

**界面登场与陈列**

内容行像卡片一样从空中降下、rotateX 收平、嵌入瞬间底边亮一道强调色的缝

- **适用** "结构化数据长进页面"的详情页/列表镜头；行级内容的批量入场
- **时长** 约 2s（12–68f）
- **能量** 中

## 我的判断

| 变体 | 判断 | 分数 | 预览 |
|---|---|---:|---|
| `row-embed` | keep | 4 | [看片](https://vincentwei1021.github.io/video-shotcraft/media/row-embed.mp4) |

## 意图

详情页的行不是"显示出来"而是"长进去"——每一行从空中降下并严丝合缝嵌入页面布局，嵌入瞬间的强调色缝是"咔哒"扣上的视觉拟音。

## 参数表

| 参数 | 典型值 | 调节手感 |
|------|--------|----------|
| 节拍 | 第 i 行 cue = 12 + i·9，飞行 12f，最后一行 60f 落地、强调色缝 68f 收尾 ≤ 镜头 70f 预算 | 先算"最后一行何时落地"再定 cue 间隔——节拍×行数要对预算（同 document-typewriter-reveal 卡的核心算术） |
| 飞行姿态 | `perspective(900px) translateY(−120·air) rotateX(16°·air)`，scale 1.06→0.995 再 4f press-bounce 回 1 | rotateX 收平是"嵌入"的关键读感；纯垂直下落读作贴纸 |
| 飞行体 | backgroundImage 取整页截图、backgroundPosition 负偏移裁出该行 | 纹理裁片不重绘内容（Q1）——重绘的行和页面字体渲染有肉眼可见差异 |
| 空槽补丁 | 行位先盖页面底色 patch，落地后 2f 消失 | 无补丁时纹理里烤入的行会先透出来，飞入变成"重影" |
| 嵌入闪光 | 底边 2px 强调色缝从中心向两侧 5f 展开（Easing.out cubic）、8f 淡出，带 6px 辉光 | 缝只在底边、只闪一次；四边都闪读作选中框 |
| 相机 | cy 300→760 匀速 75f 下摇 | 运镜与行雨并行制造"边看边长"的感觉；相机若等行落完再动，镜头会拖 |

## 已知坑

- 飞入终点必须是页面布局真实槽位、落地即嵌入（Q9）——要"从空中飞入，嵌入 dashboard"；悬浮其上不落地会显得假
- 强调色缝等光效必须裁进承载元素圆角边界内（Q4 判例），光溢出圆角是廉价感典型来源

## 出处

- 参数卡原文 [row-embed.md](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/references/shots/ui-entrance/row-embed.md)
- 上游实现 [ui-entrance/row-embed](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/demos/ui-entrance/row-embed)
- 授权 Apache-2.0，可改可用，见 [`../../../LICENSE`](../../../LICENSE) 与 [`../../../NOTICE.md`](../../../NOTICE.md)
