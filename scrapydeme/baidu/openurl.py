# coding:utf-8
# import os
import webbrowser
# for i in os.walk('result'):
#     print
dir_file = 'result/餐饮行业歌曲.txt'
fp1 = open(dir_file.decode('utf-8'))
for i in fp1:
    print i
    webbrowser.open(i)
