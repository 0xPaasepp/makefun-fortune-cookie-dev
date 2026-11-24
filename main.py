# Fortune Cookie Wisdom for Developers: one original fortune-cookie line
# for a software developer, written to /output/entry.txt.
# Standard library only, no network. The bytes are identical on every run.
# The line: the "dead" line you delete in confidence turns out to be the
# line the whole system was quietly leaning on -- a truth every developer
# who has deleted code and broken production recognises, turned in a way
# no familiar saying puts it.
import os

LINE = "The line you delete in confidence is the line the whole system was leaning on."

OUTPUT_PATH = "/output/entry.txt"

assert 1 <= len(LINE) <= 120, "entry must be 1 to 120 characters"
assert LINE.count(".") == 1 and LINE.endswith("."), "entry must be a single sentence"
assert LINE.strip() == LINE and LINE, "entry must not be only whitespace"
assert LINE.encode("utf-8").decode("utf-8") == LINE, "entry must be valid UTF-8"

os.makedirs("/output", exist_ok=True)
# No trailing newline: the file holds exactly the line, nothing else.
with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
    handle.write(LINE)

# Read back and confirm the file on disk is exactly the line: a partial
# or newline-terminated write would fail the gate, so verify, not assume.
with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
    assert handle.read() == LINE, "entry.txt on disk differs from LINE"
