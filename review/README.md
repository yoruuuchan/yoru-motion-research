# Review console

One console, one HTML file, several datasets. `index.html` knows nothing about
Locomotion or Video Shotcraft — everything source-specific lives in
`datasets/*.json`, produced by `scripts/build-review-datasets.py`. Adding another
upstream library means adding an adapter there, not another page.

## Run it

```bash
python review/serve.py
```

That serves the **parent** directory of this repository and opens
`http://127.0.0.1:8899/yoru-motion-research/review/`. The parent is the server
root because the preview media lives in sibling checkouts and is never copied in
here:

| dataset          | candidates | preview source                                                     |
| ---------------- | ---------- | ------------------------------------------------------------------ |
| `locomotion`     | 427        | `../locomotion-free/public/videos/`                                 |
| `video-shotcraft`| 209        | `../video-shotcraft/gallery/media/`, falling back to GitHub Pages   |

Opening `index.html` straight from disk does not work: the datasets are loaded
with `fetch()`, which browsers block on `file://`.

## Reviewing

Pick a dataset in the first toolbar select. Each card is one previewable
style/shot: watch it, then `keep` / `maybe` / `reject`, optionally a 1–5 score
and a note. Clicking the same verdict again clears it.

Every change is written to `localStorage` immediately, keyed per dataset
(`yoru-locomotion-curation-v1`, `yoru-shotcraft-curation-v1`), along with the
current search / filter / page so a refresh drops you back where you were. The
Locomotion key and record shape are the same ones
`locomotion-free/preview.html` used, so both consoles read each other's progress.

Locomotion also ships seeded with the 427 verdicts from
`curation/locomotion-2026-08-19.json.bz2`, so the historical review is visible in
any browser. A verdict you change overrides the seed; clearing it back to empty
restores the seed value.

`export json` writes **every** candidate — rated or not — as
`yoru-motion-curation/v2`, with the provenance needed to trace a verdict back to
its upstream shot (repo, commit, card, style, category, recipe path, preview
URL). `export md` writes the same thing as a readable list.

## Ingesting an export

```bash
python scripts/import-curation-export.py ~/Downloads/video-shotcraft-curation-2026-08-20.json
```

Validates the export against its dataset, archives the uploaded bytes as
`curation/<dataset>-<date>.json.bz2`, and generates the `-liked` / `-maybe` /
`-rejected` views next to it. It refuses to overwrite an existing snapshot
without `--force`.

## Rebuilding the datasets

```bash
python scripts/build-review-datasets.py          # regenerate
python scripts/build-review-datasets.py --check  # fail if committed output drifted
```

The Video Shotcraft adapter reads `gallery/api/library.json` and compares it to
the upstream commit pinned in the script; a refreshed checkout that no longer
matches is reported rather than silently labelled with the wrong commit.
