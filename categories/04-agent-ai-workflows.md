# 04 · Agent / AI Workflows

这里研究的是“怎么让 Claude / Codex / GPT 可靠地使用动效知识”，不是单纯收 Prompt。

## Primary

### Remotion Agent Skills
- [remotion-dev/skills](https://github.com/remotion-dev/skills)
- 官方技能覆盖 best-practices / create / markup / studio / render / maps / captions / saas / interactivity / docs / upgrade / multimedia。
- 用途：以后所有 Remotion 实现的工程底座。

### Prompt → Motion Graphics SaaS
- [remotion-dev/template-prompt-to-motion-graphics-saas](https://github.com/remotion-dev/template-prompt-to-motion-graphics-saas)
- 用途：拆解 Agent 如何理解 typography、timing、transition、motion graphics 任务并生成可渲染结果。

### video-shotcraft
- [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)
- 用途：看“shot card / recipe”怎样把导演语言变成 Agent 可执行规范。

### Remotion Bits
- [av/remotion-bits](https://github.com/av/remotion-bits)
- 用途：看 `find → fetch → insert` 的 CLI / MCP / Skill component retrieval workflow。

## Discovery-only

### Awesome Motion Design Agent Skills
- [frankxai/awesome-motion-design-agent-skills](https://github.com/frankxai/awesome-motion-design-agent-skills)
- README 把 Lenis / Framer / Remotion / Fal 等 programmatic animation schemas 放进同一 Agent 生态。
- 用于继续发现线索，**不把列表收录本身当质量认证**。

## 最终我们想学到的不是 Prompt，而是 schema

例如未来组件被 Agent 调用时，至少应知道：

- purpose
- style tags
- rhythm range
- supported aspect ratios
- editable props
- palette tokens
- transition compatibility
- audio cue suggestions
- known failure modes
- source + license

这样 Claude/Codex 选组件时是在查一个 motion system，而不是随机抽动画。
