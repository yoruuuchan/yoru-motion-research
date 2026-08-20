# counter-confetti

**数据与指标**

大数字 easeOutQuart 冲刺计数并带 scale 过冲，到位前一拍 52 片彩纸从两侧抛物线炸入，冲击环扩散、标签字距收紧收尾

- **适用** 里程碑/成绩数字的庆祝拍：用户数、营收、下载量等"值得开香槟"的指标揭示
- **时长** 约 4.6s（138f@30fps；计数 0.3–2.6s · 纸屑 2.4s 起 · 落定 3.3s）
- **能量** 高（计数蓄力 + 爆点释放，标准的情绪峰值镜头）

## 我的判断

| 变体 | 判断 | 分数 | 预览 |
|---|---|---:|---|
| `counter-confetti` | maybe |  | [看片](https://vincentwei1021.github.io/video-shotcraft/media/counter-confetti.mp4) |

## 意图

数字不是"显示"出来的，是"冲线"的：计数曲线前快后慢像百米冲刺进入慢镜，纸屑在数字到位**之前**抢拍爆开——庆祝比结果先到半拍，情绪压过信息，观众先兴奋再看清数字。

## 参数表

| 参数 | 典型值 | 调节手感 |
|------|--------|----------|
| 计数曲线 | easeOutQuart，0.06–0.56 | 换 outCubic 冲刺感减弱；线性计数是最常见的"没有情绪"写法 |
| 抢拍量 | BURST 提前 0.04 | 提前 0–0.02 读作同拍；>0.08 纸屑像"别人的庆祝" |
| 纸屑数量 | 52 片（8 色调色板） | <30 稀疏不成雨；>80 遮数字。PAL 是"演出彩纸"，一般不随品牌换色 |
| 重力/初速比 | g≈2.5×|vy| | 决定抛物线顶点在画面上 1/3 处；g 太小纸屑飘出画顶 |
| scale 过冲 | 1.3 峰值 + outBack 回落 | 数字是主角，过冲 >1.5 会撞到标签排版 |
| 终值 | p*1000（演示值） | 换真实数字：保持"从 0 滚到终值"，跳变起点会丢冲刺感 |

## 已知坑

- 纸屑物理用 `life = u*1.1` 的归一化秒——改 dur 后重力体感会变（同 u 对应不同真实时长），需重调 g/vy
- 抢拍差 0.04 是硬编码在 BURST 与计数终点两处的常量，改计数窗口时同步平移 BURST 保持提前量
- 纸屑 opacity 尾段 0.74 起衰减到 0.05——别让纸屑活到 t=1 还在飞，落定段（标签收字距）需要干净背景
- 配 SFX：计数段 tick 渐密 + BURST 拍 pop/confetti + 到位拍 impact——三层缺一情绪都塌（对照 sound-design.md counter 类）

## 出处

- 参数卡原文 [counter-confetti.md](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/references/shots/data/counter-confetti.md)
- 上游实现 [data/counter-confetti](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/demos/data/counter-confetti)
- 授权 Apache-2.0，可改可用，见 [`../../../LICENSE`](../../../LICENSE) 与 [`../../../NOTICE.md`](../../../NOTICE.md)
