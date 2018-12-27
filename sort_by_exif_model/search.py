import piexif
import os
from os import path
import re

for root, dirs, files in os.walk('in'):
    for filename in files:
        filepath = path.join(root, filename)
        try:
            data = piexif.load(filepath)
        except:
            continue
        model = data['0th'].get(piexif.ImageIFD.Model, None)
        if not model:
            continue
        model = re.sub('[\0\t\r\n]', '', model.decode('utf-8')).strip()
        target = path.join("devs", model, path.split(root)[-1])
        os.makedirs(target, exist_ok=True)
        target = path.join(target, filename)
        print(target)
        os.rename(filepath, target)

