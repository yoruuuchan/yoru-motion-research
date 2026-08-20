# odometer-digit-roll

**数据与指标**

里程表数字滚动大字报——全屏巨号指标每个数位像老虎机滚轮独立纵向滚动带残影，从左到右逐位过冲停稳，全部锁定瞬间整体加深脉冲

- **适用** 单个王牌指标的全屏亮相（"10x"/"99.98%"级）；与 impact-feedback B 式（伤害数字弹出）分工——那是元素级配菜，这是全屏级主菜
- **时长** 滚动+逐位锁定 ~63f + 脉冲 8f + hold ≥45f，约 5s
- **能量** 中高

## 我的判断

| 变体 | 判断 | 分数 | 预览 |
|---|---|---:|---|
| `odometer-digit-roll` | keep |  | [看片](https://vincentwei1021.github.io/video-shotcraft/media/odometer-digit-roll.mp4) |

## 意图

王牌数字的登场库内有"砸"（score-slam）和"弹"（damage-number），
都是位移系。本卡是**机械系**：数字不是飞进来的，是"算出来的"——
每位一条 0–9 滚轮高速转动，从左到右逐位减速、过冲半格、咔哒锁定，
Vercel Ship/Stripe Sessions 指标段的标准语法。滚动过程自带悬念
（它会停在几？），逐位锁定自带节奏（哒、哒、哒、哒），比直接显示
终值多一整拍的期待感。与 VerticalTicker（backlog 待选）的区别：
有终值、逐位停稳，不是无限滚动墙。

## 参数表

| 参数 | 典型值 | 调节手感 |
|------|--------|----------|
| 字号/字体 | 190px fw800 + fontVariantNumeric: tabular-nums | 非等宽数字每滚一格整行抖动（同 scramble 等宽判例） |
| 错峰 | 20+i×7f 起停，从左到右 | 从右往左停读作倒着算；同时停失去"哒哒哒" |
| 过冲 | +0.5 行再 6f 弹回 | 无过冲读作滑到即停，机械感减半 |
| 残影 | 2 副本 0.25/0.12，速度门控 | 3+ 副本高速下糊成一条（行高小于卡片场景） |
| 终值脉冲 | 加深 + 1.035 缩放 8f | 只加深不缩放在 190px 黑字上不可感（实渲加码） |
| 收尾 | 脉冲归零后真静止 ≥45f | R1 |

## 已知坑

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
  首次实战须以真实素材回验
- 数位 ≤6（含小数点前后）——每多一位多 7f 错峰，8 位滚完 >2.5s
  观众等不起；大数换缩写（12.4M 不是 12,400,000）
- 与 impact-feedback B（伤害数字）同片可共存但分工要清：全屏主菜
  一次（本卡），卡片配菜多次（B 式）——两处都全屏就是两次主菜
- 滚动的数字必须是**真值的各位**——终值 99.98 就滚 9/9/9/8，
  中途乱数会被暂停党抓到"假滚动"
- 声音强依赖候选位：逐位锁定"哒"×N + 终值确认一声低音
  （sound-design §4.5），无声版成立但少一半爽感

## 出处

- 参数卡原文 [odometer-digit-roll.md](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/references/shots/data/odometer-digit-roll.md)
- 上游实现 [data/odometer-digit-roll](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/demos/data/odometer-digit-roll)
- 授权 Apache-2.0，可改可用，见 [`../../../LICENSE`](../../../LICENSE) 与 [`../../../NOTICE.md`](../../../NOTICE.md)
