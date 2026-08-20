# wipe-transitions

**转场**

几何擦除转场两式——clock-wipe 时钟扫描（雷达指针扫一圈换页）与 blinds-slice 百叶窗切条（12 竖条错峰翻换成波）

- **适用** 新旧页都不动、一条几何边界扫过完成交接的通用转场；不依赖构图里有合适元素，哪儿都能用
- **时长** 单式 前态 ≥20f + 擦除 32–60f + 收尾 ≥40f，约 5s（150f）
- **能量** 中

## 我的判断

| 变体 | 判断 | 分数 | 预览 |
|---|---|---:|---|
| `clock-wipe` | maybe |  | [看片](https://vincentwei1021.github.io/video-shotcraft/media/clock-wipe.mp4) |

## 意图

转场库已有三族：穿越系（钻进去）、藏切系（遮住切）、体块系（页面是
实体）。本卡是第四族**几何擦除系**——新旧页都不动，一条几何边界扫过
完成交接，擦除的形状即语义：A 圆扫是"仪表盘刷新了一屏数据"，B 条扫
是"百叶窗逐叶翻面换页"。与 shot-transitions F 元素遮罩擦除的区别：
F 用页面内真实元素当遮罩（依赖构图），本卡是纯几何形——通用性即定位。
按语义选：数据刷新用 A，横向推进翻页用 B。

## 参数表

| 参数 | 典型值 | 调节手感 |
|------|--------|----------|
| A 扇形 | 中心屏心(960,540)、半径 1400 盖满四角，固定 73 顶点(SEGS=72) | 顶点数恒定且够密（40+）防锯齿跳变——命门 |
| A 扫速 | 30–90f 指针 0→360° 纯 linear，双向 clamp | 雷达要匀速；加缓动就不是雷达是钟摆 |
| A 亮线 | 四层 SVG line：26px 白 0.35 柔光 + 13px 白 0.60 + 9px 黑 0.55 暗描边 + 4px 白核 | 白底判例：纯提亮不可见，必须加暗描边；首渲 3px 白线太弱，加码 1.5x 才过 |
| B 波 | 20–52f：delay=列号×2f，每条 10f Easing.in(cubic) | 交接点恒为 x+160(1-p)，数学上无露底 |
| B 缝亮线 | 三层 SVG：16px 白 0.45 柔光 + 6px 黑 0.55 暗描边 + 3px 白核，进出各 2f 淡入淡出 | 同 A 白底判例 |
| 摘罩 | A 96f / B 52f 起条件卸载全部擦除结构，B 页直出 | opacity 0 不算摘，残留 clip-path 毁真静止 |
| 收尾 | A 54f / B 98f 真静止（≥40f） | R1 |

## 已知坑

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
  首次实战须以真实素材回验
- 擦除边界必须带亮线/高光——无亮线的 wipe 读作 PPT 转场，命门；
  亮线在浅色区靠黑描边、深色区靠白核，两侧都要可读
- A 与 circle-match-iris 的区别：iris 是从锚点炸开的圆（半径在长），
  clock 是角度在扫（半径恒定）——别因为都是圆混用
- 几何擦除全片 ≤2 次，且 A/B 别同片连用（两次"边界扫过"读作模板感）
- 亮线淡出与摘罩必须同帧衔接（A 90–96f 淡出、96f 卸载），
  差一帧就是残线穿帮

## 出处

- 参数卡原文 [wipe-transitions.md](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/references/shots/transition/wipe-transitions.md)
- 上游实现 [transition/wipe-transitions](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/demos/transition/wipe-transitions)
- 授权 Apache-2.0，可改可用，见 [`../../../LICENSE`](../../../LICENSE) 与 [`../../../NOTICE.md`](../../../NOTICE.md)
