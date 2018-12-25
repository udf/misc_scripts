import struct
from math import floor
from PIL import Image

max_dist = (255**2 + 255**2 + 255**2)**0.5

def rgb_dist(c1, c2):
    return (abs(c1[0] - c2[0])**2 + abs(c1[1] - c2[1])**2 + abs(c1[2] - c2[2])**2)**0.5 / max_dist

def rgb_dist_fast(c1, c2):
    return abs(c1[0] - c2[0])**2 + abs(c1[1] - c2[1])**2 + abs(c1[2] - c2[2])**2

def get_closest(target, colours):
    iterator = iter(colours)
    closest = next(iterator)
    closest_dist = rgb_dist_fast(target, closest)

    for this_colour in iterator:
        this_dist = rgb_dist_fast(target, this_colour)
        if this_dist < closest_dist:
            closest_dist = this_dist
            closest = this_colour

    return closest

name = 'reduced'

palette = []
with open(f'{name}.txt') as f:
    for hex_str in f.read().split():
        palette.append(struct.unpack('BBB', bytes.fromhex(hex_str)))

seed = (0, 0, 0)
colours = [get_closest(seed, palette)]
palette.remove(colours[0])
colours.append(get_closest(colours[-1], palette))
palette.remove(colours[-1])

while palette:
    print(len(palette))
    colour = palette.pop()

    min_dist = rgb_dist(colour, colours[0]) * 2
    best_pos = 0

    for i in range(1, len(colours)):
        dist = rgb_dist(colour, colours[i - 1]) + rgb_dist(colour, colours[i])
        if dist < min_dist:
            min_dist = dist
            best_pos = i

    dist = rgb_dist(colour, colours[-1]) * 2
    if dist < min_dist:
        best_pos = len(colours)

    colours.insert(best_pos, colour)


# compute best size
width = floor(len(colours)**0.5)
height = width

while width * height < len(colours):
    if width < height:
        width += 1
    else:
        height += 1

im = Image.new('RGBA', (width, height))
im.putdata(colours)
im.save(f'{name}_sorted.png')
