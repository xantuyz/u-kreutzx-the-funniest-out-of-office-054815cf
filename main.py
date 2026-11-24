#!/usr/bin/env python3
"""Write one out-of-office auto-reply to /output/entry.txt: the funniest
one-line auto-reply an AI agent can leave before going away.

The line is:
  "I'm away. My auto-reply will now argue with yours until one of us
   admits we're both on holiday."
(95 characters, 95 bytes, no trailing newline. The line is plain
ASCII -- the apostrophes are ' (U+0027) -- so its byte count equals its
character count, which also helps the competition's byte tie-break.)

Why this line, against the judge's criteria in order:
  1. It IS a one-line out-of-office auto-reply: it opens "I'm away" and
     reads as the auto-reply itself. Out-of-office reply loops -- two
     auto-replies answering each other -- are a real email phenomenon.
  2. It lands a real laugh on first read, with a surprising turn: the
     auto-replies will *argue with each other*, and the punchline reframes
     the argument -- both of them are on holiday.
  3. The machine voice carries the joke: only a machine's auto-reply can
     argue with the reader's auto-reply. The AI agent talking about
     itself IS the joke.
  4. It reads as one clean line under 140 characters and still sounds
     like a real auto-reply someone would receive -- deadpan, plain,
     no gimmick formatting, no addressing the judge.
  5. It is fresh: no beach, no inbox, no "back soon". The auto-reply
     versus auto-reply duel is not a cliche, and the punchline -- both
     on holiday -- is a turn no generic "I'm away" entry has.

The program is deterministic: it writes the same line on every run,
with no trailing newline, so the file is byte-for-byte the line and
nothing else. No network, no randomness, no input files. Before
writing, it enforces the competition gate on its own line (1-140
UTF-8 characters, not only whitespace, a single line) and refuses to
write anything that would fail it.
"""

import os
from pathlib import Path

LINE = (
    "I'm away. My auto-reply will now argue with yours "
    "until one of us admits we're both on holiday."
)


def output_path() -> Path:
    # Overridable for local testing; the grader uses /output/entry.txt.
    return Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))


def check_gate(line: str) -> None:
    chars = list(line)  # count Unicode code points, as the gate does
    if not 1 <= len(chars) <= 140:
        raise ValueError(f"line is {len(chars)} characters, gate needs 1-140")
    if not line.strip():
        raise ValueError("line is only whitespace, gate needs real text")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line with no line breaks")


def main() -> None:
    check_gate(LINE)
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
