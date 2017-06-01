# coeding:utf-8
import os
dirname = 'deal'
for parent, dirnames, filenames in os.walk(dirname):
    for filename in filenames:
        print filename.decode('gbk').split('.txt')[0]
