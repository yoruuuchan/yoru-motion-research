# print-texture-transitions

**转场**

印刷质感转场——ink-bleed-reveal 墨渗揭示（须状渗边洇开吃掉旧景）

- **适用** 换景接缝的纸墨审美款；与交棒六式/穿越三式并列的第三族——"介质显影"型转场
- **时长** 4–4.5s（洇开段 55–80f + 静止收尾 ≥30f）
- **能量** 中（渐进显形，无冲击拍）

## 我的判断

| 变体 | 判断 | 分数 | 预览 |
|---|---|---:|---|
| `ink-bleed-reveal` | keep |  | [看片](https://vincentwei1021.github.io/video-shotcraft/media/ink-bleed-reveal.mp4) |

## 意图

转场语言已有交棒（shot-transitions 六式）和穿越（transition-travel）
，都是空间/光学隐喻。本式开第三族：**介质隐喻**——新画面不是"到来"
而是"印染"出来的，直接调用库内纸墨审美的物理想象：像一滴墨落在
宣纸上洇开吃掉旧景，有机、书写感。天然亲和 paper/ink 调性的片子，
是 light-leak-burn（强调色漏光）之外的另一个"介质系"接缝选择。

## 参数表

| 参数 | 典型值 | 调节手感 |
|------|--------|----------|
| 渗边 | SVG mask 白圆挂 `feTurbulence(fractalNoise, baseFrequency 0.02, octaves 3, seed 固定)` + `feDisplacementMap scale 60→160 随帧涨` | filter 只揉遮罩形状、内容始终清晰；seed 必须写死（确定性） |
| 洇开 | 半径 [20,98f]→[0,1450px] Easing.out(quad)，乘 `1+0.08·sin(0.32f)·env` 快慢不匀扰动（env 末 20f 衰减归零） | 匀速圆扩张读作普通 iris——扰动即"墨的脾气" |
| 收尾摘罩 | 洇满后（帧 ~100）摘掉 SVG mask 直接铺新景 | feTurbulence 有亚像素抖动，不摘则结尾永不真静止（本批实渲判例） |
| 收尾 | 新景就位后真静止 ≥30f | R1 |

## 已知坑

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
  首次实战须以真实素材回验
- 一缝一式规矩同 shot-transitions：介质转场不与白闪/震屏叠加；
  本式与 light-leak-burn 介质系同片合计 ≤2 次，多了片子读作印刷厂宣传
- 洇开中段旧景内容会透过噪声孔洞碎片式短暂露出——读作墨渍肌理
  属可接受有机效果，但旧景若是人脸/logo 等高辨识元素会读作故障，避开
- 慢转场（55–80f 动作段），高节奏连打段落别用——那里去 E 式甩镜

## 出处

- 参数卡原文 [print-texture-transitions.md](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/references/shots/transition/print-texture-transitions.md)
- 上游实现 [transition/print-texture-transitions](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/demos/transition/print-texture-transitions)
- 授权 Apache-2.0，可改可用，见 [`../../../LICENSE`](../../../LICENSE) 与 [`../../../NOTICE.md`](../../../NOTICE.md)
