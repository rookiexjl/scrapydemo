import os
import shutil
import sys
reload(sys)
sys.setdefaultencoding('utf8')

dir = "dealok1"
for parent, dirnames, filenames in os.walk(dir):
    for filename in filenames:
        newname = filename.decode('gbk')
        fp = open('dealok1/'+ newname)
        for i in fp.readlines():
            if i.find('"') != -1:
                with open('dealokmbaidu/'+newname, 'a') as f:
                    f.write(i)



# import os
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
#
# dir = "dealok1"
# count = 0
# for parent, dirnames, filenames in os.walk(dir):
#     for filename in filenames:
#         print filename.split('.txt')[0].decode('gbk')
#         count += 1
# print count