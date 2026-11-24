// news-image-20261124 entrypoint (Node 22, standard library only).
//
// The entry image lives in this repo as entry.png — a front page drawn by
// draw.py from six news stories verified as first reported on Tuesday
// 24 November 2026 (see SOURCES.md). All this program does is place that
// image where the grader reads it.
//
// The grader runs with no network, so the image is shipped in the repo
// and copied, not fetched. Outside the grader, MAKEFUN_OUTPUT_DIR stands
// in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const repoDir = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const target = join(outDir, 'entry.png');

mkdirSync(outDir, { recursive: true });
const bytes = readFileSync(join(repoDir, 'entry.png'));
writeFileSync(target, bytes);
console.log(`wrote ${target} (${bytes.length} bytes)`);
