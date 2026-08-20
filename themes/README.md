# Themes — 设计系统交叉

你在 `D:\DESIGN` 有八套设计系统。这个目录回答一个问题：

> 我要用「昆仑」的样子做一条片子，库里哪些镜头能用、哪些用了就不像昆仑了？

一套一个文件，八个文件长得一模一样，所以可以横着比。

---

## 八套一览

| | 一句话 | 明暗 | 质感 | accent | 动效 token |
|---|---|---|---|---|---|
| [青空 Aozora](aozora.md) | 夏日天空、液态玻璃、清透蓝白 | 浅 | `glass` | `#0A84FF` | 有，5 档 |
| [昆仑 KUNLUN](kunlun.md) | 军工终端、切角青光、全等宽大写 | 深 | 都不是，见下 | `#00b8ff` | 有，5 档 |
| [真夜中 Mayonaka](mayonaka.md) | 深夜蒸汽波电台、霓虹像素故障 | 深 | `brutalist` | `#ff2bd6` | 有，3 档 |
| [PAPER](paper.md) | 独立摄影杂志、暖纸炭灰、锈红印章 | 浅 ×2 + 深 | `hairline`（圆角改 0） | `#B8543A` | 有，但见下 |
| [RIFT](rift.md) | 冷色赛博玻璃、蓝光色差边缘 | 双套 | `glass`（边框改 1px） | `#5C7BFF` | 有，3 档 |
| [YORU Content](yoru-content.md) | 铅字房、宋体、文武线、月相报头 | 浅 | `hairline`（圆角改 2） | `#3186FF` | **没有** |
| [core](core.md) | weirdcore / 池核 / 后室 / Y2K 千禧 | 浅 | `brutalist` | `#009de0` | 有，5 档 |
| [Console](console.md) | 软瓷 AI 伴侣控制台、柔影新拟态 | 双套 | `glass` | `#4F6CE8` | 有，3 档 |

八套里六套的 accent 是蓝的。真正跳出来的只有真夜中的品红和 PAPER 的锈红——
想让两条片子一眼看出不是同一套，从这两套里挑。

---

## 怎么用：两步

### 第一步 · 版式直接查你自己投过的票

版式库那 41 个 keep 本来就是**按皮肤**记的（`brutalist` / `glass` / `dark` / `minimal`…）。
也就是说，每个版式该配什么质感，你当初看片的时候已经投过票了，不用重新判断：

```bash
# 想要 glass 系（青空 / RIFT / Console）能用哪些版式
grep glass ../data/layout-keeps.tsv
```

| 设计系统 | 查这个皮肤 | 有几个版式 |
|---|---|---|
| 青空 · RIFT · Console | `glass` | 7 |
| core · 真夜中 | `brutalist` | 8 |
| PAPER · YORU Content | `default` | 10 |
| 昆仑 · 真夜中 · RIFT深 · Console深 | `dark` | 9 |

> **两套皮肤词汇会撞车，注意别查错。** 版式库用的是 Locomotion 的叫法
> （`default` / `dark` / `brutalist` / `glass` / `minimal` / `neo` / `rounded`），
> 上面那张八套一览表用的是另一套（`hairline` / `brutalist` / `glass` / `flat`）。
> 只有 `brutalist` 和 `glass` 两个词在两边是同一个意思。对照关系：
> `hairline` = `default`，`flat` = `minimal`（出处 `yoru-motion-system/src/themes/skins.ts:8`）。
> 所以 PAPER 和 YORU Content 是 `hairline`，查版式的时候要查 `default`，不是 `minimal`。

**换风格最保险的版式**（你在多套皮肤下都留了的，换设计系统不用重新看片）：

- `appointment-booking` — 5 套皮肤全留
- `changelog`、`bar-chart-reveal` — 各 4 套
- `patient-journey`、`countdown-timer`、`before-after` — 各 3 套

反过来 `bento-grid`、`social-post`、`modal-explainer` 这些只在一套皮肤下过关，
换个设计系统就得回去重新看片。

### 第二步 · 镜头按「结构性禁令」筛

每套系统的 `## 不适合的镜头` 那一节列了它受不了什么。其中有几条能直接对上
[`../data/shot-traits.tsv`](../data/shot-traits.tsv)——那张表是**从 185 个 `.tsx` 里 grep 出来的**，
不是看片的印象。

