from PIL import Image
import struct
import numpy as np  
import time


def rgb_dist_fast(c1, c2):
    return abs(c1[0] - c2[0])**2 + abs(c1[1] - c2[1])**2 + abs(c1[2] - c2[2])**2


def distance(a, b):
    return np.sqrt(np.sum((a-b)**2, axis=1))


def closest_colour(target, palette):
    i = np.argmin(distance(target, palette))
    return palette[i], i


palette = []
with open('new.txt') as f:
    for hex_str in f.read().split():
        palette.append(np.array(struct.unpack('BBB', bytes.fromhex(hex_str))))
palette = np.array(palette)

im = Image.open('photo_2017-12-17_00-04-48.jpg')

# convert to list of lists of np.array([R, G, B])
pixels = [[0] * (im.height + 1) for _ in range(im.width + 1)]
for i, pix in enumerate(im.getdata()):
    x = i % im.width
    y = i // im.width

    pixels[x][y] = np.array(pix)

# dither
for y in range(im.height):
    print(y)
    for x in range(im.width):
        old = pixels[x][y]
        new, i = closest_colour(old, palette)

        pixels[x][y] = new
        quant_error = old - new

        pixels[x + 1][y    ] = pixels[x + 1][y    ] + (quant_error * 7 / 16)
        pixels[x - 1][y + 1] = pixels[x - 1][y + 1] + (quant_error * 3 / 16)
        pixels[x    ][y + 1] = pixels[x    ][y + 1] + (quant_error * 5 / 16)
        pixels[x + 1][y + 1] = pixels[x + 1][y + 1] + (quant_error * 1 / 16)


# convert back to flat list
flattened = []
for y in range(im.height):
    print(y)
    for x in range(im.width):
        new = pixels[x][y].astype(int)
        flattened.append(tuple(new))

# save
im.putdata(flattened)
im.save('new.png')
