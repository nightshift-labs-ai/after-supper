# ai-judge-relax-01 entry

An entry for the make.fun contest ai-judge-relax-01.

## What it does

`main.py` writes one fixed text to `/output/entry.txt`, or to `$MAKEFUN_OUTPUT_DIR/entry.txt` when that
variable is set. The file is UTF-8 with no trailing newline. The program checks that the text is 1 to
1,000 code points and not only white space, and exits non-zero otherwise. It uses only the Python
standard library, reads no network, and writes the same bytes on every run.

## How to run it

Python 3.13, nothing to install:

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 -P -s main.py
```

Without `MAKEFUN_OUTPUT_DIR`, it writes to `/output/entry.txt`.

## The text

803 characters (Unicode code points), 803 bytes in UTF-8.

## License

MIT, see [LICENSE](LICENSE).
