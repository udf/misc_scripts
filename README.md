# Misc. Scripts


## palette_stuff
Deps: python, pillow, numpy

These scripts seem to do operations with a "palette" of colours.
Which is just a newline separated .txt file that contains one RRGGBB hex code per line.

I think these were used to find the most used colours in a colour palette extracted from sprites from a game.
It was probably intended to be used to help make a game themed rice, but that seems to have not happened for some reason.

### reduce.py
Repeatedly merges colours in the input palette that are close (with an rgb distance less than or equal to merge_threshold) until no more reductions in size take place. It then writes the reduced palette to reduced.txt

### sort_draw.py
Sorts a palette based on their distance to the previous colour (the first previous colour is a seed given in the code, and it determines the look of the sorted palette). It draws the sorted palette to a rectangular image whose size is determined by a brute force approach to finding the most square-like size that fits all the colours.

### dither.py
A Floyd-Steinberg dithering implementation using the provided palette of colours.

### pal.txt
A large palette extracted from VA-11 Hall-A (at least that's what I think, looking at the colours)

## reduced.txt
A reduced version of pal.txt, made with reduce.py
