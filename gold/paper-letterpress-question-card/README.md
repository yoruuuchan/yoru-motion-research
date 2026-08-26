# Paper Letterpress Question Card

低能量、长停留的采访/章节问题卡。纸面底、淡色巨型序号、小号 `QUESTION NN` 标签与两行主问题构成全部信息层；主标题用“压印”式 scale + blur + opacity 入场，短蓝线在标题落定后收束，随后保持长时间静止阅读。

## 什么时候直接用我

用于 16:9 采访、章节转场、问题提示等“观众需要在几秒内读完一句问题”的镜头。直接替换编号和问题文案，**不要重新设计布局、增加 Logo、边框、说明卡或持续运动**。

## 固定规格

- 画布：1920×1080
- 帧率：30 fps
- 时长：120f / 4.0s
- 音频：无
- Pillow：12.3.0
- FFmpeg：7.1.5，`libx264`
- 字体文件：
  - `/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc`
  - `/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc`
- 背景：`#F2F5F5` + 中央白色柔光
- 正文：`#1B2127`
- 强调蓝：`#3186FF`
- 标签蓝：`#2E4A68`

## 版式参数

| 元素 | 参数 |
|---|---|
| 淡色大序号 | 起点 `(1265, 246)`；470px Noto Serif CJK Bold；`#3186FF`，alpha 24/255 |
| `QUESTION NN` | 起点 `(170, 265)`；27px Noto Sans CJK Bold；`#2E4A68` |
| 主问题第 1 行 | 起点 `(170, 418)`；136px Noto Serif CJK Bold |
| 主问题第 2 行 | 起点 `(170, 590)`；136px Noto Serif CJK Bold |
| 收束短线 | `(170, 772)`；目标宽 225px，高 6px；`#3186FF`，alpha 235/255 |

## 时间参数

帧号为 0-based。

| 元素 | 入场 / 退场 | 缓动与变化 |
|---|---|---|
| 淡色大序号 | f2→f12 | 线性 opacity 0→1 |
| `QUESTION NN` | f2→f11 | `1-(1-t)^4` quartic ease-out；opacity 0→1 |
| 主问题第 1 行 | f6→f16 | `1-(1-t)^4`；scale 1.28→1、Gaussian blur 7px→0、opacity 0→1 |
| 主问题第 2 行 | f11→f21 | 同上 |
| 蓝色短线 | f20→f38 | smoothstep `t²(3-2t)`；宽度 0→225px |
| 阅读定格 | 约 f38→f105 | 无新增运动 |
| 整卡退场 | f106→f119（理论终点 f120） | smoothstep；`#F2F5F5` 全屏覆盖 alpha 0→1 |

## 渲染

```bash
python render_question_card.py \
  --number 01 \
  --line-1 "一个核心问题？" \
  --line-2 "我们如何回答它？" \
  --out /tmp/question-card.mp4 \
  --stills-dir stills
```

字体默认值是 Linux 容器路径；其他平台用 `--serif-font` / `--sans-font` 覆盖
（Windows 用户字体目录常有同款 `NotoSerifCJKsc-Bold.otf` / `NotoSansCJKsc-Bold.otf`）。

脚本内部使用的 FFmpeg 编码参数：

```bash
ffmpeg -y -f rawvideo -vcodec rawvideo -pix_fmt rgb24 \
  -s 1920x1080 -r 30 -i - -an \
  -c:v libx264 -preset veryfast -crf 18 \
  -pix_fmt yuv420p -movflags +faststart OUTPUT.mp4
```

## Stills

- `stills/f013-entry-mid.webp`：入场中段
- `stills/f062-hold.webp`：定格阅读
- `stills/f112-exit.webp`：退场中段

三张图均使用仓库内的中性占位文案重新渲染，并缩放为 240×135 WebP 预览；不含真实交付文案或客户信息。

## 验证记录

- 2026-08-26：真实交付版本获确认；当场归档实际 Python/Pillow + FFmpeg 渲染链路。
- 2026-08-26：去客户化默认文案重渲；三张关键帧由同一 `render_question_card.py` 生成。
- 源码状态：原生存档。

## 来源

2026-08-26
