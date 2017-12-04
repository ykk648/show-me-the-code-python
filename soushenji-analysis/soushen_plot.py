#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
import csv

font = FontProperties(fname= 'simfang.ttf')
nums = []
names = []

with codecs.open('sortNames.txt', 'r', 'utf-8') as f:
    for line in f.readlines():
        name = line.split('\'')[1]
        num = int(str(line)[-7:].split(')')[0])
        print(name, num)
        nums.append(num)
        names.append(name)

# _items = dict(zip(names,nums))
#
#
# with codecs.open('node.csv', 'w', 'gbk') as f:
#     for name,times in _items.items():
#         csv_writer = csv.writer(f)
#         csv_writer.writerow([name,name,str(times)])

nums = nums[:10]
names = names[:10]

plt.barh(range(len(nums)), nums[::-1], color=['skyblue','limegreen','orange'])
plt.yticks(range(len(names)), names[::-1], fontproperties= font, fontsize= 10)
plt.show()