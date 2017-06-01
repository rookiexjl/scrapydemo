# coding:utf-8
fp = open('url8.csv')
for i in fp.readlines():
    if i.find('m.baidu')==-1 and i.find('https')==-1 :
        lines = i.split(',')[0]
        a = i.rsplit(',')[-1].split('\n')[0].decode('utf-8').strip('?')+'.txt'
        print a
        with open('result/'+ a, "a") as f:
            f.write(lines+'\n')
