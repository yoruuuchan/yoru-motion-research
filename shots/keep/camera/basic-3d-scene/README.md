# basic-3d-scene

**运镜与空间**

impress.js 式空间演示：卡片以不同位置/旋转/缩放散布 3D 空间，相机取各步姿态之逆依次飞行对齐，末步拉到 OVERVIEW 总览

- **适用** 概念/路线图/三步法的空间化讲述；替代平面 slides 的"每一步都换个空间视角"
- **时长** 约 6.0s（180f@30fps；四站，三段飞行各 0.96s）
- **能量** 中（每次转场有空间惊喜，停留段安静读卡）

## 我的判断

| 变体 | 判断 | 分数 | 预览 |
|---|---|---:|---|
| `basic-3d-scene` | keep | 4 | [看片](https://vincentwei1021.github.io/video-shotcraft/media/basic-3d-scene.mp4) |

## 意图

把"翻页"变成"在想法的空间里旅行"：每张卡不仅有位置还有姿态（第二步侧转 40°、第三步整个画框转 90°），相机对齐它时观众的世界也跟着转——空间变化本身成为"进入新章节"的仪式感。

## 参数表

| 参数 | 典型值 | 调节手感 |
|------|--------|----------|
| 站点姿态 | 每站至少一个新变换维度 | 只挪 x/y 是平移幻灯片；rz 站（画框旋转）是记忆点，一支片用一次 |
| 飞行时长 | 0.16（约 0.96s） | 有旋转的段别快于 0.12，观众需要时间理解"世界在转" |
| 停留间隔 | 0.10–0.12 | 读卡位；卡内文字多时优先加停留而不是减飞行 |
| OVERVIEW 缩放 | s=3.1（相机拉远 1/3.1） | 值越大总览越"高空"；保证所有卡都进画框再留 10% 边距 |
| 聚焦衰减 | opacity 0.28 底 + blur 3.5px 峰 | 底值别低于 0.2——离焦卡要"在场"，纯黑会丢空间感 |
| perspective | 1000px | 与最大 |z|（520）比值约 2:1；更深的 z 需同步加大 persp 防畸变 |

## 已知坑

- 逆变换的旋转顺序（Z→Y→X 反着正变换的 X→Y→Z）不能乱——乱序在单轴旋转时看不出来，多轴复合站会歪
- 卡片 pose 写在卡自身 transform 和相机公式两处消费，加站只改 poses 表，两处 transform 字符串别动
- rz90° 站的卡内文字会跟着躺倒，相机转正后才可读——这是设计（转正瞬间"啊看懂了"），但该站文案要短
- OVERVIEW 后无返程，作段落收尾用；要循环回 STEP01 就在末尾加一段 fly back（cam 再 lerp 回 poses[0]）

## 出处

- 参数卡原文 [basic-3d-scene.md](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/references/shots/camera/basic-3d-scene.md)
- 上游实现 [camera/basic-3d-scene](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/demos/camera/basic-3d-scene)
- 授权 Apache-2.0，可改可用，见 [`../../../LICENSE`](../../../LICENSE) 与 [`../../../NOTICE.md`](../../../NOTICE.md)
