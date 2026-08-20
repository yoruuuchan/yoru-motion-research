# assemble-then-type-flyin

**光效与强调**

空的暗底网格上，无文字的组件骨架先从四面八方飞入贴合；随后各处文字逐字从 3D 空间旋转着飞来落位，先大标题后小标注，全部落位后页面成形

- **适用** 页面/海报"自己长出来"的开场；排版类产品的能力展示；从骨架到成稿的两段式叙事
- **时长** 约5.2s（156f@30fps）
- **能量** 中高（骨架段稀疏、文字段密集，能量单调上升到收尾）

## 我的判断

| 变体 | 判断 | 分数 | 预览 |
|---|---|---:|---|
| `assemble-then-type-flyin` | keep | 4 | [看片](https://vincentwei1021.github.io/video-shotcraft/media/assemble-then-type-flyin.mp4) |

## 意图

把"页面生成"拆成两个语义清楚的阶段：先立骨架（框、卡片、分隔线、
色块，全部无字），再填文字。文字用逐字 3D 旋转落位，是因为骨架段
只有平面位移——两段的运动维度必须不同，否则观众读不出"这是第二步"。

## 参数表

| 参数 | 典型值 | 调节手感 |
|------|--------|----------|
| 骨架时序 | 6 件，ft 0.04→0.20（间隔 0.03–0.04） | 骨架段占前 35%；压缩到 0.15 内就和文字段糊在一起 |
| 骨架飞入 | outBack、0.14 时长、位移 60–220px + ±8° | 与 `scanline-assemble-flyin` 同一手法，去掉扫描线后靠时序读顺序 |
| 骨架残影 | blur ≤2px，a>0.97 设 none | 阈值留 3% 裕量；直接判 a>=1 会因浮点残留一层糊 |
| 文字起点 | 大标题 0.34/0.40，小标注 0.58→0.76 | 大字先落是可读性要求：小字先落观众会去读小字 |
| 逐字位移 | dx ±170 / dy ±130 / dz −120→−420 | dz 是"从远处来"的主力；只给 dx/dy 就成了平面散入 |
| 逐字旋转 | rotateX/Y/Z 各 ±120°–190° | 大角度才有"翻着飞"的手感；±30° 只像抖动 |
| perspective | 600px（写在每个字符自己的 transform 里） | 值越小透视越夸张；1200px 以上 3D 感基本消失 |
| 字间隔 | clamp((0.94−start−0.13)/n, 0.002, 0.012) | 自适应上限 0.012 是"逐字可辨"的下限速度 |
| 落位清零 | a>=1 → transform:'none' | 不清零会留下 13 个块的合成层，长片会掉帧 |

## 已知坑

- 字符 span 走正常排版流（`display:inline-block`），动画只动 transform——
  不要用绝对定位逐字摆位，换文案就全乱
- 空格字符必须显式塞成 `' '`（代码里用 `ch === ' ' ? ' ' : ch`），
  否则 inline-block 的空 span 宽度归零，词间距消失
- `start` 是手写的 13 个数值，换文案（尤其字符数变化大时）要回看
  最后一块是否仍在 t≈0.95 前落完；`step` 只保证块内，不保证块间
- 内容为中性占位模板（"The headline for your product here" / "Acme Studio"
  等），落地全部替换；A_RGB（`159,182,232`）为强调色槽位
- 与 `scanline-assemble-flyin` 的区别是**没有扫描线**：那张靠扫描线
  解释顺序，这张靠"先骨架后文字"的两段式解释顺序，两者不要混用

## 出处

- 参数卡原文 [assemble-then-type-flyin.md](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/references/shots/effects/assemble-then-type-flyin.md)
- 上游实现 [effects/assemble-then-type-flyin](https://github.com/Vincentwei1021/video-shotcraft/blob/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/demos/effects/assemble-then-type-flyin)
- 授权 Apache-2.0，可改可用，见 [`../../../LICENSE`](../../../LICENSE) 与 [`../../../NOTICE.md`](../../../NOTICE.md)
