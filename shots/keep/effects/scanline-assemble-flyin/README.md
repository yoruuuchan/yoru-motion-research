# scanline-assemble-flyin

**光效与强调**

页面开场是空的暗底网格，一条亮扫描线自上而下掠过；扫到每个区块的落点，该处组件就从画外飞入贴合，带残影模糊与落位闪边——扫完整页恰好装配完成

- **适用** "页面自己生成"的开场；AI 建站/自动排版类产品的核心演示；从空白到成品的能力叙事
- **时长** 约4.6s（138f@30fps）
- **能量** 中高（扫描线是稳的，但每次组件飞入都是一个爆点，密度递进）

## 我的判断

| 变体 | 判断 | 分数 | 预览 |
|---|---|---:|---|
| `scanline-assemble-flyin` | keep | 4 | [看片](https://vincentwei1021.github.io/video-shotcraft/media/scanline-assemble-flyin.mp4) |

## 意图

让"页面被生成"这件事有一个可信的施工顺序：扫描线是施工进度条，
组件从画外飞进来贴合是施工动作。关键是**扫完那一刻恰好装完最后一块**
——扫描线提前收工或组件拖尾都会让"扫描驱动装配"的因果关系散掉。

## 参数表

| 参数 | 典型值 | 调节手感 |
|------|--------|----------|
| 扫描线 | t 0.05→0.72 匀速，y −30→300 | 收工时刻要略晚于最后一块落位，才读作"扫完即装完" |
| 触发换算 | ft = 0.05 + ((y+30)/330)·0.67 − 0.02 | 那个 −0.02 是提前起飞量：去掉就变成"扫过之后才动"，慢半拍 |
| 最小间隔 | prev + 0.045 | y 接近的页脚/社交会同时飞；钳制后才有"一块一块"的密度 |
| 飞入位移 | 画外 60–260px，按组件所在方位定 | 位移小于 60px 读作"抖一下就位"，不是从画外来 |
| 飞入旋转 | ±3–8° | 超过 12° 就读作"翻滚"，贴合时不服帖 |
| 飞入缓动 | outBack，0.15 时长 | outBack 的过冲是"吸附贴合"的手感；outCubic 就成了滑入 |
| 残影模糊 | blur ≤2.2px，随 1−a 衰减，a>0.97 清零 | 不清零会留一层永久糊；阈值必须留裕量 |
| 落位闪边 | inset −3px、1px 强调色，0.04 亮 / 0.11 落 | 闪边是"咬合"的听觉替代品，去掉后落位没有实感 |

## 已知坑

- **触发时刻与 plan 里的落点 y 绑定**：换页面模板后每个组件的 y 要重测，
  否则组件在扫描线到达前就飞入
- `filter` 与 `transform` 同时作用于组件节点，落位后必须把 filter 设回
  `none`（不是 `blur(0)`）——留着合成层会持续吃 GPU
- 闪边层是 append 到组件内部的子节点，组件本身若有 `overflow:hidden`
  会把 `inset:-3px` 裁掉，需改成外层兄弟节点
- 与 `scanline-annotate-focus` 共用同一套页面模板与扫描线；两张卡可以
  串联（先装配、后分析），但扫描线要换向或留空档，否则读作重复
- 页面内容为中性占位模板，ACCENT（`#9fb6e8`）可按项目替换

## 出处

- 参数卡原文 [scanline-assemble-flyin.md](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/references/shots/effects/scanline-assemble-flyin.md)
- 上游实现 [effects/scanline-assemble-flyin](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/demos/effects/scanline-assemble-flyin)
- 授权 Apache-2.0，可改可用，见 [`../../../LICENSE`](../../../LICENSE) 与 [`../../../NOTICE.md`](../../../NOTICE.md)
