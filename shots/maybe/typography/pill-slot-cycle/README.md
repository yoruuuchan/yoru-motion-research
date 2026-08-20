# pill-slot-cycle

**文字与字卡**

句中词槽轮换——固定句干钉死不动，句尾 pill 徽章每 ~0.7s 老虎机滚一格（旧的上飞加速淡出、新的从下带模糊滑入），连换 N 个功能词后落成完整句子收束

- **适用** "功能列举"类文案的最优雅解法（比逐条列表快、比乱码解码有语义）；一句话卖点 + 多个动词短语的段落
- **时长** 入场 12f + 每拍 21f × 词数 + 收束 14f + hold；6 词约 5.8s（demo 175f）
- **能量** 中（稳定节拍器，无峰值）

## 我的判断

| 变体 | 判断 | 分数 | 预览 |
|---|---|---:|---|
| `pill-slot-cycle` | maybe |  | [看片](https://vincentwei1021.github.io/video-shotcraft/media/pill-slot-cycle.mp4) |

## 意图

罗列六个功能，列表要六行、逐条淡入要六拍还占满屏。词槽轮换把它们
塞进**一句话的一个槽位**里：句干 "One AI tool to ___" 是承诺，槽里
滚过的每个 pill 是证据，最后 pill 飞走、"do it all." 落位——证据
列举完毕，结论盖章。结构自带三幕：承诺→列举→收束。命门是句干
**纹丝不动**：观众的眼睛全程钉在槽位上，句干一晃列举感就散。

## 参数表

| 参数 | 典型值 | 调节手感 |
|------|--------|----------|
| 拍长 | 21f/词，5–7 词 | <16f 读不完短语；>28f 节拍器感散掉；8+ 词观众开始数数 |
| 换位窗 | 拍内前 8f | 拉长到 12f+ 新旧同屏太久，读作两个 pill 打架 |
| 飞行距离 | 入 +120 / 出 -130px | <80px 读作原地闪换；入出不对称（出略远）让离场更决绝 |
| 运动模糊 | 入 14→0 / 出 0→10px blur | 去掉 blur 换位读作硬弹；>20px 中间帧糊成色块 |
| 收束过冲 | Easing.back(1.4)，14f | >2 结论落位像卡通；无过冲结论与列举没有档次差 |
| 收尾 hold | 完整句静置 ≥45f | 这句话是全段目的，不 hold 等于白列举 |

## 已知坑

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
  首次实战须以真实素材回验
- 与 odometer-digit-roll / split-flap-title 分工：那两卡是字符/数位级
  机械滚动（无语义），本卡是整词级 pill 轮换且嵌在活句子里——文案是
  "句干+动词短语"结构才用本卡，纯数字/纯标题词别硬套
- 与 typewriter-moves 分工：打字机是"一个字一个字造句"，本卡是
  "句子造好了换零件"——同片可共存但别在同一句文案上连用
- 与 type-rhythm-sync 分工：那是既有文字随音轨变属性（不换内容），
  本卡换内容——绑音轨时本卡拍点对鼓点即可，别再叠字重脉冲
- pill 短语长度要接近（demo 最长 "Draft an agenda"）——长短差 >2 倍
  槽宽跳变太猛，句子重心左右甩
- 收束句与句干字号字重必须完全一致（demo 都是 96px/800）——
  "do it all." 若比句干大，读作新标题而非句子补完

## 出处

- 参数卡原文 [pill-slot-cycle.md](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/references/shots/typography/pill-slot-cycle.md)
- 上游实现 [typography/pill-slot-cycle](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/demos/typography/pill-slot-cycle)
- 授权 Apache-2.0，可改可用，见 [`../../../LICENSE`](../../../LICENSE) 与 [`../../../NOTICE.md`](../../../NOTICE.md)
