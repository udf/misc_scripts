# Misc. Scripts
It goes without saying that none of the code here is my best work.  
Pull requests and issues about the code won't be accepted (anything about this README is fine).

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

### reduced.txt
A reduced version of pal.txt, made with reduce.py


## sketch_6666666
Date: 2017-07-16  
Deps: Processing

A processing sketch that was used to make these gifs:

![666](https://user-images.githubusercontent.com/13610073/50427128-60055180-08a8-11e9-83ae-ba2ebe222f1e.gif)
![666](https://user-images.githubusercontent.com/13610073/50427131-685d8c80-08a8-11e9-92db-aac9a5716c82.gif)

I don't really remember the premise of the joke at this time, but I'm sure it was incredibly humorous.


## wallpaper
Date: 2017-04-20, 2017-05-21  
Deps: Processing

Matrix-esqe Arch wallpaper, and a script that modifies it to add a couple lines from [Haywyre's Endlessly](http://www.youtube.com/watch?v=MV9-VMLsNCI).

![wallpaper](https://github.com/udf/misc_scripts/raw/master/wallpaper/modifyWallpaper/data/wallpaper.png)

I still use this wallpaper at the time of writing this, however I always thought that I had lost the code.


## recaudman
Date: 2018-06-15  
Deps: g++, alsa

A C++ program that prints out [Recaman's sequence](https://oeis.org/A005132) as charactes (so, only the rightmost byte). The purpose was to pipe its output to `aplay` to see what the sequence sounds like (spoiler: it's horrible)


## utf8-plot
Date: 2018-04-13  
Deps: python, matplotlib

### utf8_err.py
Plots the UTF-8 validity of random byte arrays of length X.
![utf8_err](https://user-images.githubusercontent.com/13610073/50427294-baa0ac80-08ac-11e9-8015-6289ab050177.png)

### urandom_dist.py
Plots the distribution of os.urandom (which is used to generate the bytes in the above script).
![urandom_dist](https://user-images.githubusercontent.com/13610073/50427296-bc6a7000-08ac-11e9-99c7-19da62dc0e8c.png)


## xkcd1525
Date: 2018-07-08  
Deps: python

A [xkcd 1525](https://xkcd.com/1525) (emoji 8-ball) question/answer url generator.


## sort_by_exif_model
Date: 2018-12-27  
Deps: python

Given lots of jpeg files in the `in` directory, move those with model EXIF data to `./devs/<model>/<parent dir>/image.jpg`.

Used to sort out lots of scattered holiday pictures where the models of the cameras were not known.

Note: the `rsync` command used to grab all the jpg files from a drive was `sudo rsync --info=progress2 -rvh --include '*/' --include '*.JPG' --include '*.JPEG' --include '*.jpg' --include '*.jpeg' --exclude '*' --prune-empty-dirs /mnt/whatever/ ./jpgs/in/drive_whatever`


## line_drawer
Date: 2018-12-29  
Deps: Python, pillow, pyuserinput

Attempts to make a line drawing from an input 1-bit image.

Used for [this shitpost](https://giant.gfycat.com/VastAmusedAfricanharrierhawk.webm) (NSFW, gfycat because I can't get it into a reasonably sized gif)

(the site is http://seoi.net/penint, also NSFW)


## git_remote_https_to_ssh
Date: 2018-11-25 
Deps: Python

Recursively finds all git repositories in the working directory and replaces https remote urls with ssh

## rainbow
Date: 2018-06-04 
Deps: gcc with C++ 17 support

Uses 256-bit ANSI colour codes to make the input text display as a rainbow (a
hue sweep across the whole string)
