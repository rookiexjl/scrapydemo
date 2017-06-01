# coding:utf-8
fp1 = open('5')
for i in fp1:
     line = "https://m.baidu.com/s?word=" + i
     with open('g', 'a') as f:
         f.write("'"+line.split('\n')[0]+"',"+'\n')
