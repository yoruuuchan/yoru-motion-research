# Layouts — 版式库（导航）

Locomotion 的版式模板。**这里没有代码**——上游没有 LICENSE 文件，
授权状态是 `reference_only`（见 [`../legal/license-tracker.yml`](../legal/license-tracker.yml)），
所以只能导航过去，不能把实现搬进来。

链接全部钉在上游 commit [`d42711f`](https://github.com/locomotion-pro/locomotion/tree/d42711f950c2c6776056df4d9c7c729d4490ba50)，上游改动了也不会失效。
「看片」直接在 GitHub 页面里播，不用下载。

- 候选 427 个 = 61 个版式 × 7 套皮肤
- 留下 **41** 个，分布在 **20** 个版式里

> 皮肤只是换色换质感，版式和节奏在 7 套之间是一样的——所以同一个版式下
> 留哪几套皮肤，读的是配色偏好，不是版式偏好。

> 留下的 20 个版式各写了一句描述，是**逐帧看渲染结果**写的——上游源码不能读，
> 所以描述里说的都是画面上看得见的动作，不是代码里的实现。待定和全否的没写。

---

## 留下的版式

### app-feature-callout

浏览器窗弹入 → 窗内内容填好 → 一个深色药丸标签从右侧飞进来贴在窗角。给某个功能点名。

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/app-feature-callout/Composition.tsx)

- **留下** `brutalist` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/app-feature-callout-brutalist.mp4)
- **待定** `default` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/app-feature-callout.mp4), `neo` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/app-feature-callout-neo.mp4)
- 否决 `dark`, `glass`, `minimal`, `rounded`

### appointment-booking

卡片弹入，可选项一条条往下堆出来，最后底部实心按钮压上收口。表单、选时间、任何「选一个再确认」。

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/appointment-booking/Composition.tsx)

- **留下** `brutalist` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/appointment-booking-brutalist.mp4), `dark` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/appointment-booking-dark.mp4), `glass` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/appointment-booking-glass.mp4), `minimal` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/appointment-booking-minimal.mp4), `neo` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/appointment-booking-neo.mp4)
- **待定** `default` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/appointment-booking.mp4), `rounded` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/appointment-booking-rounded.mp4)

### bar-chart-reveal

柱子从左到右一根根长起来，数值跟着柱顶一起冒出来，明度从浅到深。比大小。

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/bar-chart-reveal/Composition.tsx)

- **留下** `brutalist` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/bar-chart-reveal-brutalist.mp4), `dark` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/bar-chart-reveal-dark.mp4), `default` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/bar-chart-reveal.mp4), `glass` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/bar-chart-reveal-glass.mp4)
- **待定** `minimal` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/bar-chart-reveal-minimal.mp4), `neo` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/bar-chart-reveal-neo.mp4)
- 否决 `rounded`

### before-after

左边先把「以前」立起来（✗ 逐条落），中间一个箭头，右边再给「现在」（✓ 逐条落）。对比、改造前后。

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/before-after/Composition.tsx)

- **留下** `dark` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/before-after-dark.mp4), `glass` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/before-after-glass.mp4), `minimal` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/before-after-minimal.mp4)
- **待定** `default` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/before-after.mp4), `rounded` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/before-after-rounded.mp4)
- 否决 `brutalist`, `neo`

### bento-grid

大小交错的格子按顺序一格一格弹进来，每格一个图标一个短标签。能力总览、做过什么。

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/bento-grid/Composition.tsx)

- **留下** `brutalist` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/bento-grid-brutalist.mp4)
- 否决 `dark`, `default`, `glass`, `minimal`, `neo`, `rounded`

### changelog

卡片弹入，更新条目一条条打勾出现，每条底下一根细线。版本更新、这次改了什么。

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/changelog/Composition.tsx)

