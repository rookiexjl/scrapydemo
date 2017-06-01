# coeding:utf-8
import os
dirname = 'dealok'
for parent, dirnames, filenames in os.walk(dirname):
    for filename in filenames:
        fp = open('dealok/'+filename)
        for i in fp.readlines():
            if i.find('baidu')!=-1 or i.find('"')!=-1:
                print filename.decode('gbk')
