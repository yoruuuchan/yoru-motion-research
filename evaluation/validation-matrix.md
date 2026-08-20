# Validation Matrix

第二阶段由 Claude 实测，最终由 GPT / Akari 验收。视觉喜欢只是入场券。

| Dimension | 要回答的问题 | Fail 示例 |
|---|---|---|
| Visual fit | 换成我们的素材后还好看吗？ | Demo 好看，普通素材立刻像 PPT |
| Purpose fit | 它到底适合 Intro / Transition / Title 的哪一种？ | 什么都能用，但什么都不够好 |
| Parameterization | 文字、图、颜色、节奏、时长能否可靠替换？ | 改标题就溢出 / 改图就炸布局 |
| Composition | 能否和其他组件拼起来？ | 必须自己占一整条时间线 / 全局副作用 |
| Aspect ratio | 16:9 / 9:16 / 1:1 能否合理重排？ | 只是粗暴 scale / crop |
| Timing | Slow / Medium / Fast 是否能调而不破坏动作？ | 只能在作者固定时长里成立 |
| Color system | 能否接 palette tokens？ | 大量 hard-coded color / 对比度失控 |
| Typography | 中英文、长短标题是否稳定？ | 只为英文 demo 设计 |
| Dependencies | 引入成本是否合理？ | 一个简单 reveal 拖十几个 runtime deps |
| Determinism | Remotion frame-driven render 是否稳定？ | CSS transition / randomness 导致不可复现 |
| Render | Studio 好看，真实 render 是否一致？ | preview pass / render fail |
| Performance | 1080p / 竖屏是否可接受？ | 极慢、内存爆、浏览器崩 |
| Diagnostics | 失败能否知道在哪里？ | 静默 fallback / 渲染缺元素但仍返回成功 |
| License | 是否允许复制、修改、商用、再分发？ | 无 LICENSE / custom terms 未确认 |
| Asset license | 音频、字体、图片是否独立可用？ | 代码 MIT，但 bundled SFX 不可商用 |

## Result states

- `PASS` — 可进入 YORU Motion System 改造
- `PASS_WITH_CHANGES` — 视觉值得留，但需重构 API / layout / licensing cleanup
- `REFERENCE_ONLY` — 只学思路，不复制实现
- `REJECT` — 不再投入

## Completion rule

“本地能跑”“测试全绿”“Claude 说完成了”都不是最终通过。

候选真正通过至少需要：

1. benchmark render；
2. 实际 MP4 检查；
3. 参数替换测试；
4. 至少一次 16:9 → 9:16 检查（若组件宣称响应式）；
5. license / third-party asset check；
6. 人工视觉验收。
