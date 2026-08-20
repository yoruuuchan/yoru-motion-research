# color-block-step-wipe

**转场**

离散阶跃色块吞屏两式——A 中央小条按 3–5 步硬跳阶跃扩成全屏（接管后徽章两跳弹出），B 色块从角落斜向 3 步吃屏并携带一张页面卡逐跳前进

- **适用** 品牌色转场/章节交接；"硬朗无缓动"的像素游戏手感段落；接管后的纯色场当下一段的舞台
- **时长** A ~2.5s（生长 44f + 徽章 + hold）/ B ~1.5–2s（3 跳 30f + hold）；demo 合计 150f
- **能量** 中高（能量来自"跳变"的顿挫而非速度）

## 我的判断

| 变体 | 判断 | 分数 | 预览 |
|---|---|---:|---|
| `color-block-step-wipe` | keep | 2 | [看片](https://vincentwei1021.github.io/video-shotcraft/media/color-block-step-wipe.mp4) |

## 意图

库里 wipe 类全是连续扫过——边界匀速或缓动地推过去。本卡反着来：
**全程零插值零缓动**，色块像老式像素游戏的方块生长，每一跳都是硬切，
跳与跳之间完全静止。顿挫本身就是节奏：3–5 声"咔、咔、咔"比一次
平滑扫过更有宣告感。变体 B 再加一层：色块推进时携带一张内容卡同拍
离散跳位——卡不做补间，读作"整块被搬进来"，色块是运货的不是装饰的。

## 参数表

| 参数 | 典型值 | 调节手感 |
|------|--------|----------|
| 步数 | A 4–5 跳 / B 3 跳 | ≥7 跳读作低帧率滚动而非阶跃；2 跳读作闪切 |
| 跳位间隔 | 6–12f | <5f 眼睛跟不上"跳了几步"；>16f 中段静止读作卡死 |
| 徽章过冲 | 0.55→1.12→1 三档硬跳 | 改成连续 spring 破语法；过冲档 >1.2 读作弹跳动画 |
| 携带卡 | 与色块同拍跳位，rotate -4° 定角 | 卡若做补间滑动，"整块搬运"手感全失；逐跳换角度读作抖动 |
| 斜角 clip | polygon 直角三角形从角落长出 | 边缘加圆角/羽化即破"硬边"人设 |
| 接管 hold | 铺满后 ≥30f 纯色静置再进下段内容 | 刚铺满就上内容，"吞屏"这一拍没呼吸完 |

## 已知坑

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
  首次实战须以真实素材回验
- 与 wipe-transitions 分工：clock-wipe/blinds 是连续几何边界扫过（顺滑系），
  本卡是离散阶跃（顿挫系）——同片两系并用要隔开段落，紧邻会互相衬得对方像 bug
- 与 shot-transitions 的关系：本卡是"转场+接管"复合体（色块留下当新场底色），
  纯交接不留场的接缝用 shot-transitions 选型，别为了转场硬造一个色块
- **声音强依赖**：每跳一声打点（同 cel-flash-stomp 的 kick 逻辑）——
  无声版阶跃容易被观众读作播放器卡顿
- 阶跃的"故意感"靠对比成立：同段落其他元素须是顺滑补间，全片到处阶跃
  就没人信这是设计
- 实战品牌色：色块用品牌主色，A/B 两式同片可各一次但换色（demo 蓝/红）；
  同色连用两次读作素材复用

## 出处

- 参数卡原文 [color-block-step-wipe.md](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/references/shots/transition/color-block-step-wipe.md)
- 上游实现 [transition/color-block-step-wipe](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/demos/transition/color-block-step-wipe)
- 授权 Apache-2.0，可改可用，见 [`../../../LICENSE`](../../../LICENSE) 与 [`../../../NOTICE.md`](../../../NOTICE.md)
