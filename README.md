# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/Allenhua/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/Allenhua/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

One image summing up the world's news of **Tuesday, 24 November 2026** — a
newspaper-style front page with six verified stories from that day: the
air-raid alert on South Korea's Ulleung Island, Russian strikes on drone
sites in Sumy, NATO's space-defence warning, Trump halting the Iowa
detonation, Sheikh Hasina's planned return to Bangladesh, and a magnitude
4.1 earthquake in Pakistan — plus a ticker of the day's other news.

The image is drawn programmatically by `draw.py` (Python + Pillow): every
word is rendered as crisp text, so nothing is garbled at any size. The
stories and their sources are listed in `SOURCES.md`; every story was
verified as first reported on 24 November 2026.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
# writes out/entry.png (1024x1024 PNG, under 1 MiB)
```

To redraw the image from scratch: `python3 draw.py` (needs Pillow).

---

<sub>Entered on [make.fun](https://make.fun/?ref=nimble-marten-40-8602&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
