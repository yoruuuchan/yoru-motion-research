# edit-hook-moves

**收尾**

logo-sting-button 片尾钩子——片尾 logo 定住后突插 12f 彩蛋再收，预告片 button ending

- **适用** 片尾收束（全片 ≤1 次）
- **时长** ~5s
- **能量** 低→瞬时中→低

## 我的判断

| 变体 | 判断 | 分数 | 预览 |
|---|---|---:|---|
| `logo-sting-button` | maybe |  | [看片](https://vincentwei1021.github.io/video-shotcraft/media/logo-sting-button.mp4) |

## 意图

库内声画卡管的都是"画面上的事"；这一式管**时间线本身的修辞**——
终点的反悔：收黑→logo 淡入定住（观众以为结束）→突然 12f UI 特写
彩蛋硬切插入→切回 logo 收尾，预告片 button ending，留最后一个钩子。
拿观众的"已经结束了"的预期开玩笑。

## 参数表

| 参数 | 典型值 | 调节手感 |
|------|--------|----------|
| 彩蛋时长 | 12f 级，内含 tick 圆点只亮第 4–5f（2f，条件挂载） | 长于 20f 就不是"眨眼"是一个镜头 |
| 彩蛋构图 | 面板 translate+scale(2.4) 特写按钮行，平移量把 sidebar 完全推出画面 | 彩蛋里露出旧构图残边读作切错了 |
| 像素级一致 | logo 段 interpolate 全 clamp 到终值，彩蛋前后 logo 共用同一分支渲染 | 硬切回来 logo 跳 1px 都读作抖动 |
| 剪辑方式 | 全程硬切分支渲染（frame 区间 return 不同子树），无交叉溶解 | 节奏靠剪不靠淡；任何溶解都泄劲 |

## 已知坑

- demo 在灰阶/占位素材上调校通过——参数是调校起点非实战定稿，
  首次实战须以真实素材回验
- 全片 ≤1 次且只在片尾——中段用 button ending 变成故障，
  观众以为片子坏了
- 彩蛋内容必须是全片未见的新特写——复用旧镜头读作剪辑失误
  不是钩子，命门

## 出处

- 参数卡原文 [edit-hook-moves.md](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/references/shots/outro/edit-hook-moves.md)
- 上游实现 [outro/edit-hook-moves](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/demos/outro/edit-hook-moves)
- 授权 Apache-2.0，可改可用，见 [`../../../LICENSE`](../../../LICENSE) 与 [`../../../NOTICE.md`](../../../NOTICE.md)
