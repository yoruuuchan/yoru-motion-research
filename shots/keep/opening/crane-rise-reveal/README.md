# crane-rise-reveal

**开场与品牌**

升降臂拉升揭示——开场怼在一行数据特写，相机沿 Y 轴减速升起后拉，行行涌入直到整面 dashboard 铺满全幅

- **适用** "从细节到全局"的开场定场；与 drone-dive-landing（全局→单点俯冲）互为反向
- **时长** 5s（特写 hold 20f + 拉升 100f + 满幅静止 30f）
- **能量** 中高（持续单向运动，无冲击拍）

## 我的判断

| 变体 | 判断 | 分数 | 预览 |
|---|---|---:|---|
| `crane-rise-reveal` | keep |  | [看片](https://vincentwei1021.github.io/video-shotcraft/media/crane-rise-reveal.mp4) |

## 意图

开场定场库内已有 drone-dive-landing——从上帝视角砸进 hero 特写，
"全局→焦点"。本卡是它的镜像："焦点→全局"——先怼在一行真实数据上
让观众看清"这是什么"，再升降臂式拉升后退，一排排内容涌入画面，
最后整面产品铺满——"你看到的这一行，只是这一面墙的一格"。
适合以产品体量/内容丰富度为卖点的开场；两卡同片只用一个方向。

## 参数表

| 参数 | 典型值 | 调节手感 |
|------|--------|----------|
| 起点特写 | scale 3.2，对准最底行（一行占满画幅） | hold ≥20f 让"这是一行数据"可读再起飞 |
| 拉升 | 100f Easing.out(quad)，scale 3.2→1.0 | 快于 80f 行脉冲追不上；慢于 130f 中段拖 |
| 行脉冲 | 越线触发，0→0.22→0 深色叠层 22f | 脉冲跟不上相机（固定间隔触发）立刻穿帮 |
| 收尾 | 满幅后真静止 ≥30f | R1；满幅帧即标准构图，不再补推 |

## 已知坑

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
  首次实战须以真实素材回验
- 起点特写 = 一行内容被放大 3.2 倍盯着看，真实素材先过
  审美准则 Q2 的高分辨率栅格化技法，低倍截图开场即糊
- 快速拉升段可包 CameraMotionBlur（参数见 deck-deal-flyin 运动模糊行），
  但只包前半程快速段——临顶慢速段包了会抹软文字（轮 #8 判例）
- 与 drone-dive-landing 同片不并用（一升一降互为镜像，观众读作同一招）；
  与 crane 语义最近的 tilt-reveal 未入库，别混称

## 出处

- 参数卡原文 [crane-rise-reveal.md](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/references/shots/opening/crane-rise-reveal.md)
- 上游实现 [opening/crane-rise-reveal](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/demos/opening/crane-rise-reveal)
- 授权 Apache-2.0，可改可用，见 [`../../../LICENSE`](../../../LICENSE) 与 [`../../../NOTICE.md`](../../../NOTICE.md)
