# depth-layer-moves

**运镜与空间**

分层深度两款运镜——多层视差滑轨（3 层速度梯度横移出纵深）与伪 dolly-zoom（主体钉死、背景膨胀压来）

- **适用** 平面截图要"有厚度"的段落；戏剧性蓄力时刻用 dolly-zoom（一支片 ≤1 次）
- **时长** 视差滑轨 4–5s 持续；dolly-zoom 3–4s 单向行程
- **能量** 视差=中（质感型）；dolly-zoom=中高（压迫感渐强）

## 我的判断

| 变体 | 判断 | 分数 | 预览 |
|---|---|---:|---|
| `dolly-zoom` | keep | 4 | [看片](https://vincentwei1021.github.io/video-shotcraft/media/dolly-zoom.mp4) |
| `multiplane` | keep |  | [看片](https://vincentwei1021.github.io/video-shotcraft/media/multiplane.mp4) |

## 意图

整页平移是"看页面"，分层深度是"在页面的空间里"。视差滑轨给横移
加纵深（迪士尼多平面摄影机原理，Linear 片同款质感）；伪 dolly-zoom
反过来——主角纹丝不动、全世界压过来，给戏剧性时刻蓄力。

## 参数表

| 参数 | 典型值 | 调节手感 |
|------|--------|----------|
| 视差层系数 | 0.35 / 0.7 / 1.4 | 梯度 ≥2 倍层间才可辨；层数 ≤4 防过载 |
| 层次锚 | 前后景 blur + 背景降饱和 | 没有 blur/饱和锚，读作"贴片乱飞" |
| dolly 膨胀行程 | scale 1→2.0–2.5 | 行程小了压迫感不足；背景 opacity ≤0.6 防读作故障 |

## 已知坑

- 主阅读层/主体必须高清纹理且无 blur——观众在读它
- 视差与 PageCam rot 3D 的组合（斜拍视差）未验证，实战先渲 still 确认
- dolly-zoom 是"戏剧调料"：一支片 ≤1 次，日常段落用视差滑轨
- 参数经占位素材调校转正，非实战定稿，首次实战后回验

## 出处

- 参数卡原文 [depth-layer-moves.md](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/references/shots/camera/depth-layer-moves.md)
- 上游实现 [camera/depth-layer-moves](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/demos/camera/depth-layer-moves)
- 授权 Apache-2.0，可改可用，见 [`../../../LICENSE`](../../../LICENSE) 与 [`../../../NOTICE.md`](../../../NOTICE.md)
