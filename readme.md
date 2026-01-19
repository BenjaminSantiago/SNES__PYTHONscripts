# Python scripts for SNES Tasks

Here you'll find a bunch of scripts needed for various scripts for SNES tasks. 

Right now everything is in PILLOW because they are all graphics stuff. 

Will make front ends at some point. 

## What they do: 
- *gifs_to_snes_strip.py* --> take a number of gif files, convert their frames to a single strip, set a specific color to be the 0th palette index, and be option for transparency. 
- *set_gif_transparency_index0.py* --> the above sets a specific hex value (in the palette of the image) to be the zeroth index for SNES transparency. (Photoshop orders by color "popularity" and reordering the palette seems to end up being backwards when it gets to the SNES)
- *gen_tilemap.py* --> generate a "random" tilemap that is randomly h/v or both from a specific set of 4 tiles
- *gen_with_mask.py* --> same as above except that it takes a "real" bitmap as an input, and then replaces a specific value (say 6969 with a rando tile)

## To do: 
- an SNES BGR color picker (5 bit color) 
- tilemap generator, or converter? 
- convert GIF expliclity to .pic and .clr (without PCX or PCX2SNES)
- stuff to help calculate VRAM offsets and shit like this.