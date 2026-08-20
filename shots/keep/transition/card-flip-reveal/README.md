# card-flip-reveal

**转场**

功能卡 3D 翻面揭示——卡片沿 Y 轴翻 180°，正面 UI 翻到侧棱最薄处闪过一道随角度移动的高光带，背面揭出大号结论数字，逐张错峰扫过整排

- **适用** "功能→成果"的成对叙事：一排功能卡逐张翻出各自的指标/结论；元素级转场卡
- **时长** 单卡翻转 26f，三卡错峰 10f，全程 ~4.9s（含 hold）
- **能量** 中高

## 我的判断

| 变体 | 判断 | 分数 | 预览 |
|---|---|---:|---|
| `card-flip-reveal` | keep | 4 | [看片](https://vincentwei1021.github.io/video-shotcraft/media/card-flip-reveal.mp4) |

## 意图

库内"翻"字辈已有 wall-reveal-moves B（整墙波浪翻面，讲入场）和
split-flap（字符翻牌，讲文字）。本卡是**语义翻面**：一张卡的正反两面
是一对因果——正面是功能界面，背面是它带来的数字结论。翻面动作本身
就是"所以呢？"的回答，Apple bento 段落的标准语法。逐张错峰 10f 扫过
一排，三张卡三个数字节奏读作"成果连报"。

## 参数表

| 参数 | 典型值 | 调节手感 |
|------|--------|----------|
| 翻转时长 | 18f + 8f 回弹 | <14f 看不到侧棱瞬间；>28f 读作慢慢转 |
| 过冲 | 192°→180°（12°） | 无过冲落定读作生硬停表 |
| 高光峰值 | 0.32 加深灰 @90° | 峰值错开 90° 读作贴图错误 |
| 错峰 | 10f/卡，≤4 卡 | 同时翻读作整墙翻面（那是 wall-reveal B 的活）|
| 背面内容 | 大号数字（90px 级）+ 一行小标签 | 背面塞完整 UI 读不完——翻面后只有一拍注意力 |
| 收尾 | 末卡落定真静止 ≥40f | R1 |

## 已知坑

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
  首次实战须以真实素材回验
- 与 wall-reveal-moves B 式（网格波浪翻面）同技术根不同语义：那是
  入场（背面灰卡→正面 UI），这是揭示（正面 UI→背面结论）——同片
  两者都用时翻转方向要区分（入场 rotateX、揭示 rotateY）
- 正反两面必须语义成对（界面→它的成果）；翻出无关内容，翻面就
  只是花哨的换图
- 真实素材正面用截图时注意 backface 渲染开销，三卡以上分 Sequence
- 声音候选位：每卡翻停帧一声轻"啪"（sound-design §4.5），三连啪
  节奏感翻倍

## 出处

- 参数卡原文 [card-flip-reveal.md](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/references/shots/transition/card-flip-reveal.md)
- 上游实现 [transition/card-flip-reveal](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/demos/transition/card-flip-reveal)
- 授权 Apache-2.0，可改可用，见 [`../../../LICENSE`](../../../LICENSE) 与 [`../../../NOTICE.md`](../../../NOTICE.md)
