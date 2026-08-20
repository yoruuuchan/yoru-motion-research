# speed-ramp-freeze

**节奏与蒙太奇**

帧号非线性 remap 的两款节奏手法——变速（快→0.2x 凝视→快）与定格标注（流动→定格圈注→解冻）

- **适用** 卡片流/长横移中把一个重点"放慢/停下给人看"；教学解说语境用定格标注
- **时长** 变速全程 4–5s（慢速窗 ≥40f）；定格标注全程 4–5s（定格段 ≥45f）
- **能量** 中高（速度反差本身即energy beat）

## 我的判断

| 变体 | 判断 | 分数 | 预览 |
|---|---|---:|---|
| `freeze-annotate` | maybe |  | [看片](https://vincentwei1021.github.io/video-shotcraft/media/freeze-annotate.mp4) |

## 意图

匀速流读作 PPT（R2），全程快流观众抓不住重点（R3）。变速在一条
运动里制造"冲刺-凝视-冲刺"；定格标注更进一步——干脆停下来，
马克笔圈出重点再走。两款同一技术根（帧号 remap），语义不同：
变速是"路过时多看一眼"，定格是"停课划重点"。

## 参数表

| 参数 | 典型值 | 调节手感 |
|------|--------|----------|
| 慢窗/定格时长 | ≥40f / ≥45f | 短了凝视不成立（R3 宁慢勿快） |
| 快慢斜率反差 | ≥10 倍 | 反差不足读不出"慢下来了" |
| 圈注描边 | 8f 划完 + 抖动 scale 7 | 太慢像加载动画；无抖动像机械标注 |

## 已知坑

- 变速段 SFX 钉帧跟**输出帧**不跟源帧（画面动作在输出时间轴上发生）；
  拟音槽位：定格款配马克笔沙沙声（S4），本卡转正时未配、实战补
- 定格标注一支 30s 片 ≤2 次（同 D 式克制原则）
- 参数经占位素材调校转正，非实战定稿，首次实战后回验

## 出处

- 参数卡原文 [speed-ramp-freeze.md](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/references/shots/rhythm/speed-ramp-freeze.md)
- 上游实现 [rhythm/speed-ramp-freeze](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/demos/rhythm/speed-ramp-freeze)
- 授权 Apache-2.0，可改可用，见 [`../../../LICENSE`](../../../LICENSE) 与 [`../../../NOTICE.md`](../../../NOTICE.md)
