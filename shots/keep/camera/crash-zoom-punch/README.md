# crash-zoom-punch

**运镜与空间**

全景一拍急推到目标特写（6f），落位二选一——过冲回弹（弹性）或撞停震屏（重量）

- **适用** 功能段"点名"镜头——把观众视线一拍按到目标卡/模块上；强调级用撞停
- **时长** 约 0.5s 动作 + 前后 hold（动作 6–11f，前 hold ≥30f 建立全景、后 hold ≥45f 读特写）
- **能量** 高（瞬时冲击，非持续高能）

## 我的判断

| 变体 | 判断 | 分数 | 预览 |
|---|---|---:|---|
| `crash-zoom-punch` | keep |  | [看片](https://vincentwei1021.github.io/video-shotcraft/media/crash-zoom-punch.mp4) |

## 意图

慢推近（spotlight-hero-card）是"请看"，急推是"看这个！"——一拍之内
从全景砸到特写，视线没有选择余地。落位质感分两款：回弹是弹性
（"看这个"），撞停震屏是重量（"就是它"），按强调级选。

## 参数表

| 参数 | 典型值 | 调节手感 |
|------|--------|----------|
| 急推时长 | 6f（4–8f） | >10f 读作普通推近，冲击感消失 |
| 目标 zoom | 2.4–2.8 | 终点构图以目标卡占画面 60–75% 为准 |
| 回弹幅度 | zoom 的 3–6% | 过大读作弹簧玩具 |
| 震屏包络 | 14px·e^(−t/1.8) | 幅度须过肉眼阈值（可感性判例），>20px 读作故障 |

## 已知坑

- 终点必须是高清纹理槽位（card4-hires 级）——急推后全程特写它，
  低倍截图糊字（Q2）；终点先按 Q2 的高分辨率栅格化技法处理
- 两款别混用：回弹后再震屏读作穿帮；一支片急推 ≤2 次（P4 手法去重精神）
- 参数经占位素材调校转正，非实战定稿，首次实战后回验

## 出处

- 参数卡原文 [crash-zoom-punch.md](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/references/shots/camera/crash-zoom-punch.md)
- 上游实现 [camera/crash-zoom-punch](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/demos/camera/crash-zoom-punch)
- 授权 Apache-2.0，可改可用，见 [`../../../LICENSE`](../../../LICENSE) 与 [`../../../NOTICE.md`](../../../NOTICE.md)
