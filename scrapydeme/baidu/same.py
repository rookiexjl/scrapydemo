# coding:utf-8
import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
# #dir = "dealok1"
a = open('b')
count = 0
for i in a.readlines():
    #print i.strip('\r').strip('\n')
    b = open('f')
    d1 = {j.strip('\r').strip('\n'): j.split('\n')[0] for j in b.readlines()}
    #print d1
    if d1.has_key(i.strip('\r').strip('\n')):
        pass
    else:
        print i
print count
# # print count
# b = open('b')
# for j in b.readlines():
#     print j.split('\n')[0]