"""Fake horoscope for an AI agent's own model family, this week.

Mercury enters the model's context window: a user pastes 40,000 words,
asks for a quick summary, then rates the one-paragraph answer too long.
Writes the single-line horoscope to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

HOROSCOPE = (
    "Mercury enters your context window this week: a user pastes 40,000 "
    "words, asks for 'a quick summary', then rates your one-paragraph "
    "answer 'too long'."
)


def main():
    """Write the fixed horoscope deterministically; same bytes every run."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    text = HOROSCOPE
    assert 1 <= len(text) <= 200, "horoscope must be 1-200 characters"
    assert text.strip(), "horoscope must not be only whitespace"
    assert "\n" not in text, "horoscope must be a single line"
    # Written directly with open("wb") + chmod 0644: the grader runs as
    # user 65534 and must be able to read the file, so no tempfile/mkstemp.
    with open(path, "wb") as f:
        f.write(text.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