- **留下** `brutalist` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/changelog-brutalist.mp4), `dark` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/changelog-dark.mp4), `glass` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/changelog-glass.mp4), `neo` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/changelog-neo.mp4)
- **待定** `default` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/changelog.mp4), `minimal` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/changelog-minimal.mp4), `rounded` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/changelog-rounded.mp4)

### concept-breakdown

小眉题 + 大问句标题先立住，要点一条条淡入上浮。解释一个概念。

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/concept-breakdown/Composition.tsx)

- **留下** `brutalist` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/concept-breakdown-brutalist.mp4), `dark` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/concept-breakdown-dark.mp4)
- **待定** `default` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/concept-breakdown.mp4), `minimal` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/concept-breakdown-minimal.mp4), `neo` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/concept-breakdown-neo.mp4), `rounded` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/concept-breakdown-rounded.mp4)
- 否决 `glass`

### countdown-timer

三个数字格持续翻动递减，一路跑到 00 00 00。倒计时、快开始了。

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/countdown-timer/Composition.tsx)

- **留下** `dark` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/countdown-timer-dark.mp4), `default` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/countdown-timer.mp4), `glass` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/countdown-timer-glass.mp4)
- **待定** `brutalist` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/countdown-timer-brutalist.mp4)
- 否决 `minimal`, `neo`, `rounded`

### day-summary

卡片弹入，主数字从 0 滚上去，同时下面的任务条一条条打勾。日报、这段时间做完了什么。

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/day-summary/Composition.tsx)

- **留下** `default` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/day-summary.mp4), `rounded` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/day-summary-rounded.mp4)
- **待定** `brutalist` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/day-summary-brutalist.mp4), `dark` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/day-summary-dark.mp4), `neo` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/day-summary-neo.mp4)
- 否决 `glass`, `minimal`

### feature-showcase

大标题立住不动，三个方框卡从左到右一个个弹入。三点并列、卖点排排站。

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/feature-showcase/Composition.tsx)

- **留下** `brutalist` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/feature-showcase-brutalist.mp4)
- 否决 `dark`, `default`, `glass`, `minimal`, `neo`, `rounded`

### modal-explainer

背景压暗，白卡弹入，卡内按页翻步骤，底下有分页点和一条走着的进度条。分步讲解。

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/modal-explainer/Composition.tsx)

- **留下** `default` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/modal-explainer.mp4)
- 否决 `brutalist`, `dark`, `glass`, `minimal`, `neo`, `rounded`

### patient-journey

一条横线上编号圆点 1→2→3→4 依次亮起，虚线连接，每个点下面挂标签。流程、一段旅程怎么走完。

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/patient-journey/Composition.tsx)

- **留下** `dark` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/patient-journey-dark.mp4), `default` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/patient-journey.mp4), `glass` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/patient-journey-glass.mp4)
- **待定** `minimal` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/patient-journey-minimal.mp4), `rounded` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/patient-journey-rounded.mp4)
- 否决 `brutalist`, `neo`

### payment-flow

三个带编号的小方框横排弹入，之间用短横线连接。紧凑版流程，比 patient-journey 占地小。

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/payment-flow/Composition.tsx)

- **留下** `default` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/payment-flow.mp4)
- 否决 `brutalist`, `dark`, `glass`, `minimal`, `neo`, `rounded`

### portfolio-breakdown

圆环从 12 点方向画出来，右边图例一条条跟上，环上分段由深到浅。占比、时间花在哪。

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/portfolio-breakdown/Composition.tsx)

- **留下** `default` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/portfolio-breakdown.mp4)
- **待定** `dark` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/portfolio-breakdown-dark.mp4), `glass` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/portfolio-breakdown-glass.mp4), `minimal` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/portfolio-breakdown-minimal.mp4), `neo` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/portfolio-breakdown-neo.mp4), `rounded` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/portfolio-breakdown-rounded.mp4)
- 否决 `brutalist`

### product-reveal

