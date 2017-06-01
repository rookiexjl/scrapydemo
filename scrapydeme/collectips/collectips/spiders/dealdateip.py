# coding:utf-8
fp1 = open('ip1')
for i in fp1:
    if i.find('Cn') != -1:
        if i.find('HTTPS') == -1:
            print i.split('Cn')[1].split('\t')[5]
            with open('ip2', 'a') as f:

                line = i.split('Cn')[1].split('\t')[1] + '\t' + i.split('Cn')[1].split('\t')[2] + '\t' + \
                       i.split('Cn')[1].split('\t')[4] + '\t' + i.split('Cn')[1].split('\t')[5]
                f.write(line)
