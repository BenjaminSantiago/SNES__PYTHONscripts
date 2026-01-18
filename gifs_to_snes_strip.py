"""

"""
from PIL import Image, ImageSequence
import sys
import os

MAX_COLORS = 16

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def collect_frames(gif_path):
    img = Image.open(gif_path)
    frames = []
    for frame in ImageSequence.Iterator(img):
        frames.append(frame.convert("RGB"))
    return frames

def collect_all_colors(frames):
    colors = set()
    for frame in frames:
        colors.update(frame.getdata())
    return colors

def build_palette(all_colors, transparent_rgb):
    if transparent_rgb not in all_colors:
        all_colors.add(transparent_rgb)

    if len(all_colors) > MAX_COLORS:
        raise ValueError(f"Too many colors ({len(all_colors)}), max is {MAX_COLORS}")

    palette = [transparent_rgb]
    for c in sorted(all_colors):
        if c != transparent_rgb:
            palette.append(c)

    while len(palette) < MAX_COLORS:
        palette.append((0, 0, 0))

    return palette

def apply_palette(img, palette):
    pal_img = Image.new("P", img.size)
    flat_palette = [v for rgb in palette for v in rgb]
    pal_img.putpalette(flat_palette)

    return img.quantize(
        palette=pal_img,
        dither=Image.NONE
    )

def make_strip(frames, palette):
    w, h = frames[0].size
    strip = Image.new("P", (w * len(frames), h))

    flat_palette = [v for rgb in palette for v in rgb]
    strip.putpalette(flat_palette)

    for i, frame in enumerate(frames):
        q = apply_palette(frame, palette)
        strip.paste(q, (i * w, 0))

    return strip

def main():
    if len(sys.argv) < 4:
        print("Usage:")
        print("  python gifs_to_snes_strip.py <#hex> <out_dir> [--merge] <gif1> <gif2> ...")
        sys.exit(1)

    transparent_hex = sys.argv[1]
    out_dir = sys.argv[2]

    merge = False
    gif_args = []

    for arg in sys.argv[3:]:
        if arg == "--merge":
            merge = True
        else:
            gif_args.append(arg)

    os.makedirs(out_dir, exist_ok=True)

    transparent_rgb = hex_to_rgb(transparent_hex)

    gif_frames = {}
    all_frames = []

    for path in gif_args:
        frames = collect_frames(path)

        # sanity check: frame sizes
        if all_frames:
            if frames[0].size != all_frames[0].size:
                raise ValueError("All GIFs must have the same frame dimensions")

        gif_frames[path] = frames
        all_frames.extend(frames)

    all_colors = collect_all_colors(all_frames)
    palette = build_palette(all_colors, transparent_rgb)

    if merge:
        strip = make_strip(all_frames, palette)
        out_path = os.path.join(out_dir, "merged_strip.gif")

        strip.save(
            out_path,
            save_all=False,
            transparency=0
        )

        print(f"Saved merged strip: {out_path}")

    else:
        for path, frames in gif_frames.items():
            strip = make_strip(frames, palette)
            name = os.path.splitext(os.path.basename(path))[0]
            out_path = os.path.join(out_dir, f"{name}_strip.gif")

            strip.save(
                out_path,
                save_all=False,
                transparency=0
            )

            print(f"Saved: {out_path}")

if __name__ == "__main__":
    main()
