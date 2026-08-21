# Shots — 镜头库

从 Video Shotcraft 筛出来的镜头动作。一个目录一条参考：`README.md` 说它是什么、
参数怎么调、你当时怎么判断的，旁边的 `.tsx` 就是实现。

- `keep/` — 认可的，可以直接拿去用
- `maybe/` — 待定的，代码留着但不进主线
- `_kernel/` — 所有实现共用的两个模块（缓动/插值 + 占位 UI）

**做片挑主镜头，先从 5 分里挑，4 分补位。** 没打分的 keep 也是认可的，
但那是词汇表，不是购物清单——一条片子用不了几个镜头，别因为库大就堆招式。

上游 https://github.com/Vincentwei1021/video-shotcraft @ `0d6f0b5`，Apache-2.0。
改动见 [`NOTICE.md`](NOTICE.md)。

## keep — 认可

### 界面登场与陈列 · `ui-entrance`

- [card-stack](keep/ui-entrance/card-stack/) **3分** — `card-stack`
- [deck-deal-flyin](keep/ui-entrance/deck-deal-flyin/) **5分** — `deck-deal-flyin`
- [doc-park-left-pill-deal](keep/ui-entrance/doc-park-left-pill-deal/) — `doc-park-left-pill-deal`
- [draw-svg-trace](keep/ui-entrance/draw-svg-trace/) — `draw-svg-trace`
- [element-body-moves](keep/ui-entrance/element-body-moves/) — `axial-stretch`, `contact-shadow-lift`
- [floating-glossy-label-pills](keep/ui-entrance/floating-glossy-label-pills/) — `floating-glossy-label-pills`
- [integration-hub-map](keep/ui-entrance/integration-hub-map/) — `integration-hub-map`
- [list-reveal](keep/ui-entrance/list-reveal/) — `list-reveal`
- [list-stack-press](keep/ui-entrance/list-stack-press/) — `list-stack-press`
- [neon-frame-forerun](keep/ui-entrance/neon-frame-forerun/) — `neon-frame-forerun`
- [neon-frame-orbit-drop](keep/ui-entrance/neon-frame-orbit-drop/) — `neon-frame-orbit-drop`
- [page-waterfall-wall](keep/ui-entrance/page-waterfall-wall/) — `page-waterfall-wall`
- [paper-craft-moves](keep/ui-entrance/paper-craft-moves/) — `masking-tape-slap`, `popup-book-rise`
- [product-card-progressive-assemble](keep/ui-entrance/product-card-progressive-assemble/) — `product-card-progressive-assemble`
- [radial-wave](keep/ui-entrance/radial-wave/) — `radial-wave`
- [research-card-stack-scroll](keep/ui-entrance/research-card-stack-scroll/) — `research-card-stack-scroll`
- [row-embed](keep/ui-entrance/row-embed/) **4分** — `row-embed`
- [runway-ground-skim](keep/ui-entrance/runway-ground-skim/) **5分** — `runway-ground-skim`
- [skeleton-reveal](keep/ui-entrance/skeleton-reveal/) — `skeleton-reveal`
- [value-stagger-gradient](keep/ui-entrance/value-stagger-gradient/) — `value-stagger-gradient`
- [wall-reveal-moves](keep/ui-entrance/wall-reveal-moves/) — `bento-light-up`, `grid-wave-flip`, `wireframe-draw-on`

### 交互与功能演示 · `interaction`