| 设计系统 | 它禁的结构性手法 | 101 条有代码的 keep 里还剩 |
|---|---|---|
| 青空 | （没有）它自己的曲线就是弹簧 | **101** |
| 昆仑 | 弹簧 | **78** |
| RIFT | 弹簧 | **78** |
| Console | 弹簧、3D | **55** |
| 真夜中 | 弹簧、模糊 | **41** |
| core | 弹簧、模糊、3D | **33** |
| YORU Content | 弹簧、模糊、3D | **33** |
| PAPER | 弹簧、模糊、3D，**而且见下** | **33** |

```bash
# 昆仑能用哪些（禁弹簧）
awk -F'\t' '$1=="keep" && $4 !~ /spring/ {print $2"/"$3}' ../data/shot-traits.tsv
```

**PAPER 要单独说一句。** 它不只是禁某几种手法——`readme.md:103,105` 写着
「没有入场动画」「Nothing scales」。而这个镜头库整个就是入场和缩放。所以上表那个 33
是虚的：真按 PAPER 的规矩，能直接用的接近于零。它适合做**静帧版式**，不适合做动效。
这不是坏消息，是省你半天时间。

---

## 那张手法表为什么分两类

一开始我把八种手法一视同仁地当排除项，算出来昆仑只剩 10 条、core 只剩 6 条。
这个数字是错的——它把「改一个值」和「重写这条镜头」混为一谈了：

**结构性（改不掉）** — 长在动作概念里，禁了等于要重写

| 手法 | keep 里有多少 |
|---|---|
| 弹簧回弹 | 23 |
| 模糊虚焦 | 44 |
| 3D 相机 | 26 |
| 混合模式 | 4 |

**表面（改一个值就完事）** — 系统禁了只意味着「记得改」，不是「不能用」

| 手法 | keep 里有多少 |
|---|---|
| 圆角 | 87 |
| 渐变 | 52 |
| 辉光 | 20 |
| 色相编码 | 12 |

比如昆仑禁圆角（它用切角）——87 条带圆角的镜头**照样能用**，把 `borderRadius`
换成 `clip-path` 切角就行。但昆仑禁弹簧，那 23 条弹簧镜头就是真的不能用，
因为把弹簧改成 steps 之后它已经不是那条镜头了。

**这张表只是初筛，不是判决。** 它只认识这八种手法。各家 `## 不适合的镜头` 里还有
「频闪黑帧」「暖色调实拍」「emoji 装饰」「大写标签」这些——机器看不出来，得你自己读。

还有 **13 条一种手法都不沾**（纯位移+缩放），配哪套都不打架，可以当安全牌：

```bash
awk -F'\t' '$4==""{print $1" "$2"/"$3}' ../data/shot-traits.tsv
```

---

## 三个缺口

**1 · 昆仑没有对应的质感。** 它的招牌是**切角**（`clip-path` 斜切掉四角），
而现有四种质感只有圆角（14/18px）和直角（0）两种，没有切角这个概念。
昆仑实质上需要第五种。现在文件里按 `brutalist` 记，但那是最接近，不是对上了。

**2 · YORU Content 没有动效规范。** 内容层是零动效的印刷物，只有工具台有一档
0.12s 线性。拿它做片子的话，节奏得从别处借——借哪里、按什么规矩借，还没定。

**3 · `yoruDark` 的配色是错的，要修。** `yoru-motion-system` 里现有的那套暗色：

- `bg: #12171C` 在设计系统里**根本没有出处**，是当时推的。真正的暗底是 `#111827`
- `inkMuted` 在暗底上只有约 5.5:1，`inkFaint` 约 2.5:1——都达不到可读对比度
- `surface` 和 `lineStrong` 撞成了同一个值
- `yoruLight` 的 ramp 前两阶也是插值出来的，不是 token 值

逐项对照表在 [`yoru-content.md`](yoru-content.md) 的「和已有 yoruLight / yoruDark 的差异」一节。

---

## 这些文件是怎么来的

八个子代理各读一套，规矩是**每个色值、每个时长都要写出处**（`tokens/colors.css:23` 这种），
没有对应 token 的角色必须标「这是决定不是测量」并说明依据。所以你翻到任何一个数字，
都能顺着找回 `D:\DESIGN` 里的那一行。

这条规矩当场就抓到一个问题：**PAPER 的 `motion.css` 没有被 `styles.css` 导入**——
是个死文件。照着它抄动效数字会全错，真正生效的在 `space.css`，数值不一样。

两张索引表由 [`../scripts/build-trait-index.py`](../scripts/build-trait-index.py) 生成。
**改脚本，不要改 `.tsv`。**
