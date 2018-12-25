import struct
import colorsys as coloursys

max_dist = (255**2 + 255**2 + 255**2)**0.5

def rgb_dist(c1, c2):
    return (abs(c1[0] - c2[0])**2 + abs(c1[1] - c2[1])**2 + abs(c1[2] - c2[2])**2)**0.5 / max_dist

def rgb_dist_fast(c1, c2):
    return abs(c1[0] - c2[0])**2 + abs(c1[1] - c2[1])**2 + abs(c1[2] - c2[2])**2

def get_v(c):
    return coloursys.rgb_to_hsv(c[0]/255, c[1]/255, c[2]/255)[2]

class Bucket:
    def __init__(self, colour, merge_threshold=0.02):
        self.colours = {colour}
        self.avg = colour
        self.merge_threshold = merge_threshold

    def add(self, colour):
        if rgb_dist(self.avg, colour) > self.merge_threshold:
            return False

        self.colours.add(colour)
        self.calc_avg()
        return True

    def calc_avg_old(self):
        r, g, b = 0, 0, 0
        for colour in self.colours:
            r += colour[0]
            g += colour[1]
            b += colour[2]

        n = len(self.colours)
        self.avg = (r / n, g / n, b / n)

    def calc_avg(self):
        colour_iter = iter(self.colours)
        best_colour = next(colour_iter)

        for colour in colour_iter:
            if get_v(colour) < get_v(best_colour):
                best_colour = colour

        self.avg = best_colour

    def round_avg(self):
        return (round(self.avg[0]), round(self.avg[1]), round(self.avg[2]))


colours = set()
with open('pal.txt') as f:
    for hex_str in f.read().split():
        colours.add(struct.unpack('BBB', bytes.fromhex(hex_str)))


merge_threshold = 0.05

while True:
    n_old_colours = len(colours)

    # construct buckets from palette
    buckets = []
    while len(colours):
        first = next(iter(colours))
        bucket = Bucket(first, merge_threshold)
        colours.remove(first)

        for colour in {colour for colour in colours if rgb_dist(first, colour) <= merge_threshold}:
            bucket.add(colour)

        colours = colours - bucket.colours
        buckets.append(bucket)

    # convert buckets to palette
    for bucket in buckets:
        colours.add(bucket.round_avg())

    # stop if we failed to reduce the palette size
    if n_old_colours == len(colours):
        break
    print(n_old_colours, '->', len(colours))

with open('reduced.txt', 'w') as f:
    for colour in colours:
        f.write('{0:02x}{1:02x}{2:02x}\n'.format(*colour))