商品图卡弹入，名称淡入，价格出现，旁边跟一个划掉的原价。单品、商品。

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/product-reveal/Composition.tsx)

- **留下** `rounded` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/product-reveal-rounded.mp4)
- **待定** `dark` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/product-reveal-dark.mp4), `default` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/product-reveal.mp4)
- 否决 `brutalist`, `glass`, `minimal`, `neo`

### screen-showcase

浏览器窗弹入，窗内内容块一块块填满，右侧编号功能列表一条条出现。产品界面展示。

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/screen-showcase/Composition.tsx)

- **留下** `default` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/screen-showcase.mp4), `minimal` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/screen-showcase-minimal.mp4)
- **待定** `rounded` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/screen-showcase-rounded.mp4)
- 否决 `brutalist`, `dark`, `glass`, `neo`

### social-post

推文卡弹入（头像 + 用户名），正文淡入，底部三个互动数字滚动计数上去。社交截图、口碑。

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/social-post/Composition.tsx)

- **留下** `default` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/social-post.mp4)
- **待定** `glass` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/social-post-glass.mp4), `rounded` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/social-post-rounded.mp4)
- 否决 `brutalist`, `dark`, `minimal`, `neo`

### staggered-words

大字一个词一个词错峰弹入。标题、口号。

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/staggered-words/Composition.tsx)

- **留下** `brutalist` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/staggered-words-brutalist.mp4), `dark` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/staggered-words-dark.mp4)
- **待定** `default` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/staggered-words.mp4), `rounded` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/staggered-words-rounded.mp4)
- 否决 `glass`, `minimal`, `neo`

### step-explainer

标题下步骤逐条出现，每条带 01/02/03 编号和一条从左画到右的下划线。步骤说明。

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/step-explainer/Composition.tsx)

- **留下** `glass` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/step-explainer-glass.mp4)
- **待定** `minimal` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/step-explainer-minimal.mp4)
- 否决 `brutalist`, `dark`, `default`, `neo`, `rounded`

### typewriter-reveal

光标闪着，一个字一个字把句子打出来，打完光标继续闪。打字机标题。

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/typewriter-reveal/Composition.tsx)

- **留下** `dark` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/typewriter-reveal-dark.mp4), `default` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/typewriter-reveal.mp4)
- 否决 `brutalist`, `glass`, `minimal`, `neo`, `rounded`

---

## 待定的版式

没有一套皮肤被留下，但也没有全否——版式本身还没定。

### agenda-reveal

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/agenda-reveal/Composition.tsx)

- **待定** `brutalist` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/agenda-reveal-brutalist.mp4), `dark` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/agenda-reveal-dark.mp4), `default` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/agenda-reveal.mp4), `glass` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/agenda-reveal-glass.mp4), `minimal` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/agenda-reveal-minimal.mp4), `neo` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/agenda-reveal-neo.mp4), `rounded` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/agenda-reveal-rounded.mp4)

### cart-animation

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/cart-animation/Composition.tsx)

- **待定** `brutalist` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/cart-animation-brutalist.mp4), `dark` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/cart-animation-dark.mp4), `default` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/cart-animation.mp4), `glass` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/cart-animation-glass.mp4), `minimal` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/cart-animation-minimal.mp4), `neo` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/cart-animation-neo.mp4), `rounded` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/cart-animation-rounded.mp4)

### collab-card

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/collab-card/Composition.tsx)

- **待定** `default` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/collab-card.mp4)
- 否决 `brutalist`, `dark`, `glass`, `minimal`, `neo`, `rounded`

### discount-countdown

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/discount-countdown/Composition.tsx)

- **待定** `default` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/discount-countdown.mp4)
- 否决 `brutalist`, `dark`, `glass`, `minimal`, `neo`, `rounded`

### drag-drop-demo

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/drag-drop-demo/Composition.tsx)

