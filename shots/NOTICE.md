# NOTICE

本目录下的 `.tsx` 实现来自 Video Shotcraft，按 Apache License 2.0 使用。

- 上游仓库 https://github.com/Vincentwei1021/video-shotcraft
- 上游 commit `0d6f0b57f0d4d6700761644c07f7ef03c3e50234`（2026-08-14T04:17:12Z）
- 原始授权文件保留在 [`LICENSE`](LICENSE)

## 我们做了什么改动

1. **只收录筛选留下的部分。** 上游 209 个候选里，`keep/` 和 `maybe/` 只放留下和待定的，
   否决的不复制（判断记录仍完整保存在 `curation/`）。
2. **改了 import 路径。** 上游的 `demos/_fixtures/` 和 `demos/_textures/` 在这里合并成
   `_kernel/`，所有实现文件里对应的相对路径同步改写。除此之外实现代码未做修改。
3. **每个目录新增了 `README.md`**，由 `scripts/build-shot-library.py` 从上游的中文参数卡
   和我们自己的筛选记录生成。这部分是我们写的，不属于上游。

上游对镜头手法的来源与法律边界另有说明，见上游仓库的
`references/shots/ATTRIBUTION.md`。
