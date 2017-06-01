# coding:utf-8
fp = open('carlist2')
for lines1 in fp.readlines():
    print lines1
    lines2 = lines1.strip()
    lines1 = lines1.strip() + '.txt'
    print lines2
    lines3 = lines2[:-1]+'.txt'
    fp = open(lines1.decode('utf-8'))
    a = []
    for line in fp.readlines():
        print a.append(line.strip())
    b = set(a)
    print '***************'
    for i in b :
        with open(lines3.decode('utf-8'), "a") as f:
            f.write(i + '\n')

