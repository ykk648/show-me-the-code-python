#!/usr/bin/env python
# -*- coding: utf-8 -*-

import jieba, codecs
import jieba.posseg as pseg
import csv

names = {}
relationships = {}
lineNames = []
sortNames = []

jieba.load_userdict('dict.txt')
with codecs.open('soushen.txt', 'r', 'utf-8') as f:
    for line in f.readlines():
        poss = pseg.cut(line)
        lineNames.append([])
        for w in poss:
            #print(w.flag, w.word)
            if (w.flag == 'nr' and len(w.word) >= 2):
                lineNames[-1].append(w.word)
                # print(w.word)
                if names.get(w.word) is None :
                    names[w.word] = 0
                    relationships[w.word] = {}
                names[w.word] += 1
        sortNames = sorted(names.items(), key= lambda d:d[1], reverse= True)
        print(sortNames[:20])
    with codecs.open('sortNames.txt', 'w', 'utf-8') as f:
        for items in sortNames[:20]:
            f.write(str(items))
            f.write('\r\n')

for line in lineNames:
    for name1 in line:
        for name2 in line:
            if (name1 != name2):
                if relationships[name1].get(name2) is None:
                    relationships[name1][name2] = 1
                else:
                    relationships[name1][name2] += 1

with codecs.open('soushen_node.csv', 'w', 'utf-8') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['Id', 'Label', 'Weight'])
    for name,times in names.items():
        csv_writer.writerow([name,name,str(times)])

with codecs.open('soushen_edge.csv', 'w', 'utf-8') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['Source', 'Target', 'Weight'])
    for name,edges in relationships.items():
        for v, w in edges.items():
            if w > 3:
                csv_writer.writerow([name, v, str(w)])
