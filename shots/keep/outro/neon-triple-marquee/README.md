# neon-triple-marquee

**收尾**

三行对向霓虹跑马灯 recap——BETTER/FASTER/STRONGER 空心描边巨字上中下排满全屏，奇偶行反向匀速无限横滚，三行按 1/3 相位轮流亮起，结尾整组淡出

- **适用** 片尾主题词复读机段落；三连词口号的"余韵"拍法（cel-flash-stomp 砸完之后的低一档收尾）；音乐段无旁白铺陈
- **时长** 4–5s（demo 150f：10f 淡入 + 循环体 + 20f 淡出）
- **能量** 中高（持续流动 + 逐行脉冲，无瞬时冲击）

## 我的判断

| 变体 | 判断 | 分数 | 预览 |
|---|---|---:|---|
| `neon-triple-marquee` | keep |  | [看片](https://vincentwei1021.github.io/video-shotcraft/media/neon-triple-marquee.mp4) |

## 意图

一行 marquee 只是网页装饰；三行叠起来、奇偶反向、再让亮度按相位轮流
走，就成了"主题词在观众眼前列队巡游"。命门是**明暗轮唱**：任一时刻
只有一行是霓虹主角，其余压暗成细描边背景——三行全亮是灯牌事故，
轮流亮才是 recap。反向对滚制造"包围感"：上下行向右、中行向左，
视线被夹在中间，词从两侧源源不断流过，读作"这三个词说不完"。

## 参数表

| 参数 | 典型值 | 调节手感 |
|------|--------|----------|
| 字号/行距 | 300px，行距 350px 排满 1080 | 行间留白 >80px 读作三条横幅广告而非一面词墙 |
| 滚速 | 14/17/14 px/f，中行反向 | >25 读不清词只见光带；三行同速同向读作整版平移 |
| 脉冲周期 | 45f，相位差 15f | 周期 <30f 三行抢闪读作故障；>70f 轮唱感断掉 |
| 亮度区间 | opacity 0.35→1 + stroke 5→8px | 暗态 <0.25 暗行消失，"三行"结构丢了 |
| 辉光 | 双层 drop-shadow，亮态 30/70px | 单层或 <20px 读作普通描边字不读作霓虹 |
| 淡入淡出 | 入 10f / 出 20f 整组 opacity | 循环体无始无终，掐头去尾全靠这两端；硬切进出读作素材没铺满 |

## 已知坑

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
  首次实战须以真实素材回验
- 与 page-waterfall-wall 分工：那卡是页面截图纵向瀑布做"内容体量感"，
  本卡是文字行横向对滚做"主题词余韵"——素材是词不是页，位置在片尾不在中段
- 与 outro-group-photo-launch 分工：全家福是峰值终镜（元素合影+发布会收场），
  本卡是终镜前的 recap 铺垫或低成本备选终镜，两者可串（本卡→淡出→全家福）不可叠
- 与 cel-flash-stomp 同吃"三连词口号"文案：那卡逐词砸（高能宣告），
  本卡整组滚（余韵复读）——同一组词全片最多各用一次，先砸后滚顺序不可反
- 副本数按 `ceil(1920/unitW)+3` 留冗余——短词（≤4 字符）unitW 小，
  副本不足会在回绕瞬间露右侧空缺
- 实战品牌色版：三行可统一品牌色靠明暗区分，但辉光对比须 ≥ demo 的
  0.35→1 幅度，不然轮唱读不出来

## 出处

- 参数卡原文 [neon-triple-marquee.md](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/references/shots/outro/neon-triple-marquee.md)
- 上游实现 [outro/neon-triple-marquee](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/demos/outro/neon-triple-marquee)
- 授权 Apache-2.0，可改可用，见 [`../../../LICENSE`](../../../LICENSE) 与 [`../../../NOTICE.md`](../../../NOTICE.md)
