from PIL import Image
from pymouse import PyMouse
import time
import math


def square_ring(n):
    # AAAAB
    # D   B
    # D   B
    # D   B
    # DCCCC
    for x in range(-n, n):
        yield x, -n
    for y in range(-n, n):
        yield n, y
    for x in range(n, -n, -1):
        yield x, n
    for y in range(n, -n, -1):
        yield -n, y


def xy_to_ind(x, y):
    return y * im.width + x


def ind_to_xy(ind):
    return ind % im.width, ind // im.width


def find_first():
    for i, p in enumerate(pixels):
        if p == 0:
            return i


def get_neigh(start):
    sx, sy = ind_to_xy(start)
    for ox, oy in search_offs:
        x = sx + ox
        y = sy + oy
        if x < 0 or x >= im.width:
            continue
        if y < 0 or y >= im.height:
            continue
        ind = xy_to_ind(x, y)
        if pixels[ind] == 1:
            continue
        return x, y, ind


def m_to(x, y):
    cx, cy = m.position()
    dx = x - cx
    dy = y - cy
    steps = max(abs(dx), abs(dy))
    if not steps:
        return
    dx /= steps
    dy /= steps
    for i in range(steps):
        m.move(round(cx + dx * (i + 1)), round(cy + dy * (i + 1)))
        #time.sleep(0.01)


search_offs = []
search_offs.extend(list(square_ring(1)))
search_offs.extend(list(square_ring(2)))
search_offs.extend(list(square_ring(3)))
search_offs.extend(list(square_ring(4)))
search_offs.extend(list(square_ring(5)))
search_offs = sorted(search_offs, key=lambda o: math.sqrt(o[0]**2 + o[1]**2))

m = PyMouse()
im = Image.open('hitler.png')

pixels = list(im.getdata())

time.sleep(2)
mx, my = m.position()
scale = 1

while True:
    first = find_first()
    if not first:
        break
    pixels[first] = 1
    targets = []
    start = first
    while True:
        v = get_neigh(start)
        if not v:
            break
        x, y, ind = v
        start = ind
        pixels[ind] = 1
        targets.append((x, y))

    if targets:
        x, y = ind_to_xy(first)
        x *= scale
        y *= scale
        print("press", mx + x, my + y)
        m.press(mx + x, my + y)
        print(len(targets))
        for x, y in targets:
            x *= scale
            y *= scale
            print("move", mx + x, my + y)
            #m_to(mx + x, my + y)
            m.move(mx + x, my + y)
        print("release", mx + x, my + y)
        m.release(mx + x, my + y)