- [ai-stream-response](keep/interaction/ai-stream-response/) — `ai-stream-response`
- [autolayout-gap-dial](keep/interaction/autolayout-gap-dial/) — `autolayout-gap-dial`
- [canvas-materialize-moves](keep/interaction/canvas-materialize-moves/) **4分** — `panel-to-canvas`, `diagram-cascade`
- [chip-grid-single-select-blackout](keep/interaction/chip-grid-single-select-blackout/) — `chip-grid-single-select-blackout`
- [chip-lift-to-user-pill](keep/interaction/chip-lift-to-user-pill/) **4分** — `chip-lift-to-user-pill`
- [collab-cursor-moves](keep/interaction/collab-cursor-moves/) **3分** — `dialogue-duet`, `cast-ensemble`
- [command-palette-summon](keep/interaction/command-palette-summon/) **4分** — `command-palette-summon`
- [hashtag-to-pill-materialize](keep/interaction/hashtag-to-pill-materialize/) **4分** — `hashtag-to-pill-materialize`
- [input-trigger-moves](keep/interaction/input-trigger-moves/) — `cursor-performance`, `keycap-smash-cut`
- [picker-carousel-feature-cycle](keep/interaction/picker-carousel-feature-cycle/) — `picker-carousel-feature-cycle`
- [segmented-thumb-hero](keep/interaction/segmented-thumb-hero/) — `segmented-thumb-hero`
- [theme-switch-moves](keep/interaction/theme-switch-moves/) — `theme-sweep-toggle`, `palette-theme-ripple`
- [type-and-filter](keep/interaction/type-and-filter/) — `type-and-filter`
- [voice-waveform-live](keep/interaction/voice-waveform-live/) — `voice-waveform-live`

### 光效与强调 · `effects`

- [assemble-then-type-flyin](keep/effects/assemble-then-type-flyin/) **4分** — `assemble-then-type-flyin`
- [brand-frame-snap](keep/effects/brand-frame-snap/) **4分** — `brand-frame-snap`
- [dashboard-glow-highlight-pill](keep/effects/dashboard-glow-highlight-pill/) **5分** — `dashboard-glow-highlight-pill`
- [fui-hud-moves](keep/effects/fui-hud-moves/) — `reticle-lock-on`
- [glow-flyline-moves](keep/effects/glow-flyline-moves/) — `flyline-arc`, `orb-flyline-relay`
- [icon-performance-moves](keep/effects/icon-performance-moves/) — `pop-burst-confirm`, `attention-bounce`
- [impact-feedback](keep/effects/impact-feedback/) — `hit-counter`, `anime-impact`
- [light-play-moves](keep/effects/light-play-moves/) — `halation-bloom`
- [radial-ripple-phone-chips](keep/effects/radial-ripple-phone-chips/) — `radial-ripple-phone-chips`
- [scan-bracket-sweep](keep/effects/scan-bracket-sweep/) **4分** — `scan-bracket-sweep`
- [scanline-annotate-focus](keep/effects/scanline-annotate-focus/) **4分** — `scanline-annotate-focus`
- [scanline-assemble-flyin](keep/effects/scanline-assemble-flyin/) **4分** — `scanline-assemble-flyin`
- [spotlight-sweep-moves](keep/effects/spotlight-sweep-moves/) — `glow-wake-sleep-panel`, `slide-spotlight-pan`, `corner-spotlight-reveal`

### 转场 · `transition`

- [bottom-push-stack-wipe](keep/transition/bottom-push-stack-wipe/) **4分** — `bottom-push-stack-wipe`
- [card-flip-reveal](keep/transition/card-flip-reveal/) **4分** — `card-flip-reveal`
- [card-flock-tumble](keep/transition/card-flock-tumble/) **4分** — `card-flock-tumble`
- [circle-match-iris](keep/transition/circle-match-iris/) **3分** — `circle-match-iris`
- [color-block-step-wipe](keep/transition/color-block-step-wipe/) **2分** — `color-block-step-wipe`
- [cube-navigation](keep/transition/cube-navigation/) **4分** — `cube-navigation`
- [line-carry-transition](keep/transition/line-carry-transition/) — `line-carry-transition`
- [mosaic-reframe](keep/transition/mosaic-reframe/) — `mosaic-reframe`
- [page-turn-transitions](keep/transition/page-turn-transitions/) — `cube-rotate`
- [paper-plane-messenger](keep/transition/paper-plane-messenger/) — `paper-plane-messenger`
- [print-texture-transitions](keep/transition/print-texture-transitions/) — `ink-bleed-reveal`
- [shot-transitions](keep/transition/shot-transitions/) **5分** — `flash-cut`, `shot-transitions-4`, `shot-transitions-5`
- [transition-hidden-cut](keep/transition/transition-hidden-cut/) — `versus-slam`

