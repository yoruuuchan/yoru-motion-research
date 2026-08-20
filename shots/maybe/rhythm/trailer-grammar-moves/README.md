# trailer-grammar-moves

**节奏与蒙太奇**

预告片语法三式——trailer-bumper 前置速剪钩子、card-footage-cadence 字卡穿插对话、smash-cut 猛切入定

- **适用** 预告片的三个结构性时刻：开场怎么钩（A）、中段怎么对话（B）、高潮怎么收（C）；三式合用即一支预告片的骨架
- **时长** A ~4.7s / B ~5s / C ~4.5s
- **能量** A 高 / B 中 / C 高

## 我的判断

| 变体 | 判断 | 分数 | 预览 |
|---|---|---:|---|
| `card-footage-cadence` | maybe |  | [看片](https://vincentwei1021.github.io/video-shotcraft/media/card-footage-cadence.mp4) |
| `trailer-bumper` | maybe |  | [看片](https://vincentwei1021.github.io/video-shotcraft/media/trailer-bumper.mp4) |

## 意图

库内节奏卡各管一段：beat-cut 管切点排布、montage-rhythm 管段落呼吸、
rhythm-interrupt 管打断。本卡管**预告片的结构性时刻**——不是某个
镜头怎么动，是整片的三个关节怎么接：A 是开场钩——正片前 0.9 秒塞
三个最抓眼镜头速剪 + 黑场静默一拍再开场，预告片的"预告"；B 是中段
对话——UI 镜头与黑底短语卡互相接拍交替硬切，画面与文字都踩拍点，
第三幕结构；C 是高潮句号——满屏动势轰鸣最高潮一帧硬切成整齐静止
全景死寂，喧闹→死寂。三式合用即一支预告片的骨架。

## 参数表

| 参数 | 典型值 | 调节手感 |
|------|--------|----------|
| A 速剪 | 三镜等长 9f，零过渡；镜头 3 用 origin 58%/40% 放大 2.2x 怼脸特写 | 节拍感靠等长；三镜构图必须明显不同 |
| A 微推 | 每镜内部 scale 1→1.04 线性 | 静帧三连读作幻灯片——命门 |
| A 黑场 | 27–33f 纯黑 #000 空 div，6f | 黑场里放任何东西都毁掉"静默一拍" |
| B 交替 | UI 段 12f 级 ↔ 字卡 8f 级硬切，条件挂载分段=天然零过渡 | 段长可变但要读出"接拍"感 |
| B 字卡 | 黑底白字居中，落定 1.05→1 out-cubic 5f 内完成，其余全静 | 字卡的静 ↔ UI 段的动，质感对比即节奏 |
| C 切点 | 42f 一帧完成全部反差；切前 3f 动势仍在加速 | 绝不减速迎接切点——命门 |
| C 模糊 | 飞卡 blur = 1+4p（p∝瞬时速度），背景恒 1.5px 衬前景 | 速度门控：快才糊，不是全程糊 |
| 收尾 | A 静止 91f / B 45f / C 93f（≥40f） | C 死寂段直接 return 无动画子树，帧函数级真静止 |

## 已知坑

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
  首次实战须以真实素材回验
- A 黑场必须纯黑无物（drop-blackout 判例同族）——黑场是喘息，
  不是又一张字卡
- B 与 cel-flash-stomp/beat-cut 字卡段的分工：那些是字在表演
  （字自己是主角），这是字与画对话（互相接拍）——别混用
- C 死寂段绝对真静止、音乐同帧骤停——声音强依赖，无声版的 smash cut
  只剩一半（sound-design §4.5）；A 三连切每切一声打点、黑场全消音
- C 与 drop-blackout-slam 的区别：那是黑场蓄力再爆（静→爆），
  这是爆完瞬间入定（爆→静）——方向相反，别接错位置

## 出处

- 参数卡原文 [trailer-grammar-moves.md](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/references/shots/rhythm/trailer-grammar-moves.md)
- 上游实现 [rhythm/trailer-grammar-moves](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/demos/rhythm/trailer-grammar-moves)
- 授权 Apache-2.0，可改可用，见 [`../../../LICENSE`](../../../LICENSE) 与 [`../../../NOTICE.md`](../../../NOTICE.md)
