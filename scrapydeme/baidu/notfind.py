# coding:utf-8
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# dir = "deal"
# count = 0

# ftb = open('f')
# d1 = []
# for parent, dirnames, filenames in os.walk(dir):
#     for filename in filenames:
#         lines = filename.decode('gbk').encode('utf-8')
#         d1.append(lines)
#print d1
# d2 = []
# dir1 = 'deal'
# for parent, dirnames, filenames in os.walk(dir1):
#     for filename in filenames:
#         lines = filename.decode('gbk').encode('utf-8')
#         d2.append(lines)

ftb = open('b')
# d1 = []
# for parent, dirnames, filenames in os.walk(dir):
#     for filename in filenames:
#         lines = filename
#         d1.append(lines.split('.txt')[0].decode('gbk').encode('utf8'))
#
ftb1 = open('f')


count = 0
d3 = {j.strip('\r').strip('\n') for j in ftb1}
for i in ftb:
    # for j in d3:
    #     print j
    if i.strip('\r').strip('\n') not in d3:
        count += 1
        print i.split('\n')[0].decode('utf-8')
print count
# for j in d1:
#     print j

# for i in range(3):
#     d1 = {j for j in range(2)}
#     if i not in d1:
#         print i