### 运镜与空间 · `camera`

- [basic-3d-scene](keep/camera/basic-3d-scene/) **4分** — `basic-3d-scene`
- [crash-zoom-punch](keep/camera/crash-zoom-punch/) — `crash-zoom-punch`
- [cursor-flyover](keep/camera/cursor-flyover/) **4分** — `cursor-flyover`
- [depth-layer-moves](keep/camera/depth-layer-moves/) **4分** — `multiplane`, `dolly-zoom`
- [graze-face-tour](keep/camera/graze-face-tour/) **5分** — `graze-face-tour`
- [overhead-camera-moves](keep/camera/overhead-camera-moves/) — `tilt-reveal`, `overhead-tabletop-drop`
- [space-camera-moves](keep/camera/space-camera-moves/) **4分** — `exploded-view`, `drone-dive-landing`
- [steep-tilt-glide](keep/camera/steep-tilt-glide/) **5分** — `steep-tilt-glide`
- [tension-camera-moves](keep/camera/tension-camera-moves/) **4分** — `bullet-time-freeze-orbit`, `dutch-roll-to-level`, `pull-back-isolation`
- [terminal-3d](keep/camera/terminal-3d/) **5分** — `terminal-3d`

### 文字与字卡 · `typography`

- [countdown-arc-scatter](keep/typography/countdown-arc-scatter/) — `countdown-arc-scatter`
- [document-typewriter-reveal](keep/typography/document-typewriter-reveal/) — `document-typewriter-reveal`
- [flying-words](keep/typography/flying-words/) — `flying-words`
- [glitch-cycle](keep/typography/glitch-cycle/) — `glitch-cycle`
- [gradient-word-sweep](keep/typography/gradient-word-sweep/) — `gradient-word-sweep`
- [scramble](keep/typography/scramble/) — `scramble`
- [type-assembly-moves](keep/typography/type-assembly-moves/) — `drift-assembly`, `text-on-path`
- [typewriter-moves](keep/typography/typewriter-moves/) — `terminal-typewriter`, `error-retype`
- [typing-code-block](keep/typography/typing-code-block/) — `typing-code-block`
- [word-relay-filmstrip](keep/typography/word-relay-filmstrip/) — `word-relay-filmstrip`

### 节奏与蒙太奇 · `rhythm`

- [beat-cut-moves](keep/rhythm/beat-cut-moves/) — `beat-cut-accelerando`
- [beat-step-list-theme-cycle](keep/rhythm/beat-step-list-theme-cycle/) — `beat-step-list-theme-cycle`
- [montage-rhythm-moves](keep/rhythm/montage-rhythm-moves/) **4分** — `wright-triple-cut`, `domino-cascade`
- [panel-grid-moves](keep/rhythm/panel-grid-moves/) — `grid-flash-mosaic`, `comic-panel-split`
- [quad-split-parallel-scenes](keep/rhythm/quad-split-parallel-scenes/) — `quad-split-parallel-scenes`
- [smear-multiples](keep/rhythm/smear-multiples/) — `smear-multiples`
- [speed-ramp-freeze](keep/rhythm/speed-ramp-freeze/) — `speed-ramp`
- [trailer-grammar-moves](keep/rhythm/trailer-grammar-moves/) — `smash-cut`

### 数据与指标 · `data`

- [before-after-slider-scrub](keep/data/before-after-slider-scrub/) — `before-after-slider-scrub`
- [chart-live-moves](keep/data/chart-live-moves/) **4分** — `oscilloscope-stream`, `unit-dot-swarm-regroup`, `axis-rescale-shock`
- [gauge-readout-moves](keep/data/gauge-readout-moves/) — `needle-sweep-selftest`, `tape-scroll-fixed-pointer`
- [hatch-depth](keep/data/hatch-depth/) — `hatch-depth`
- [odometer-digit-roll](keep/data/odometer-digit-roll/) — `odometer-digit-roll`
- [particle-sand-fill](keep/data/particle-sand-fill/) — `particle-sand-fill`
- [scroll-brake-moves](keep/data/scroll-brake-moves/) — `changelog-scroll-brake`, `brake-reticle-lock`
- [timeline-travel](keep/data/timeline-travel/) — `timeline-travel`

