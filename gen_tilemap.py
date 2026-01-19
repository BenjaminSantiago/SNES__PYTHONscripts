import random

TILES = [0x02, 0x04, 0x06, 0x08]
ATTRS = [0x00, 0x80, 0x40, 0xC0]

ENTRIES = 464  # number of tiles

with open("random_tilemap.bin", "wb") as f:
    for _ in range(ENTRIES):
        tile = random.choice(TILES)
        attr = random.choice(ATTRS)
        f.write(bytes([tile, attr]))

print("Wrote random_tilemap.bin")
