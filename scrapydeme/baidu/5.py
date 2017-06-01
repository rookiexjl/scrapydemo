import os
import shutil
import sys
reload(sys)
sys.setdefaultencoding('utf8')

dir = "deal"
for parent, dirnames, filenames in os.walk(dir):
    for filename in filenames:
        newname = filename.decode('gbk')
        print 'deal/'+ newname
        fp = open('deal/'+ newname)
        if len(fp.readlines()) < 5:
            with open('5', 'a') as f:
                f.write(newname.split('.txt')[0] + '\n')
            f.close()
        else:
            fp.close()
            shutil.move('deal/' + filename, 'dealok/')
