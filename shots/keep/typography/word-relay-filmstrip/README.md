# word-relay-filmstrip

**文字与字卡**

左列黑白相间等高页面卡步进滚动、右侧衬线大词原位接力（名词恒定+动词轮换）——切词瞬间才滚动一格，词块垂直中心与当前页面卡中点精确对齐

- **适用** "一个主体 × 多种能力"的枚举段（Computer researches/builds/codes…）；作品集/案例流展示；产品多场景巡礼
- **时长** 每词期 ~1.5–2s × 3–4 词；全段 5–7s
- **能量** 中低（编辑部气质，节奏靠切词的"咔哒"感）

## 我的判断

| 变体 | 判断 | 分数 | 预览 |
|---|---|---:|---|
| `word-relay-filmstrip` | keep |  | [看片](https://vincentwei1021.github.io/video-shotcraft/media/word-relay-filmstrip.mp4) |

## 意图

左边是证据（页面截图胶片），右边是论点（大词）：动词换一次，
胶片就步进一格给出新证据——文字与画面互为注脚。命门是**步进制**：
左列平时完全静止，只在切词瞬间滚动一格（滚动=换证据的机械动作），
持续滚动会让左列沦为背景装饰、切词失去"咔哒"感。第二命门是
**对齐**：大词块垂直中心必须与当前页面卡中点精确对齐（像素级），
歪了整个版式的"编辑部严谨感"就塌了。

## 参数表

| 参数 | 典型值 | 调节手感 |
|------|--------|----------|
| 页面卡 | 等高（530px@1080p）、黑白相间、约半屏宽 | 不等高/同色系读不出步进；卡太窄失去"证据"分量 |
| 词期 | ~45–60f/词 | <40f 读不完词+胶片看不清；词期不必均匀 |
| 滚动窗口 | ~12f ease-in-out，恰一卡高 | 持续滚动=命门违例；滚过头/不足读作机械故障 |
| 词接力 | 旧词 4–6f 灰化淡出 → 新词 6–8f 落位 | 同帧交叉必叠影；间隙 >10f 读作断片 |
| 垂直对齐 | 词块中心=当前卡中点（像素级） | 用户单点意见"文字高度和中间的页面中点要对齐"；差 >8px 可感 |
| 字体 | 衬线 Didot 类、动词字重比名词轻或同 | 无衬线会丢"编辑部"气质 |

## 已知坑

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
  首次实战须以真实素材回验
- 与 text-column-converge 分工：那张是左右对峙合拢的揭晓戏；
  本卡是纵向证据流+原位接力，无合拢无揭晓
- 与 pill-slot-cycle 分工：那张是胶囊槽位轮换 UI 元素；
  本卡是版式级的图文对位系统
- 实战素材：页面卡应使用真实截图（demo 为灰条示意，残余差距
  已知）；截图亮度要人工分档保证相间可读

## 出处

- 参数卡原文 [word-relay-filmstrip.md](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/references/shots/typography/word-relay-filmstrip.md)
- 上游实现 [typography/word-relay-filmstrip](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/demos/typography/word-relay-filmstrip)
- 授权 Apache-2.0，可改可用，见 [`../../../LICENSE`](../../../LICENSE) 与 [`../../../NOTICE.md`](../../../NOTICE.md)
