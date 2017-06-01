# coding:utf-8
import codecs
import re
import os

fpmake = open("newmake.txt")
for lines in fpmake.readlines():
    fpcarlist = open("carlist")
    for lines1 in fpcarlist.readlines():
        # print lines.strip().decode('gbk').encode('utf-8')
        try:
            if len(lines1.split(' '))==3:
                if lines1.split(' ')[0] != -1 and lines1.split(' ')[1] != -1 and lines1.split(' ')[2] != -1:
                    if lines.decode('gbk').encode('utf-8').find(lines1.split(' ')[0].strip()) !=-1 and lines.decode('gbk').encode('utf-8').find(lines1.split(' ')[1].strip()) != -1 and lines.decode('gbk').encode('utf-8').find(lines1.split(' ')[2].strip()) != -1:
                        lines1 = lines1.split(' ')[0] + lines1.split(' ')[1] + lines1.split(' ')[2]
                        a = lines1.strip().decode('utf-8') + '2.txt'
                        with open(a, "a") as f:
                            f.write(lines)
            else:
                if lines1.split(' ')[0]!=-1 and lines1.split(' ')[1]!=-1:
                   # print lines.find(lines1.split(' ')[0].decode('utf-8')) !=-1
                    # print lines1.split(' ')[0] in lines
                    #print lines1.split(' ')[0] in lines
                    if lines.decode('gbk').encode('utf-8').find(lines1.split(' ')[0].strip()) !=-1 and lines.decode('gbk').encode('utf-8').find(lines1.split(' ')[1].strip()) != -1:
                        lines1 = lines1.split(' ')[0] + lines1.split(' ')[1]
                        a = lines1.strip().decode('utf-8') + '2.txt'
                        with open(a, "a") as f:
                            f.write(lines)
        except:
            # print lines.decode('gbk').encode('utf-8')
            if lines.decode('gbk').encode('utf-8').find(lines1.strip()) != -1:
                a = lines1.strip().decode('utf-8') + '2.txt'
                with open(a, "a") as f:
                    f.write(lines)
            pass


fpcarlist21 = open('carlist2')
for lines1 in fpcarlist21.readlines():
    lines2 = lines1.strip()
    lines3 = lines2[:-1] + '2.txt'
    lines4 = lines2[:-1] + '1.txt'
    fp1 = open(lines3.decode('utf-8'))
    for lines in fp1.readlines():
        if lines.find('html')!=-1:
            with open(lines4.decode('utf-8'), "a") as f:
                f.write(lines.split('html')[0] + 'html'+'\n')
        else:
            with open(lines4.decode('utf-8'), "a") as f:
                f.write(lines.split('\t')[0]+'\n')


fpcarlist22 = open('carlist2')
for lines1 in fpcarlist22.readlines():
    lines2 = lines1.strip()
    lines1 = lines1.strip() + '.txt'
    lines3 = lines2[:-1]+'.txt'
    fp = open(lines1.decode('utf-8'))
    a = []
    for line in fp.readlines():
        a.append(line.strip())
    b = set(a)
    for i in b :
        with open(lines3.decode('utf-8'), "a") as f:
            f.write(i + '\n')

fp.close()
fpmake.close()
fpcarlist22.close()
fpcarlist21.close()

fpcarlist23 = open('carlist2')
for lines1 in fpcarlist23.readlines():
    lines2 = lines1.strip()
    lines1 = lines2[:-1] + '1.txt'
    lines3 = lines2[:-1] + '2.txt'
    print lines1
    print lines3
    fpcarlist23.close()
    os.remove(lines1.decode('utf-8'))
    fpcarlist23.close()
    os.remove(lines3.decode('utf-8'))
