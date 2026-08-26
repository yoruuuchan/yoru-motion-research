# Question Card — Editorial

采访问题之间使用的 4 秒编辑感问题卡。用于“一个问题 → 一段回答”的访谈剪辑结构；同族内容直接以本条目为母版，只换问题文字与栏目标签，不重新设计。

## 文件

```text
gold/question-card-editorial/
├── README.md
├── render_question_cards.py
└── stills/
    ├── still_018_intro.png
    ├── still_060_hold.png
    └── still_110_outro.png
```

MP4 不入库。`stills/` 均由公开版中性占位文案重新渲染，并缩放为 640 × 360 预览图。

## 默认参数

| 参数 | 默认值 |
| --- | --- |
| 画布 | 1920 × 1080 |
| 帧率 | 30 fps |
| 时长 | 120 帧 / 4 秒 |
| 卡片数 | 4 |
| `--label` | `INTERVIEW` |
| `--tags` | `标签 A · 标签 B · 标签 C · 标签 D`（底部说明行） |
| 问题文案 | `QUESTIONS` 中的 4 条中性占位文案 |
| 大标题字体 | Noto Serif CJK Bold，默认 `/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc` |
| 正文小字字体 | Noto Sans CJK Regular，默认 `/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc` |
| 等宽编号字体 | DejaVu Sans Mono，默认 `/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf` |
| 编码 | H.264 / `libx264` / CRF 18 / `yuv420p` |

字体路径可以通过 `--serif-font`、`--sans-font`、`--mono-font` 覆盖。需要 Pillow 与 FFmpeg。

## 时序

| 元素 | 帧区间 | 动作 | 缓动 |
| --- | ---: | --- | --- |
| 全局入场 | 3–20 | opacity 0 → 1 | cubic ease-out |
| 顶部发丝线 | 5–24 | x2 145 → 1630 | cubic ease-out |
| 顶部强调短线 | 8–20 | width 0 → 150 px | cubic ease-out |
| 大号编号 | 0–25 | y 330 → 300 | cubic ease-out |
| `QUESTION 0N` | 12–28 | x 145 → 185，opacity 0 → 1 | cubic ease-out |
| 问题正文 | 16–34 | x 145 → 190，单行 y +24 → 0，opacity 0 → 1 | cubic ease-out |
| 多行正文 | 每行 +3 帧 | 同上 | cubic ease-out |
| 底部说明与横线 | 25–42 | y 870 → 850，opacity 0 → 1 | cubic ease-out |
| 全局退场 | 101–119 | opacity 1 → 0 | cubic ease-in |
| 退场抬升 | 101–119 | y 0 → -18 px | cubic ease-in |

颜色：

```text
BG      #FFFFFF
INK     #111827
MUTED   #6F8199
HAIR    #DAE4F0
NAVY    #2F3E66
ACCENT  #3186FF
PALE    #E8F2FF
```

## 运行

渲染 4 张问题卡，同时刷新三张关键帧：

```bash
python render_question_cards.py
```

只重渲关键帧：

```bash
python render_question_cards.py --stills-only
```

自定义栏目标签：

```bash
python render_question_cards.py --label "YOUR LABEL"
```

## 关键帧

- `stills/still_018_intro.png`：入场中段，正文正在进入
- `stills/still_060_hold.png`：完整定格
- `stills/still_110_outro.png`：退场中段

## 来源

- 交付日期：2026-08-13
- 来源：一次采访交付，共 4 张；公开条目不记录客户名
- 源码状态：事后从会话恢复，不是原生源码存档
- 公开化处理：真实问题替换为中性占位文案；原 `OPC INTERVIEW` 顶部标签改为 `--label` 参数，默认 `INTERVIEW`；底部说明行改为 `--tags` 参数，默认中性占位；抽帧图使用占位文案重新渲染

## 验证记录

- 2026-08-26：本地复渲与交付版全 120 帧逐帧比对，平均像素差 0.45/255；差异全部为标点字形边缘（原容器 `.ttc` 默认日文面 vs 简中面），布局、颜色、时序完全一致。
