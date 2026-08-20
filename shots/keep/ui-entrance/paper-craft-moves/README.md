# paper-craft-moves

**界面登场与陈列**

纸艺两式——masking-tape-slap 纸胶带拍定（悬浮微晃被"啪啪"按死）与 popup-book-rise 立体书立起（卡片沿底边错峰立墙）

- **适用** 纸墨主视觉片的实体材料语言：单卡定妆入场用 A、整版 dashboard 开场建立用 B；与纸墨+强调色的主视觉（模板片为纸/墨/琥珀）天然同源
- **时长** A 3–4s / B 4–5.5s
- **能量** A 中（两拍打击）/ B 中高（立墙有纵深冲击）

## 我的判断

| 变体 | 判断 | 分数 | 预览 |
|---|---|---:|---|
| `masking-tape-slap` | keep |  | [看片](https://vincentwei1021.github.io/video-shotcraft/media/masking-tape-slap.mp4) |
| `popup-book-rise` | keep |  | [看片](https://vincentwei1021.github.io/video-shotcraft/media/popup-book-rise.mp4) |

## 意图

Wes Anderson 手账美术与立体书纸艺的 UI 翻译。A：卡片轻飘入位后
悬着微晃（未固定的纸），两条撕边半透明胶带"啪、啪"先后拍在对角，
第二条拍下**同帧**卡片停晃、投影变薄、整卡下沉——"按死"的定妆
一瞬是主角，两声"啪"是天然音效点。B：整页平躺如摊开书页（俯视），
卡片像贴在页上的纸片沿各自底边错峰立起成墙，立到 95° 回弹 90°
（纸的韧性），根部投影随立起收窄。

## 参数表

| 参数 | 典型值 | 调节手感 |
|------|--------|----------|
| A 按死三件套 | 同帧：晃动 2f 归零 + 投影 34px→8px + 全卡下沉 2px | 三件拆帧就没有"按死"感；第一条胶带只把包络衰到 0.45（半死） |
| A 胶带质感 | 半透明 + 锯齿撕边 + 落点故意歪 2–3° | 歪斜是设计的手工感；直挺挺读作 UI 元素 |
| B 立起方向 | rotateX 0→**-90°**（向观众立起） | demo 判例：方向写反卡片往画面里倒被底板裁切 |
| B 根部投影 | blur 矩形不随卡立起，高 104→14px、透明度 0.26→0.1 随角度插值 | 无投影纸片浮空；投影跟着立起来穿帮 |
| B 收尾 | 全部站定后场景 75°→68° 轻回正（in-out cubic） | 直接定住少一口呼吸 |

## 已知坑

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
  首次实战须以真实素材回验
- A 的晃动是"未固定"的叙事铺垫不是手持抖动（Q3 边界）：
  振幅包络必须最终归零，全片只在被按死前存在
- B 与 tilt-reveal 分工：tilt 是**机位**抬头看静止页面，
  本卡机位基本不动、**构件自己**站起来
- B 立墙后卡片呈 90° 侧立态，文字不可读——立墙是构图动作，
  信息交给立起后的正视段落（Q6 同源）
- 声音：A 两声"啪"（纸拍击拟音）；B 每排立起一声轻纸响，
  错峰对齐（S2/S4 同源）

## 出处

- 参数卡原文 [paper-craft-moves.md](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/references/shots/ui-entrance/paper-craft-moves.md)
- 上游实现 [ui-entrance/paper-craft-moves](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/demos/ui-entrance/paper-craft-moves)
- 授权 Apache-2.0，可改可用，见 [`../../../LICENSE`](../../../LICENSE) 与 [`../../../NOTICE.md`](../../../NOTICE.md)
