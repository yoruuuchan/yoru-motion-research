# canvas-materialize-moves

**交互与功能演示**

内容"物化上画布"两式——panel-to-canvas 行倒卡（面板表格行沿弧线飞出、跨容器变形成画布卡片）与 diagram-cascade 级联生成树（prompt 打字后节点逐层弹出、连线先于节点生长）

- **适用** AI/协作工具"生成结果落到画布上"的叙事段落；A 式讲"已有内容换了个存在形态"，B 式讲"从一句话长出一棵结构"
- **时长** A ~4.3s（130f）/ B ~5.3s（160f）
- **能量** 中

## 我的判断

| 变体 | 判断 | 分数 | 预览 |
|---|---|---:|---|
| `diagram-cascade` | keep | 4 | [看片](https://vincentwei1021.github.io/video-shotcraft/media/diagram-cascade.mp4) |
| `panel-to-canvas` | keep | 4 | [看片](https://vincentwei1021.github.io/video-shotcraft/media/panel-to-canvas.mp4) |

## 意图

库内生成叙事只有"面板内流式写入"（ai-stream-response 证据行汇入面板）
和"图表自己活起来"（chart-live-moves），没有词管**内容离开容器、在
开放画布上物化成新实体**。本卡补这一块：画布是舞台，生成物是登台的
演员。A 式的命门是跨容器形态迁移——同一条内容从"行"变成"卡"，位置
/宽高/圆角/内容布局在一条 spring 上同步插值，观众读到"是它飞过去
变的"而不是"删一个加一个"；B 式的命门是级联时序——线牵出节点、层
喂出层，结构感来自先后而非同时。

## 参数表

| 参数 | 典型值 | 调节手感 |
|------|--------|----------|
| A 打勾 | 12/22/32f 逐个，spring(damping 10, stiffness 260) pop | 打勾是"预告"，全删观众不知道要飞谁；同帧齐勾读作静态已选 |
| A 起飞错峰 | 按钮 46f 按下，三行 54/60/66f 起飞（错峰 6f） | 同帧齐飞读作复制粘贴；错峰 >12f 尾行像掉队 |
| A 飞行插值 | spring(damping 16, stiffness 60, 34f)；位置走二次贝塞尔，中点上抬 170px | 直线飞读作平移不读作"倒出来"；中点抬 <100px 弧线感消失 |
| A 形态迁移 | 行 560×80 → 卡 480×240，圆角 10→18，rowOp 在 u≈0.45 前灭、cardOp 后亮 | 两套内容交叉淡化必须错开——中段两态同显即穿帮 |
| A 落位倾角 | ±2° 随机（-2/1.5/2） | 全正读作网格排版；>4° 读作散落故障 |
| B 打字 | 1.1 字符/帧，敲完 prompt 条描边 G.border→G.ink 确认 | 无确认态则"敲完"与"开始生成"之间没有因果扣 |
| B 级联时序 | 根 52f 起，层间隔 20f、同层兄弟错峰 6f；节点 spring(damping 11, stiffness 170) | 层间隔 <12f 读作一次性全出；兄弟同帧读作复制 |
| B 连线先行 | SVG 折角 path（父底边→中线→子顶边）描线 16f ease-out，比子节点早 8f | "线牵出节点"是因果感来源；线晚于节点就成了补笔 |
| B 收尾呼吸 | 末节点 +22f 起，以树心为原点 scale 1→1.035→1（sin inOut，28f） | 呼吸是"成树"的句号；>1.06 读作缩放故障 |

## 已知坑

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
  首次实战须以真实素材回验
- 与 ai-stream-response 分工：那卡内容在**面板内**流式落位（结论先到、
  证据随后），本卡内容**离开面板上画布**；同片可串（先流式生成→再倒上画布），
  串用时 A 式的打勾段可省——流式完成态即"已选"
- 与 chart-live-moves 分工：那卡是数据图表自身的活性（流线/点阵/爆轴），
  B 式是结构图的**诞生过程**——图活着≠图正在被生成，别拿 B 式去演已有图表
- A 式行槽必须塌陷成虚线留白——行飞走后原位完好如初，"迁移"就退化成
  "复制"，语义全失
- A 式交叉淡化窗口（rowOp 灭于 u≈0.45 前、cardOp 亮于其后）是防穿帮的
  命门；spring 有过冲，u 可能短暂 >1，内容 opacity 都要 clamp
- B 式呼吸原点必须是树的视觉重心（demo 960,620）而非画面中心，
  不然读作整屏 zoom

## 出处

- 参数卡原文 [canvas-materialize-moves.md](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/references/shots/interaction/canvas-materialize-moves.md)
- 上游实现 [interaction/canvas-materialize-moves](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/demos/interaction/canvas-materialize-moves)
- 授权 Apache-2.0，可改可用，见 [`../../../LICENSE`](../../../LICENSE) 与 [`../../../NOTICE.md`](../../../NOTICE.md)
