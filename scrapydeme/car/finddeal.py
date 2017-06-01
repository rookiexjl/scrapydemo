# coding:utf-8
import codecs


fp = open("make3.txt")
for lines in fp.readlines():
    lines = lines.lower()
    fp1 = open("carlist")
    for lines1 in fp1.readlines():
        # print lines.strip().decode('gbk').encode('utf-8')
        try:
            if len(lines1.split(' '))==3:
                if lines1.split(' ')[0] != -1 and lines1.split(' ')[1] != -1 and lines1.split(' ')[2] != -1:
                    if lines.decode('gbk').encode('utf-8').find(lines1.split(' ')[0].strip()) !=-1 and lines.decode('gbk').encode('utf-8').find(lines1.split(' ')[1].strip()) != -1 and lines.decode('gbk').encode('utf-8').find(lines1.split(' ')[2].strip()) != -1:
                        lines1 = lines1.split(' ')[0] + lines1.split(' ')[1] + lines1.split(' ')[2]
                        a = lines1.strip().decode('utf-8') + '.txt'
                        with open('findKeyString/'+a, "a") as f:
                            f.write(lines)
            else:
                if lines1.split(' ')[0]!=-1 and lines1.split(' ')[1]!=-1:
                   # print lines.find(lines1.split(' ')[0].decode('utf-8')) !=-1
                    # print lines1.split(' ')[0] in lines
                    #print lines1.split(' ')[0] in lines
                    if lines.decode('gbk').encode('utf-8').find(lines1.split(' ')[0].strip()) !=-1 and lines.decode('gbk').encode('utf-8').find(lines1.split(' ')[1].strip()) != -1:
                        lines1 = lines1.split(' ')[0] + lines1.split(' ')[1]
                        a = lines1.strip().decode('utf-8') + '.txt'
                        with open('findKeyString/'+a, "a") as f:
                            f.write(lines)
        except:
            # print lines.decode('gbk').encode('utf-8')
            if lines.decode('gbk').encode('utf-8').find(lines1.strip()) != -1:
                a = lines1.strip().decode('utf-8') + '.txt'
                with open('findKeyString/'+a, "a") as f:
                    f.write(lines)
            pass

# fp1 = open("carlist")
# for lines1 in fp1.readlines():
#     # print lines.strip().decode('gbk').encode('utf-8')
#     print lines1.split(' ')[1].strip()
#
# fp.close()
# a = '江铃'
# b = 'a.xcar.com.cn /2760/	江铃福特		撼路者'
# print b.find(a)
