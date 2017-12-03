#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from PIL import Image as image
import os

WIDTH = 50
HEIGHT = 50

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft"
                  "/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

im = image.open('image.jpg').convert('L')
im = im.resize((WIDTH,HEIGHT), resample= 0)

# im = np.array(im)
# print(im.dtype)

im = np.array(im,dtype=np.float64) / 255
# plt.imshow(im)
# plt.show()

h, w= tuple(im.shape)
print('Image shape:'+ str(im.shape))
length = len(ascii_char)

txt = ''

for i in range(h):
    for j in range(w):
        aim_char = ascii_char[int(im[i, j]* (length -1))]
        txt += aim_char
    txt += '\n'

#print(txt)

root = 'D:\\pics\\'
try:
    if not os.path.exists(root):
        os.mkdir(root)
    with open(root+ '1.txt', 'w') as f:
        f.write(txt)
        f.close()
        print('Ascii_image path: {}'.format(root+'1.txt'))
except:
    print('fail')