### 开场与品牌 · `opening`

- [brand-ink-open](keep/opening/brand-ink-open/) — `brand-ink-open`
- [crane-rise-reveal](keep/opening/crane-rise-reveal/) — `crane-rise-reveal`
- [dataviz-landscape-open](keep/opening/dataviz-landscape-open/) **5分** — `dataviz-landscape-open`
- [fracture](keep/opening/fracture/) — `fracture`
- [letterspace-materialize](keep/opening/letterspace-materialize/) — `letterspace-materialize`
- [magician-card-flourish](keep/opening/magician-card-flourish/) **4分** — `magician-card-flourish`
- [spotlight-hero-card](keep/opening/spotlight-hero-card/) — `spotlight-hero-card`
- [stroke-segment-build](keep/opening/stroke-segment-build/) — `stroke-segment-build`

### 收尾 · `outro`

- [logo-shrink-wordmark-lockup](keep/outro/logo-shrink-wordmark-lockup/) — `logo-shrink-wordmark-lockup`
- [neon-triple-marquee](keep/outro/neon-triple-marquee/) — `neon-triple-marquee`
- [ui-strip-away-outro](keep/outro/ui-strip-away-outro/) — `ui-strip-away-outro`
- [ui-to-brand-morph](keep/outro/ui-to-brand-morph/) — `icon-flip-bloom`

## maybe — 待定

### 文字与字卡 · `typography`

- [blur-slide](maybe/typography/blur-slide/) — `blur-slide`
- [brace-expand](maybe/typography/brace-expand/) — `brace-expand`
- [cel-flash-stomp](maybe/typography/cel-flash-stomp/) — `cel-flash-stomp`
- [marker-underline-title](maybe/typography/marker-underline-title/) — `marker-underline-title`
- [outline-word-fill](maybe/typography/outline-word-fill/) — `outline-word-fill`
- [pill-slot-cycle](maybe/typography/pill-slot-cycle/) — `pill-slot-cycle`
- [split-flap-title](maybe/typography/split-flap-title/) — `split-flap-title`
- [title-demote-to-label](maybe/typography/title-demote-to-label/) — `title-demote-to-label`
- [type-assembly-moves](maybe/typography/type-assembly-moves/) — `split-text-stagger`
- [type-entrance-moves](maybe/typography/type-entrance-moves/) — `scramble-decode`, `letter-drop-physics`
- [type-rhythm-sync](maybe/typography/type-rhythm-sync/) — `font-weight-pump`, `karaoke-fill-sync`
- [vertical-word-roll-blur-cycle](maybe/typography/vertical-word-roll-blur-cycle/) — `vertical-word-roll-blur-cycle`

### 节奏与蒙太奇 · `rhythm`

- [beat-cut-moves](maybe/rhythm/beat-cut-moves/) — `paparazzi-flash`
- [montage-rhythm-moves](maybe/rhythm/montage-rhythm-moves/) — `drop-blackout-slam`
- [panel-grid-moves](maybe/rhythm/panel-grid-moves/) — `flip-grid-reflow`
- [rhythm-interrupt-moves](maybe/rhythm/rhythm-interrupt-moves/) — `jump-cut-punch-in`
- [sakuga-timing-shift](maybe/rhythm/sakuga-timing-shift/) — `sakuga-timing-shift`
- [spectrum-morph-ui](maybe/rhythm/spectrum-morph-ui/) — `spectrum-morph-ui`
- [speed-ramp-freeze](maybe/rhythm/speed-ramp-freeze/) — `freeze-annotate`
- [trailer-grammar-moves](maybe/rhythm/trailer-grammar-moves/) — `trailer-bumper`, `card-footage-cadence`

