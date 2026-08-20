# smear-multiples

**节奏与蒙太奇**

残像分身——卡片高速横移时拖 4 个清晰可数的半透明分身副本，落位瞬间收拢合一；motion blur 的动画式平替

- **适用** 元素高速位移段想要"漫画式速度感"而非"摄影式模糊"时；与 CameraMotionBlur 二选一
- **时长** 元素级技法（移动 12f + 合拢回弹 8f，寄生在位移动作上）
- **能量** 中高

## 我的判断

| 变体 | 判断 | 分数 | 预览 |
|---|---|---:|---|
| `smear-multiples` | keep |  | [看片](https://vincentwei1021.github.io/video-shotcraft/media/smear-multiples.mp4) |

## 意图

快速位移的速度感库内标准答案是 CameraMotionBlur（摄影隐喻：快门拖影，
连续的糊）。本卡给第二个答案，动漫演出的 smear frame 传统：残像是
**离散、清晰、可数的**完整副本——观众能数出 4 张卡，读作"快到留下
分身"而非"快到糊掉"。两者气质完全不同：blur 是实拍级质感，分身是
漫画级趣味；同一次位移二选一，叠用读作渲染错误。分身式还有一个
实用优势：残像里内容仍可辨，适合"移动的东西本身是信息"的场景。

## 参数表

| 参数 | 典型值 | 调节手感 |
|------|--------|----------|
| 分身数/间隔 | 4 个 / 各差 2f | >5 个读作队伍；间隔 >3f 断成跳帧 |
| 移动速度 | ~900px/12f（峰值 ~100px/f） | 慢移动不配分身（门限管住）；快过 3f/程分身来不及被看见 |
| 合拢窗口 | 落位前 3f 内收干 | 分身残留到落位后读作重影故障 |
| 收尾 | 落位回弹后真静止 ≥20f | R1 |

## 已知坑

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
  首次实战须以真实素材回验
- 与 CameraMotionBlur 同一次位移**互斥**；同片不同镜头可以各用（一次
  漫画式一次摄影式反而立体），但同类位移统一用一种（P4 一致性）
- 分身是"清晰完整副本"——加 blur、拉伸、变形都会滑向另一个手法
  （轴向拉伸在词汇表另案），保持可数是本卡的身份
- 深底浅卡对比度下分身层次才读得开；同色系底上 0.09 那档会消失，
  可减为 3 个分身重配 0.5/0.3/0.15

## 出处

- 参数卡原文 [smear-multiples.md](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/references/shots/rhythm/smear-multiples.md)
- 上游实现 [rhythm/smear-multiples](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/demos/rhythm/smear-multiples)
- 授权 Apache-2.0，可改可用，见 [`../../../LICENSE`](../../../LICENSE) 与 [`../../../NOTICE.md`](../../../NOTICE.md)