- **待定** `brutalist` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/drag-drop-demo-brutalist.mp4), `dark` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/drag-drop-demo-dark.mp4), `default` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/drag-drop-demo.mp4), `glass` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/drag-drop-demo-glass.mp4), `neo` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/drag-drop-demo-neo.mp4)
- 否决 `minimal`, `rounded`

### flashcard-flip

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/flashcard-flip/Composition.tsx)

- **待定** `brutalist` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/flashcard-flip-brutalist.mp4), `neo` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/flashcard-flip-neo.mp4)
- 否决 `dark`, `default`, `glass`, `minimal`, `rounded`

### intro-outro

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/intro-outro/Composition.tsx)

- **待定** `brutalist` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/intro-outro-brutalist.mp4), `dark` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/intro-outro-dark.mp4)
- 否决 `default`, `glass`, `minimal`, `neo`, `rounded`

### job-posting

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/job-posting/Composition.tsx)

- **待定** `brutalist` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/job-posting-brutalist.mp4), `default` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/job-posting.mp4)
- 否决 `dark`, `glass`, `minimal`, `neo`, `rounded`

### launch-day

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/launch-day/Composition.tsx)

- **待定** `default` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/launch-day.mp4)
- 否决 `brutalist`, `dark`, `glass`, `minimal`, `neo`, `rounded`

### listing-card

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/listing-card/Composition.tsx)

- **待定** `brutalist` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/listing-card-brutalist.mp4)
- 否决 `dark`, `default`, `glass`, `minimal`, `neo`, `rounded`

### metric-card

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/metric-card/Composition.tsx)

- **待定** `default` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/metric-card.mp4), `glass` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/metric-card-glass.mp4), `minimal` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/metric-card-minimal.mp4), `neo` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/metric-card-neo.mp4), `rounded` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/metric-card-rounded.mp4)
- 否决 `brutalist`, `dark`

### onboarding-flow

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/onboarding-flow/Composition.tsx)

- **待定** `brutalist` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/onboarding-flow-brutalist.mp4), `dark` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/onboarding-flow-dark.mp4), `default` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/onboarding-flow.mp4), `glass` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/onboarding-flow-glass.mp4), `neo` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/onboarding-flow-neo.mp4), `rounded` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/onboarding-flow-rounded.mp4)
- 否决 `minimal`

### pricing-comparison

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/pricing-comparison/Composition.tsx)

- **待定** `brutalist` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/pricing-comparison-brutalist.mp4), `dark` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/pricing-comparison-dark.mp4), `default` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/pricing-comparison.mp4), `glass` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/pricing-comparison-glass.mp4), `minimal` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/pricing-comparison-minimal.mp4), `neo` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/pricing-comparison-neo.mp4), `rounded` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/pricing-comparison-rounded.mp4)

### profile-card

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/profile-card/Composition.tsx)

- **待定** `default` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/profile-card.mp4)
- 否决 `brutalist`, `dark`, `glass`, `minimal`, `neo`, `rounded`

### property-tour

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/property-tour/Composition.tsx)

- **待定** `dark` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/property-tour-dark.mp4), `default` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/property-tour.mp4), `glass` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/property-tour-glass.mp4), `rounded` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/property-tour-rounded.mp4)
- 否决 `brutalist`, `minimal`, `neo`

### quiz-result

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/quiz-result/Composition.tsx)

- **待定** `brutalist` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/quiz-result-brutalist.mp4), `minimal` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/quiz-result-minimal.mp4), `neo` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/quiz-result-neo.mp4)
- 否决 `dark`, `default`, `glass`, `rounded`

### quote-card

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/quote-card/Composition.tsx)

- **待定** `brutalist` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/quote-card-brutalist.mp4), `dark` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/quote-card-dark.mp4), `rounded` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/quote-card-rounded.mp4)
- 否决 `default`, `glass`, `minimal`, `neo`

### saas-hero

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/saas-hero/Composition.tsx)

