# spotlight-hero-card

**开场与品牌**

聚光灯扫过页面锁定一张卡，斜 45° 推进后卡片弹起悬浮、光束沿轮廓两圈、贴回原位

- **适用** "单一主角"式产品开场；把一个核心对象（卡片/条目/模块）立成全片主角
- **时长** 约 4.6s（82–220f）
- **能量** 中（质感最高的一镜，节奏慢而稳）

## 我的判断

| 变体 | 判断 | 分数 | 预览 |
|---|---|---:|---|
| `spotlight-hero-card` | keep |  | [看片](https://vincentwei1021.github.io/video-shotcraft/media/spotlight-hero-card.mp4) |

## 意图

开场只讲一件事：这一张卡就是产品的原子单位。聚光灯替观众做视线引导，弹起悬浮给它体积和重量，轮廓光束是"扫描/检视"的隐喻，最后贴回原位表示它属于这个页面。

## 参数表

| 参数 | 典型值 | 调节手感 |
|------|--------|----------|
| 选卡 | cards[3]，中心 x 恰为 960（页面中心） | 主角卡先按"推进后构图居中"选，不是随便挑一张 |
| 相机 | 静止全页 zoom 0.78（82–114f）→ 16f 推进 zoom 2.6；rotY 34° 主导 + rotX 仅 8°，persp 1200；焦点取卡心左移 30px；reseat 触地后 cx/cy/zoom/rot 全锁死 ≥15f | 侧向水平机位读感优于俯拍（"从左侧拍摄而不是从下方"，Q6）；收尾禁用 zoom 2.6→2.58 一类尾漂，呼吸必须是真静止（R1） |
| 聚光灯 | 4 个中间站（86→130f），光池半径 620→420→360 收拢，锁定 +6% 脉冲；vignette 0.16→0.42 | 中间站让"随机照射"可信；直奔目标读作程序化 |
| 动作弧 | rise 10f（bezier(0.2,1.25,0.3,1) 过冲）→ 悬停 54f（sin bob 振幅 4px 周期 40f，z=110px·lift）→ reseat 18f，落地 press 0.997 | 锁定→落地 ≈98f≈3.3s——质感镜头要"放慢到 3 秒"（R3），初版几乎总是偏快 |
| 轮廓光束 | lap1 142→156f（strokeWidth 5+2.5 双层）、lap2 162→182f（3.5+1.75、整体 opacity 0.62）；strokeDasharray "0.14 1" 走 dashoffset | 两圈快慢有别才读作"持续扫描"，一圈是眨眼；光束只给主角一次（Q4） |
| 双层影 | `0 8·lift px …, 0 46·lift px 90·lift px` 随高度生长 | 影子不随高度长，悬浮就不成立 |

## 已知坑

- 开场多卡群舞撑不起第一印象（Q5）——开场曾反复推倒多次才收敛到单卡；直接从单主角+完整动作弧起稿
- 推进特写下卡上文字会糊，根因是纹理栅格化分辨率不是 DoF——配套技法展开见审美准则 Q2
- 逐卡 glint 闪烁被两次否决（"不需要每个卡片都闪烁一下"，Q4），光效严格只给主角

## 出处

- 参数卡原文 [spotlight-hero-card.md](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/references/shots/opening/spotlight-hero-card.md)
- 上游实现 [opening/spotlight-hero-card](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/demos/opening/spotlight-hero-card)
- 授权 Apache-2.0，可改可用，见 [`../../../LICENSE`](../../../LICENSE) 与 [`../../../NOTICE.md`](../../../NOTICE.md)
