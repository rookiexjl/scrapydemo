# coding:utf-8
import re

fp = open('carlist2')
for lines1 in fp.readlines():
    lines2 = lines1.strip()
    lines3 = lines2[:-1] + '2.txt'
    print lines3
    lines4 = lines2[:-1] + '1.txt'
    print lines4
    fp1 = open(lines3.decode('utf-8'))
    for lines in fp1.readlines():
        if lines.find('html')!=-1:
            print lines.split('html')[0] + 'html'
            with open(lines4.decode('utf-8'), "a") as f:
                f.write(lines.split('html')[0] + 'html'+'\n')
        else:
            print lines.split('\t')[0]
            with open(lines4.decode('utf-8'), "a") as f:
                f.write(lines.split('\t')[0]+'\n')