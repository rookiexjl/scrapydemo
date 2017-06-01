import os
dir = 'a'
for parent, dirnames, filenames in os.walk(dir):
    for filename in filenames:
        print filename.split('.txt')[0].decode('gbk')