import random
import re

# CONFIG
SENTINEL = 0x0000      # value to replace (e.g. 0x6969)
TILES = [0x0002, 0x0004, 0x0006, 0x0008]
FLAGS = [0x0000, 0x4000, 0x8000, 0xC000]

HEX_RE = re.compile(r'\$([0-9A-Fa-f]{4})')

def replace_word(word):
    value = int(word, 16)
    if value == SENTINEL:
        tile = random.choice(TILES)
        flag = random.choice(FLAGS)
        return f"${tile | flag:04X}"
    else:
        return f"${value:04X}"

with open("input.asm", "r") as f:
    lines = f.readlines()

for line in lines:
    if ".dw" not in line:
        print(line.rstrip())
        continue

    parts = HEX_RE.findall(line)
    replaced = [replace_word(p) for p in parts]
    print("    .dw " + ", ".join(replaced))
