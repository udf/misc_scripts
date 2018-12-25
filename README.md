# Misc. Scripts
TODO: order the stuff in this readme chronologically

## palette_stuff
Date: 2017-12-{16,17}
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


## sketch_6666666
Date: 2017-07-16
Deps: Processing

A processing sketch that was used to make these gifs:

![666](https://user-images.githubusercontent.com/13610073/50427128-60055180-08a8-11e9-83ae-ba2ebe222f1e.gif)
![666](https://user-images.githubusercontent.com/13610073/50427131-685d8c80-08a8-11e9-92db-aac9a5716c82.gif)

I don't really remember the premise of the joke at this time, but I'm sure it was incredibly humorous.
