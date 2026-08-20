# spotlight-sweep-moves

**光效与强调**

暗场聚光显影三式——A 醒睡扫过（光到即亮光走即暗）、B 贴边泛光横摇（紫光贴 UI 边缘渗入+聚光匀速右移）、C 角落匀速显影（径向聚光从角落匀速扩张点亮全屏）；黑场里"光即叙事"的 UI 展示

- **适用** 暗色调品牌片里逐个介绍 UI 面板/功能区；黑场开场把界面"点亮"登场；段落间光转场
- **时长** 单式 3.5–4.5s；A/B 可串联成巡礼段
- **能量** 中低（克制、神秘感，爆点在"亮起"瞬间）

## 我的判断

| 变体 | 判断 | 分数 | 预览 |
|---|---|---:|---|
| `corner-spotlight-reveal` | keep |  | [看片](https://vincentwei1021.github.io/video-shotcraft/media/corner-spotlight-reveal.mp4) |
| `glow-wake-sleep-panel` | keep |  | [看片](https://vincentwei1021.github.io/video-shotcraft/media/glow-wake-sleep-panel.mp4) |
| `slide-spotlight-pan` | keep |  | [看片](https://vincentwei1021.github.io/video-shotcraft/media/slide-spotlight-pan.mp4) |

## 意图

黑场里观众只能看见光给看的东西——聚光既是照明也是运镜和剪辑：
光到哪里哪里登场，光走即谢幕。三式共用"贴边紫色辉光光线"这个
身份元素（光线贴着 UI 边框/logo/顶边走，辉光要亮要糊，是光在
"抚摸"界面而不是描边动画）。命门是**匀速**：聚光的移动/扩张
严格 linear——缓动会让光有"意图"，匀速才读作探照灯的机械扫掠
（C 式判例：linear 但半径终值过大＝前 1/4 就饱和，观感照样不匀速）。

## 参数表

| 参数 | 典型值 | 调节手感 |
|------|--------|----------|
| 聚光移动/扩张 | 全程 linear、零缓动 | **匀速是命门**——全程零缓动；加 ease 读作光有主观意图 |
| C 式半径终值 | 恰好在片尾覆盖全屏（1300@1080p/100f） | 终值过大＝提前饱和假匀速：亮度采样须全程平滑爬升（实测 8/46/101/…/238） |
| 贴边光线辉光 | 3–4 层（blur26+blur9+亮芯+粉偏移） | 层少读作细线描边；辉光要够亮够糊才是"光" |
| 光线锚定 | 严格贴 UI 边缘/顶边/logo | 光线脱离边缘漂浮＝失去"抚摸界面"语义（A 式返工判例：定位丢失紫光跑到底边） |
| 显影罩 | radial 渐变硬边略糊（feather ~15%） | 边太硬像圆形遮罩；太糊没有"照到/照不到"的界线 |

## 已知坑

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
  首次实战须以真实素材回验
- 与 light-play-moves 分工：那张是元素/文字上的
  光泽戏（sheen/辉光呼吸）；本卡光是**运镜和剪辑**（显影/谢幕/转场），
  光决定观众看什么
- 三式重做判例：聚光扫过必须带贴边光线同行（v1 只有显影罩被裁
  "改改再看"——裸聚光没有身份，贴边紫光才是这个手法的签名）
- 原片（clickup-30）光线转角有一瞬彩虹色散，demo 未做；实战可
  在转角帧加 1–2f 色散层提质感

## 出处

- 参数卡原文 [spotlight-sweep-moves.md](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/references/shots/effects/spotlight-sweep-moves.md)
- 上游实现 [effects/spotlight-sweep-moves](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/demos/effects/spotlight-sweep-moves)
- 授权 Apache-2.0，可改可用，见 [`../../../LICENSE`](../../../LICENSE) 与 [`../../../NOTICE.md`](../../../NOTICE.md)