### 转场 · `transition`

- [bubble-swarm-takeover](maybe/transition/bubble-swarm-takeover/) — `bubble-swarm-takeover`
- [page-turn-transitions](maybe/transition/page-turn-transitions/) — `barn-door-split`
- [shot-transitions](maybe/transition/shot-transitions/) — `mask-wipe`
- [tear-streak-transitions](maybe/transition/tear-streak-transitions/) — `glitch-displace`
- [transition-hidden-cut](maybe/transition/transition-hidden-cut/) — `invisible-cut`, `light-leak-burn`
- [transition-travel](maybe/transition/transition-travel/) — `shared-element-morph`, `letterform-zoom`
- [white-flash-logo-simplify-cut](maybe/transition/white-flash-logo-simplify-cut/) — `white-flash-logo-simplify-cut`
- [wipe-transitions](maybe/transition/wipe-transitions/) — `clock-wipe`

### 光效与强调 · `effects`

- [aurora-bloom-bg-flip](maybe/effects/aurora-bloom-bg-flip/) — `aurora-bloom-bg-flip`
- [fui-hud-moves](maybe/effects/fui-hud-moves/) — `line-unfold-panel`
- [glow-flyline-moves](maybe/effects/glow-flyline-moves/) — `glow-orb-ambient`
- [light-play-moves](maybe/effects/light-play-moves/) — `spotlight-sweep`, `sheen-sweep`
- [line-boil](maybe/effects/line-boil/) — `line-boil`
- [slam-entrance-moves](maybe/effects/slam-entrance-moves/) — `kanada-perspective-snap`, `score-slam`, `impact-burst-kit`

### 界面登场与陈列 · `ui-entrance`

- [avatar-bracket-carousel](maybe/ui-entrance/avatar-bracket-carousel/) — `avatar-bracket-carousel`
- [bezier-source-converge-merge](maybe/ui-entrance/bezier-source-converge-merge/) — `bezier-source-converge-merge`
- [carousel-3d](maybe/ui-entrance/carousel-3d/) **3分** — `carousel-3d`
- [cloner-depth-echo](maybe/ui-entrance/cloner-depth-echo/) — `cloner-depth-echo`
- [morph-from-primitive](maybe/ui-entrance/morph-from-primitive/) — `morph-from-primitive`
- [svg-shape-morph](maybe/ui-entrance/svg-shape-morph/) — `svg-shape-morph`

### 收尾 · `outro`

- [edit-hook-moves](maybe/outro/edit-hook-moves/) — `logo-sting-button`
- [grain-dissolve](maybe/outro/grain-dissolve/) — `grain-dissolve`
- [outro-group-photo-launch](maybe/outro/outro-group-photo-launch/) — `outro-group-photo-launch`
- [ui-to-brand-morph](maybe/outro/ui-to-brand-morph/) — `input-morph-assemble`

### 数据与指标 · `data`

- [avatar-grid-radial-build-colorize](maybe/data/avatar-grid-radial-build-colorize/) — `avatar-grid-radial-build-colorize`
- [counter-confetti](maybe/data/counter-confetti/) — `counter-confetti`

### 交互与功能演示 · `interaction`

- [glass-pill-dictation-typing](maybe/interaction/glass-pill-dictation-typing/) — `glass-pill-dictation-typing`

### 开场与品牌 · `opening`

- [icon-field-colorize](maybe/opening/icon-field-colorize/) — `icon-field-colorize`

### 运镜与空间 · `camera`

- [tension-camera-moves](maybe/camera/tension-camera-moves/) — `slow-push-in`

## 上游还有没收录的实现文件

这些卡的目录里还剩下一些 `.tsx`，文件名跟你评过的任何变体都对不上——
多半是上游自己的迭代版本，没有单独进过筛选。没有判断依据就不搬，
想看的话去上游对应目录。

- `transition/shot-transitions` — PortalWipeV2.tsx, WhipBrakeReal.tsx
