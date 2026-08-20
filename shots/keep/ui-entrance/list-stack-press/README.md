# list-stack-press

**界面登场与陈列**

列表卡从画面底部逐张飞上摞起，每张落地压弹整摞、计数器同步跳一格

- **适用** feed/雷达/收件箱类"每天有新东西"的镜头；强调持续积累的资产列表
- **时长** 约 3s（18–88f）
- **能量** 中

## 我的判断

| 变体 | 判断 | 分数 | 预览 |
|---|---|---:|---|
| `list-stack-press` | keep |  | [看片](https://vincentwei1021.github.io/video-shotcraft/media/list-stack-press.mp4) |

## 意图

"堆叠有重量"：每张新卡落上来，已落定的整摞被压下再弹回——观众从物理反馈里读出"这是实打实攒下来的东西"。计数器同步跳格把数量感钉死。

## 参数表

| 参数 | 典型值 | 调节手感 |
|------|--------|----------|
| 节拍 | CUES=[18,30,42,54,66]（12f 等距），每张飞 22f，bezier(0.45,0.05,0.25,1.12) 末端过冲 | 少量卡（5 张）可以等距；大批量入场才需要递加速（对照 deck-deal 的 R2） |
| 入场 | 从下方 600px 升入，交替 ±2° tilt 收平，scale 1.06→1 | 交替倾斜打破对称；同向倾斜读作复制粘贴 |
| 堆叠压感 | 后一张到场时整摞压下 6px、8f 弹回（脉冲 [cue,cue+4,cue+8]→[0,6,0]） | 这是"有重量"的关键一笔，砍掉后堆叠变成简单排版 |
| 阴影 | 空中 `0 32px 64px`、落定 `0 2px 8px` | 阴影随高度收敛，和 deck-deal/spotlight 同一套语言 |
| 联动高亮 | 落地后滞后 2–4f 于 72% 高度处长出 40% 宽强调色（模板片为琥珀）底色（7f 长 + 5f 淡）；最后一张离切点仅 ~12f 需压缩节拍 | 高亮是次级动作（法则 5/8）：在主动作（落地压弹）之后跟进，不与之同帧抢戏；末尾元素的节拍要按剩余帧预算压缩，不能照抄前面的 |
| glaze 扫光 | 420px 宽、rotate 14°、mixBlendMode overlay，帧 82→96 从 −700 扫到 2600 | 扫光全镜头只此一次、扫整摞不逐卡（Q4） |
| 计数器（digit-roll 手法） | DigitRoll 以 landedCount 为 key 强制重滚，落一张跳一格；每位 delay=i·4、22f 滚定，bezier(0.25,0.8,0.25,1)；滚动量=(10+target)·lineH 先滚过完整一条 0-9 带再落位 | 计数与落地不同步立刻穿帮，key 重滚最省事；"转过一圈"保证任何目标位都有滚感；数字带双份拼接+overflow hidden+tabular-nums（不开 tabular 会横向抖）；滚动必须在所属画面淡出前落定（曾专修过此时点） |
| 相机 | zoom 1.35→0.9 五键跟随堆叠向下 | 正视机位（见已知坑），相机只做纵向跟随 |

## 已知坑

- 堆叠/列表信息镜头必须正视（Q6）——全片倾斜化时本镜头曾被单独回滚回正视；风格化机位逐镜头验证，不全局套用
- 逐卡 glint 高亮扫过被否两次（Q4），高亮用静态强调色底色条即可，动感交给压弹
- 与 history-list-stack（document-typewriter-reveal 卡尾段）是同一动作词汇——全片同一手法只当一次主角（P4），两处并用时一处必须降为配角
- anticipation/拖拽层级参数借鉴自迪士尼 12 法则（pixel2motion skill 内置提炼版），非用户判例——是默认建议不是令；与判例冲突时判例优先
- 预备动作幅度必须过肉眼阈值（deck-deal 判例 2026-07-09：小幅度用户完全无感，放大 12 倍才通过）——渲染后自查"不逐帧能否看出蓄力"

## 出处

- 参数卡原文 [list-stack-press.md](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/references/shots/ui-entrance/list-stack-press.md)
- 上游实现 [ui-entrance/list-stack-press](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/demos/ui-entrance/list-stack-press)
- 授权 Apache-2.0，可改可用，见 [`../../../LICENSE`](../../../LICENSE) 与 [`../../../NOTICE.md`](../../../NOTICE.md)
