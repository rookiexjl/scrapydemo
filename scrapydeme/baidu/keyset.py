# coding:utf-8
import os

line_dict_uniq = dict()
with open('b','r') as fd:
    for line in fd:
        key = line.split(',')[0]
        if key not in line_dict_uniq.keys():
            line_dict_uniq[key] = line
        else:
            continue
for i in line_dict_uniq:
    line = line_dict_uniq[i]
    with open('f', "a") as f:
        f.write(line)