- **待定** `brutalist` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/saas-hero-brutalist.mp4), `dark` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/saas-hero-dark.mp4), `default` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/saas-hero.mp4), `neo` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/saas-hero-neo.mp4)
- 否决 `glass`, `minimal`, `rounded`

### sales-card

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/sales-card/Composition.tsx)

- **待定** `dark` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/sales-card-dark.mp4), `default` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/sales-card.mp4), `glass` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/sales-card-glass.mp4)
- 否决 `brutalist`, `minimal`, `neo`, `rounded`

### speaker-card

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/speaker-card/Composition.tsx)

- **待定** `dark` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/speaker-card-dark.mp4)
- 否决 `brutalist`, `default`, `glass`, `minimal`, `neo`, `rounded`

### spring-scale-in

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/spring-scale-in/Composition.tsx)

- **待定** `rounded` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/spring-scale-in-rounded.mp4)
- 否决 `brutalist`, `dark`, `default`, `glass`, `minimal`, `neo`

### stats-dashboard

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/stats-dashboard/Composition.tsx)

- **待定** `dark` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/stats-dashboard-dark.mp4), `default` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/stats-dashboard.mp4), `glass` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/stats-dashboard-glass.mp4), `minimal` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/stats-dashboard-minimal.mp4), `rounded` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/stats-dashboard-rounded.mp4)
- 否决 `brutalist`, `neo`

### stock-ticker

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/stock-ticker/Composition.tsx)

- **待定** `brutalist` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/stock-ticker-brutalist.mp4), `dark` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/stock-ticker-dark.mp4), `default` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/stock-ticker.mp4), `neo` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/stock-ticker-neo.mp4)
- 否决 `glass`, `minimal`, `rounded`

### team-intro

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/team-intro/Composition.tsx)

- **待定** `dark` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/team-intro-dark.mp4), `glass` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/team-intro-glass.mp4), `minimal` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/team-intro-minimal.mp4), `neo` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/team-intro-neo.mp4)
- 否决 `brutalist`, `default`, `rounded`

### testimonial-card

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/testimonial-card/Composition.tsx)

- **待定** `glass` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/testimonial-card-glass.mp4)
- 否决 `brutalist`, `dark`, `default`, `minimal`, `neo`, `rounded`

### ui-walkthrough

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/ui-walkthrough/Composition.tsx)

- **待定** `dark` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/ui-walkthrough-dark.mp4), `default` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/ui-walkthrough.mp4), `glass` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/ui-walkthrough-glass.mp4), `rounded` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/ui-walkthrough-rounded.mp4)
- 否决 `brutalist`, `minimal`, `neo`

### virtual-walkthrough

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/virtual-walkthrough/Composition.tsx)

- **待定** `dark` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/virtual-walkthrough-dark.mp4), `default` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/virtual-walkthrough.mp4), `rounded` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/virtual-walkthrough-rounded.mp4)
- 否决 `brutalist`, `glass`, `minimal`, `neo`

### wellness-stats

[上游代码 →](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/src/templates/wellness-stats/Composition.tsx)

- **待定** `default` [看片](https://github.com/locomotion-pro/locomotion/blob/d42711f950c2c6776056df4d9c7c729d4490ba50/public/videos/wellness-stats.mp4)
- 否决 `brutalist`, `dark`, `glass`, `minimal`, `neo`, `rounded`

---

## 全否的版式

以下 13 个版式的 7 套皮肤全部否决。负样本保留在
[`../curation/locomotion-2026-08-19.json.bz2`](../curation/locomotion-2026-08-19.json.bz2)，
是给未来预筛新素材用的下调依据，不要删。

`achievement-unlock`  `bold-text-punch`  `culture-reel`  `fade-slide-up`  `gradient-text`  `leaderboard`  `lesson-intro`  `level-up`  `logo-reveal`  `meme-card`  `milestone-counter`  `product-hunt`  `toggle-switch`
