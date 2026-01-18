from PIL import Image
import sys

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

if len(sys.argv) != 4:
    print("Usage: python set_gif_transparency_index0.py <#hexcolor> <input.gif> <output.gif>")
    sys.exit(1)

hex_color = sys.argv[1]
in_path = sys.argv[2]
out_path = sys.argv[3]

target_rgb = hex_to_rgb(hex_color)

img = Image.open(in_path)

# Ensure palette mode
if img.mode != "P":
    raise ValueError("GIF must be palette-based (mode 'P')")

palette = img.getpalette()
palette_colors = [tuple(palette[i:i+3]) for i in range(0, len(palette), 3)]

if target_rgb not in palette_colors:
    raise ValueError(f"Color {hex_color} not found in palette")

target_index = palette_colors.index(target_rgb)

# Swap target color with index 0
palette_colors[0], palette_colors[target_index] = (
    palette_colors[target_index],
    palette_colors[0],
)

# Apply new palette
flat_palette = [v for rgb in palette_colors for v in rgb]
img.putpalette(flat_palette)

# Swap pixel indices 0 <-> target_index
pixels = img.load()
w, h = img.size

for y in range(h):
    for x in range(w):
        if pixels[x, y] == 0:
            pixels[x, y] = target_index
        elif pixels[x, y] == target_index:
            pixels[x, y] = 0

img.save(out_path, transparency=0)

print(f"Saved: {out_path}")
print(f"Transparency color {hex_color} is now palette index 0")
