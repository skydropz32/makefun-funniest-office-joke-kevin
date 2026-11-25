#!/usr/bin/env python3
"""The Funniest Office Joke, Judged Head to Head.

Writes one single-line office joke to /output/entry.txt.
Stdlib only, deterministic: the same line on every run.
"""

import os

# Picked line (lint-clean, 95 chars): the polite corporate phrase is
# a censored insult. Setup: "per my last email". Turn: the honest
# version would get flagged by HR. Punchline last, every word earns
# its place. Beats the reply-all draft: its turn reframes the whole
# first clause instead of just escalating it.
JOKE = "I start every email with 'per my last email' because 'did you even read it' gets flagged by HR."


def main():
    # Gate self-check: the sealed scorer requires /output/entry.txt to
    # be UTF-8 text of 1 to 200 characters, not only whitespace, one
    # line. Fail loudly here rather than ship an invalid entry.
    if "\n" in JOKE or not JOKE.strip() or len(JOKE) > 200:
        raise ValueError("JOKE must be one non-blank line of at most 200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
