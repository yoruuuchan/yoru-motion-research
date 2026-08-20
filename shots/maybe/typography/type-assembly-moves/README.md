# type-assembly-moves

**文字与字卡**

文字集结四式——split-text-stagger 逐字裂升、letterform-drift-assembly 漂移合拢、tracking-expand-reveal 字距呼吸、text-on-path 沿线流入

- **适用** 大标题/标语的入场；与 type-entrance-moves 两式、split-flap-title、document-typewriter-reveal 同属标题入场大品类，全片 ≤2 种
- **时长** 单式 4–5s（动作段 A ~56f / B ~104f / C ~58f / D ~99f，均含 hold）
- **能量** A 中 / B 中高 / C 低中 / D 中

## 我的判断

| 变体 | 判断 | 分数 | 预览 |
|---|---|---:|---|
| `split-text-stagger` | maybe |  | [看片](https://vincentwei1021.github.io/video-shotcraft/media/split-text-stagger.mp4) |

## 意图

标题入场已有"原位变形系"四式（乱码解码/字符坠落/翻牌/打字机——字
在原地换形态）。本卡补"集结系"：字符从别处**汇聚成**标题，运动轨迹
本身有戏。A 琴键式——每字从看不见的裁切线下滑升，理性利落，通用度
最高；B 片头式——字符四散带模糊漂入、逐个锁定加深，Stranger Things
的仪式感，适合品牌名亮相;C 呼吸式——字母从叠压一团吸一口气展开，
最安静的一式，适合抒情段落；D 语义式——字符沿一条上升曲线鱼贯流入
再摆正，曲线可以正好描着图表增长线走，文字与数据同框叙事。

## 参数表

| 参数 | 典型值 | 调节手感 |
|------|--------|----------|
| A 过冲 | 10%（原案 6% 可测不可感，实渲加码） | 正常速度要看得见回落那一下 |
| B 锁定脉冲 | 字色深到 #000 + 描边 0→3px→0 / 8f | 白底上加深+描边，不用发光（判例） |
| B 漂移三绑定 | 位移 (1−p)、blur 8(1−p)、opacity 0.35→1 共用一条 p | 三者分曲线走，字会"到了还糊着" |
| C 实现命门 | letter-spacing 恒为终态，逐字符 span 只做 translateX=(1−p)(i−词心)(−0.56em) | 直接动 letter-spacing 逐帧重排必抖 |
| D 摆正 | 到达停 8f 再 12f lerp 到水平基线（y 拉平 rotate→0） | 不摆正就永远是"挂在线上"，读不出标题 |
| D 曲线 | evolve（dashoffset）随最前字符同步生长 | 曲线先画完字再走，读作两个动画 |
| 收尾 | 全员落定真静止 ≥30f | R1 |

## 已知坑

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
  首次实战须以真实素材回验
- 标题入场大品类现已八式（本卡四式 + type-entrance-moves 两式 +
  split-flap-title + document-typewriter-reveal），**同片 ≤2 种**（P4）铁律不变
- B 式与 D 式都是高注意力入场，别再叠相机动作——字在飞的时候镜头必须稳
- C 式幅度命门：起始叠压至少 −0.4em 级（每缝 80px+ 位移）才可感，
  −0.1em 级"微展开"正常速度读不出（可感性判例）
- D 式字符在曲线低段会短暂交叠，是鱼贯读感的一部分；但字号 >80px 时
  交叠面积过大会糊成一团，大字改用更长曲线或减字数

## 出处

- 参数卡原文 [type-assembly-moves.md](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/references/shots/typography/type-assembly-moves.md)
- 上游实现 [typography/type-assembly-moves](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/demos/typography/type-assembly-moves)
- 授权 Apache-2.0，可改可用，见 [`../../../LICENSE`](../../../LICENSE) 与 [`../../../NOTICE.md`](../../../NOTICE.md)
