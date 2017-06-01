# coding:utf-8
import codecs


# fp = open("make1.txt")
# for lines in fp.readlines():
#     if lines.decode('gbk').encode('utf-8').find('比亚迪') != -1:
#         a =  'key'
#         with open(a, "a") as f:
#             f.write(lines)
# fp.close()

fp = open("make1.txt")
for lines in fp.readlines():
    if lines.find('cx-5') != -1:
        a = 'rc'
        with open(a, "a") as f:
            f.write(lines)
fp.close()