# Motion Research Catalog

> 当前是 **v0.1 粗筛目录**。目标是让 Yoru 先看风格，不是现在就安装全部项目。
>
> 使用方式：点开 Preview / Gallery → 看 30 秒左右 → 在 `curation/` 里记 `❤️ / ○ / ×`。先看脸，不跑代码。

## A. 第一轮优先看：最可能直接影响我们的 Motion System

| Repo | 主要价值 | 先看什么 | 初始定位 |
|---|---|---|---|
| [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | 152 shot recipe cards、209 styles / motion previews、Agent Skill、Remotion 组件、声音设计 | [Live Gallery](https://vincentwei1021.github.io/video-shotcraft/) | **审美 / 镜头动作词典** |
| [av/remotion-bits](https://github.com/av/remotion-bits) | Remotion 动画组件与 utilities；文字、转场、粒子、3D；带 CLI / MCP / Skill | [remotion-bits.dev](https://remotion-bits.dev) | **基础动效零件库** |
| [locomotion-pro/locomotion](https://github.com/locomotion-pro/locomotion) | 67 个较完整 Remotion 模板 + 6 种视觉主题 + Studio / AI 编辑思路 | [locomotion.pro](https://locomotion.pro) | **风格 × 模板参考** |
| [reactvideoeditor/remotion-templates](https://github.com/reactvideoeditor/remotion-templates) | 81 个独立效果 / 动画组件；Text、Cinematic、Transition、Branding、Chart 等 | [Live Demos](https://www.reactvideoeditor.com/remotion-templates) | **动作拆解库** |
| [reactvideoeditor/clippkit](https://github.com/reactvideoeditor/clippkit) | 类似 UI component library 的 Remotion 组件库；Intro、文字、Transition、Scene | [clippkit.com](https://clippkit.com) | **可组合组件设计参考** |
| [remotionhub/remotionhub-assets](https://github.com/remotionhub/remotionhub-assets) | RemotionHub 的案例 / animation asset 数据与 manifest | Repo 内 manifest / remotion 目录 | **案例资产索引** |

## B. Remotion 官方：工程规则、能力边界、Agent 用法

| Repo | 主要价值 | 先看什么 | 初始定位 |
|---|---|---|---|
| [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | Remotion 本体、官方 docs、examples、Elements 相关实现 | docs / examples / Elements | **工程基座** |
| [remotion-dev/skills](https://github.com/remotion-dev/skills) | 官方 Agent Skills：create / markup / render / captions / maps / SaaS 等 | `remotion-best-practices` 与 `remotion-markup` | **Agent 写法规范** |
| [remotion-dev/template-prompt-to-motion-graphics-saas](https://github.com/remotion-dev/template-prompt-to-motion-graphics-saas) | Prompt → motion graphics 的官方模板 / Agent 架构参考 | skills / prompt flow | **AI 生成工作流参考** |
| [remotion-dev/template-audiogram](https://github.com/remotion-dev/template-audiogram) | Audiogram / 音频驱动画面模板 | composition + audio handling | **口播 / 音频内容参考** |
| [remotion-dev/template-next-app-dir](https://github.com/remotion-dev/template-next-app-dir) | Remotion 与 Next.js App Router 集成 | app / render architecture | **未来工具化参考** |

## C. 编辑器、时间线与“让人可以选模板”的交互

| Repo | 主要价值 | 注意 |
|---|---|---|
| [reactvideoeditor/free-react-video-editor](https://github.com/reactvideoeditor/free-react-video-editor) | Browser timeline、clip arrangement、text overlay、Remotion Player | **许可证不是 MIT；只做架构参考，暂不复制代码** |
| [reactvideoeditor/hyperframes-templates](https://github.com/reactvideoeditor/hyperframes-templates) | 新的 HTML / Agent video template 方向 | 先观察，后续判断是否值得实测 |

## D. 相邻框架：不准备替代 Remotion，专门偷师不同 motion language

| Repo | 路线 | 我们看什么 |
|---|---|---|
| [motion-canvas/motion-canvas](https://github.com/motion-canvas/motion-canvas) | TypeScript + Canvas + generator timeline | Explainer、矢量动画、镜头与节奏表达 |
| [midrender/revideo](https://github.com/midrender/revideo) | 从 Motion Canvas 路线发展的视频模板 / 自动化框架 | 动态输入、模板化、API 视频生成 |
| [ManimCommunity/manim](https://github.com/ManimCommunity/manim) | Python 数学 / 知识动画 | 技术科普、解释型动效的结构 |
| [Zulko/moviepy](https://github.com/Zulko/moviepy) | Python 视频编辑 / compositing | 后处理、批处理、非视觉设计型流水线 |

## E. 二级研究索引：用于继续发现新候选，不直接视为可信组件源

| Repo | 用途 |
|---|---|
| [frankxai/awesome-motion-design-agent-skills](https://github.com/frankxai/awesome-motion-design-agent-skills) | Agent + motion design 相关资源索引；适合找线索，不直接当质量背书 |
| [Supersynergy/awesome-ai-video-editing](https://github.com/Supersynergy/awesome-ai-video-editing) | AI video editing 生态索引 |
| [renezander030/awesome-video-automation](https://github.com/renezander030/awesome-video-automation) | 自动化视频相关项目索引 |
| [linwuqu/Remotion_awesome_videos](https://github.com/linwuqu/Remotion_awesome_videos) | Remotion 成片 / 案例候选集合，待二次审核 |

## F. 已发现但暂不进入主筛选

- `Thedurancode/locomotion-templates`：当前内容与 `locomotion-pro/locomotion` 基本重合，先把后者视为 canonical candidate，避免重复看。
- GitHub 搜索中大量一次性 Remotion demo / assignment / fork：暂不收录，除非后续发现明确独特的 motion style。

---

## Yoru 的筛选规则

先不要评价“代码写得好不好”，第一轮只回答：

- `❤️`：我真的想以后用这种视觉 / 动作语言
- `○`：有一部分喜欢，值得继续拆
- `×`：无感 / 土 / 不适合我的内容

如果愿意多写一句，再补：

`喜欢的是：字体 / 转场 / 图片运动 / 节奏 / 色彩 / 构图 / UI / 3D / SFX / 其他`

第二轮再由 Akari 按你留下来的结果重新分类。