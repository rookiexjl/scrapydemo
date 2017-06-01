# utf-8
fp1 = open('a.txt')
for i in fp1:
    with open('dirname/' + i.split('\t')[-1].strip('\n')+'.txt', 'a') as f:
        f.write(i)