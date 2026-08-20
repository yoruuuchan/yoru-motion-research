# marker-underline-title

**文字与字卡**

大标题落定后，关键词下方马克笔下划线从左到右快速描画——变宽笔形、毛糙边缘、微上斜跟随斜体字势，贴着字底

- **适用** 标题里强调单个关键词（new/free/AI…）；手写感/人味的品牌调性；正文标注式强调
- **时长** 标题落定 +4~8f 后起笔，划线 8–12f，总 1–1.5s
- **能量** 低（一笔点睛，不抢标题的戏）

## 我的判断

| 变体 | 判断 | 分数 | 预览 |
|---|---|---:|---|
| `marker-underline-title` | maybe |  | [看片](https://vincentwei1021.github.io/video-shotcraft/media/marker-underline-title.mp4) |

## 意图

打印体标题里突然出现一笔手绘马克笔，用材质反差把一个词从
排版里拎出来——像人拿笔在海报上圈重点。命门有三：**快**
（8–12f 一笔呵成，慢了读作加载条）、**近**（贴着字底，离远了
读作分隔线不是强调）、**跟字势**（斜体词的划线必须左低右高
微上斜——斜向画反是最容易犯且一眼假的错，判例见已知坑）。

## 参数表

| 参数 | 典型值 | 调节手感 |
|------|--------|----------|
| 划线时长 | 10f（原片实测节奏；14f 版被裁偏慢） | >14f 读作进度条；<6f 看不见笔迹方向 |
| 字底距离 | ≈-0.1em（从 -40 收到 -20@1080p 才贴住字势） | 离远读作分隔线；碰到字底降部又乱 |
| 斜向 | 左低右高微上斜（跟斜体） | **画反（左高右低）一眼假**——返工判例 |
| 笔宽 | 中段 ~0.12em，首尾 ~0.6x | 等宽读作机器线；差异>2x 读作书法 |
| 毛糙度 | 边缘轻噪声 | 太糙读作故障；全平滑读作 CSS border |

## 已知坑

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
  首次实战须以真实素材回验
- 与 draw-svg-trace 撞领域（有意单列为两卡）：那张是通用
  SVG 描画（图标/插画/任意线稿）；本卡专做**文字强调**的马克笔
  质感（变宽+毛糙+跟字势），做图形描画去用那张
- 斜向判例：v1 左高右低被比对环节抓出——划线斜向必须跟字势，
  正体字则水平微抖
- 残余差距：原片（notion-ai）笔头飞白颗粒感更细碎，实战可加
  更细的笔刷噪点

## 出处

- 参数卡原文 [marker-underline-title.md](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/references/shots/typography/marker-underline-title.md)
- 上游实现 [typography/marker-underline-title](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/demos/typography/marker-underline-title)
- 授权 Apache-2.0，可改可用，见 [`../../../LICENSE`](../../../LICENSE) 与 [`../../../NOTICE.md`](../../../NOTICE.md)
