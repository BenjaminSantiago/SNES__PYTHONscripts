# Python scripts for SNES Tasks

Here you'll find a bunch of scripts needed for various scripts for SNES tasks. 

Right now everything is in PILLOW because they are all graphics stuff. 

Will make front ends at some point. 

## What they do: 
- *gifs_to_snes_strip.py* --> take a number of gif files, convert their frames to a single strip, set a specific color to be the 0th palette index, and be option for transparency. 
- *set_gif_transparency_index0.py* --> the above sets a specific hex value (in the palette of the image) to be the zeroth index for SNES transparency. (Photoshop orders by color "popularity" and reordering the palette seems to end up being backwards when it gets to the SNES)
