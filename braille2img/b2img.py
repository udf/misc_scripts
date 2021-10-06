from PIL import Image

with open('amogus.txt') as f:
  lines = [l.strip() for l in f]

height = len(lines) * 4
width = max(map(len, lines)) * 2
im = Image.new('RGB', (width, height))

colors = ((0,0,0), (255,255,255))

for iline, line in enumerate(lines):
  for ichar, char in enumerate(line):
    x = ichar * 2
    y = iline * 4

    bits = ord(char) & 0xFF

    im.putpixel((x + 0, y + 0), colors[(bits >> 0) & 1])
    im.putpixel((x + 0, y + 1), colors[(bits >> 1) & 1])
    im.putpixel((x + 0, y + 2), colors[(bits >> 2) & 1])
    im.putpixel((x + 1, y + 0), colors[(bits >> 3) & 1])
    im.putpixel((x + 1, y + 1), colors[(bits >> 4) & 1])
    im.putpixel((x + 1, y + 2), colors[(bits >> 5) & 1])
    im.putpixel((x + 0, y + 3), colors[(bits >> 6) & 1])
    im.putpixel((x + 1, y + 3), colors[(bits >> 7) & 1])

im.save('out.png')