# avatar-grid-radial-build-colorize

**数据与指标**

8×7 小卡片网格由中心分环生长铺满（内容混合首字母/图标/图片占位），随后约 15% 的卡片随机时刻染红标异常，标题图例常驻中央

- **适用** "群体中浮现异常/重点"的数据叙事：用户群健康度、监控面板、批量状态总览
- **时长** 约 5.6s（168f@30fps；铺满 0.5–1.7s · 染色 1.7–3.4s 陆续浮现）
- **能量** 中（生长段有节奏感，染色段是安静的"发现"时刻）

## 我的判断

| 变体 | 判断 | 分数 | 预览 |
|---|---|---:|---|
| `avatar-grid-radial-build-colorize` | maybe |  | [看片](https://vincentwei1021.github.io/video-shotcraft/media/avatar-grid-radial-build-colorize.mp4) |

## 意图

两幕结构：第一幕"群体成形"——卡片从中心一环环长出，像镜头下的菌落生长；第二幕"异常浮现"——铺满后个别卡片陆续变红，观众的眼睛被迫扫描全场找红点。它把"我们帮你盯着所有项"这句话拍成了体验。

## 参数表

| 参数 | 典型值 | 调节手感 |
|------|--------|----------|
| 生长速度 | 每 4 帧一环 + 3 帧抖动，1.2s 铺满 | 快于 3 帧/环读作"闪现"；抖动砍掉后波前整齐得像机器 |
| 异常比例 | 15% | <8% 观众可能漏看；>25% "异常"变"普遍"，叙事反转 |
| 染色窗口 | 每张 0.036，散布在 0.30–0.60 | 全部同拍染色是警报不是浮现；散布区间越长"陆续发现"感越强 |
| 状态色 | 绿 #37C46B → 红 #F0453A（点），底 #FDECEC | 功能色不随品牌换；底色染红别深过 #F8D8D8，卡片文字要仍可读 |
| 网格规模 | 8×7 − 中央 18 格 = 38 张可见 | 更大网格需同步缩 gap 和字号；中央留空区随标题长度调 |
| 内容混合比 | 首字母/图标/图片 各 1/3（rand 均分） | 全换成同类（如全头像）也成立；混合版本更像"多类型资产"场景 |

## 已知坑

- 中央留空用 `visibility:hidden` 而不是不渲染——删格子会让分环计算的环心偏移，生长波变形
- 染色的三个通道（底/描边/点）必须同一条 cT 曲线驱动，分开会出现"点红了底还白"的中间态
- 图片占位是 CSS 渐变色块，换真实图片时保留 `overflow:hidden` 和 border-radius 继承，注意深色图上状态点要加白描边
- 标题/图例 z-index 在卡片之上但无底板，若换更密的网格需给中央区加半透明底垫保证可读

## 出处

- 参数卡原文 [avatar-grid-radial-build-colorize.md](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/references/shots/data/avatar-grid-radial-build-colorize.md)
- 上游实现 [data/avatar-grid-radial-build-colorize](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/demos/data/avatar-grid-radial-build-colorize)
- 授权 Apache-2.0，可改可用，见 [`../../../LICENSE`](../../../LICENSE) 与 [`../../../NOTICE.md`](../../../NOTICE.md)
