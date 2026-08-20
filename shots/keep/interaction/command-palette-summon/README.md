# command-palette-summon

**交互与功能演示**

命令面板降临——整屏压暗加模糊，⌘K 面板带过冲弹落，候选行错峰浮现，敲字列表实时收窄

- **适用** 效率型产品的"全产品在一个输入框里"叙事；命令面板/搜索/快捷键功能的标志性登场
- **时长** 4–5s
- **能量** 中（仪式感型，弹落帧与收窄是两个小打击点）

## 我的判断

| 变体 | 判断 | 分数 | 预览 |
|---|---|---:|---|
| `command-palette-summon` | keep | 4 | [看片](https://vincentwei1021.github.io/video-shotcraft/media/command-palette-summon.mp4) |

## 意图

Raycast/Linear 发布片的标志性仪式：一声轻响，整个 UI 世界压暗
让路，⌘K 面板从中心上方弹落，候选列表错峰浮现；敲两个字母，
列表实时收窄——"你要的一切都在这个输入框里"。模拟交互按真人
操作速度走（R3），收窄的"挤压感"来自行高塌缩而非淡出。

## 参数表

| 参数 | 典型值 | 调节手感 |
|------|--------|----------|
| 压暗 | 亮度 45% + blur 10px，10f | 压不够面板不突出；全黑失去上下文 |
| 弹落 | 起点上方 20px，overshoot 一拍回正 | 无过冲读作淡入，仪式感没了 |
| 候选错峰 | 4f/行 | 同帧出读作贴图 |
| 收窄 | height→0 + overflow hidden 塌缩 | 淡出收窄没有"挤压"感；塌缩完必须卸载 |
| 光标 | 闪烁周期 16f；定格后强制常亮 | 闪到结尾就永不真静止（demo 判例） |

## 已知坑

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
  首次实战须以真实素材回验
- 输入节奏按真人打字速度（R3 判例），两键间隔 ≥12f
- 组合款见 theme-switch-moves B 式（面板收缩成点引发主题涟漪）
- 实战候选行放真实功能名——这是功能清单的天然展位（P4 映射）
- 声音：唤出一声轻响（非游戏音），按键 2 声键帽拟音，
  高亮一声轻 pop（S1/S4 同源）

## 出处

- 参数卡原文 [command-palette-summon.md](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/references/shots/interaction/command-palette-summon.md)
- 上游实现 [interaction/command-palette-summon](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/demos/interaction/command-palette-summon)
- 授权 Apache-2.0，可改可用，见 [`../../../LICENSE`](../../../LICENSE) 与 [`../../../NOTICE.md`](../../../NOTICE.md)
