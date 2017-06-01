#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import MySQLdb

conn= MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='123456',
        db ='zsp',
        charset='utf8'
        )
cur = conn.cursor()

#执行数据库的操作cur.execute
cur.execute("select url,name,brand,type from car")
rows = cur.fetchall()
for i in rows:
    if i[2] != None:
        if i[3] != None:
            line = i[0] + ',' + i[1] + ',' + i[2] + ',' + i[3]
            with open('url.csv', "a") as f:
                f.write(line + '\n')
        else:
            line = i[0] + ',' + i[1] + ',' + i[2]
            with open('url.csv', "a") as f:
                f.write(line + '\n')
    else:
        if i[3] != None:
            line = i[0] + ',' + i[1] + ',' + i[3]
            with open('url.csv', "a") as f:
                f.write(line + '\n')
        else:
            line = i[0] + ',' + i[1]
            with open('url.csv', "a") as f:
                f.write(line+'\n')
conn.close()
