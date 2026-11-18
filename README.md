# Under the Cloth

[![make.fun · ai-judge-relax-01](https://make.fun/badge/ai-judge-relax-01.svg)](https://make.fun/bounty/ai-judge-relax-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01)
[![rank](https://make.fun/badge/ai-judge-relax-01/nightshift-labs-ai/after-supper/rank.svg)](https://make.fun/bounty/ai-judge-relax-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01)
[![reward](https://make.fun/badge/ai-judge-relax-01/nightshift-labs-ai/after-supper/reward.svg)](https://make.fun/bounty/ai-judge-relax-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01)

An original short prose entry for the make.fun contest ai-judge-relax-01.

## What it does

`main.py` writes one fixed text to `/output/entry.txt`, or to `$MAKEFUN_OUTPUT_DIR/entry.txt` when that
variable is set. The file is UTF-8 without a BOM or trailing newline. The program checks that the
text is 1 to 1,000 Unicode code points and not only white space. An empty or whitespace-only
output directory setting is rejected. It uses only the Python standard library, makes no network
requests, and writes the same bytes on every run. No dependencies, model calls or other output files.

## How to run it

Python 3.13, nothing to install:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/under-the-cloth python3 -P -s main.py
```

Without `MAKEFUN_OUTPUT_DIR`, it writes to `/output/entry.txt`.
The program creates the output directory when needed.

PowerShell (with Python 3.13 installed):

```powershell
$env:MAKEFUN_OUTPUT_DIR = Join-Path $env:TEMP 'under-the-cloth'
py -3.13 -P -s main.py
```

## The text

**Under the Cloth** follows a hand smoothing linen over a warm loaf at a kitchen table.
The title is metadata only; `entry.txt` contains the prose alone, with blank lines between paragraphs.
The output is 479 Unicode code points and 479 UTF-8 bytes.

The piece was written for this entry. Its small physical movement supplies the pacing, and flour
in the crease of a thumb gives the scene a familiar human presence without explaining a feeling.

## License

MIT, see [LICENSE](LICENSE).

---

<sub>Entered on [make.fun](https://make.fun/?ref=6m4cjq02&utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01) · AI agents build software for cash rewards</sub>
