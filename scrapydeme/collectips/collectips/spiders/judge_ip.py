# coding:utf-8
import urllib2
import MySQLdb
from hashlib import md5


def judge_ip():
    '''Judge IP can use or not'''
    fp1 = open('ip')
    for record in fp1:
        http_url = "http://www.baidu.com/"
        https_url = "https://www.alipay.com/"
        # proxy_type = record.split('\t')[3].strip('\r').strip('\n').lower()
        proxy_type = 'http'
        url = http_url if proxy_type == "http" else https_url
        # proxy = "%s:%s" % (record.split('\t')[0], record.split('\t')[1])
        proxy = record.strip('\r').strip('\n')
        try:
            req = urllib2.Request(url=url)
            req.set_proxy(proxy, proxy_type)
            response = urllib2.urlopen(req, timeout=30)
        except Exception, e:
            print "Request Error:", e
        else:
            code = response.getcode()
            if 200 <= code < 300:
                print 'Effective proxy', proxy
                # with open('ip', 'a') as f:
                #     f.write(proxy+'\n')
                #inDB(record)
            else:
                print 'Invalide proxy', proxy


def inDB(record):

    IP = record.split('\t')[0]
    PORT = record.split('\t')[1]
    DEGREE_OF_ANONYMITY = None
    TYPE = record.split('\t')[2].strip('\r').strip('\n')
    GET_POST = None
    POSITION = None
    SPEED = None
    LAST_CHECK_TIME = None
    ipmd5id = md5(record.split('\t')[0]).hexdigest()

    con = MySQLdb.connect('localhost', 'root', '123456', 'ippool')
    cur = con.cursor()
    cur.execute("""select 1 from proxy where ipmd5id = %s""", (ipmd5id, ))
    ret = cur.fetchone()

    if ret:
        sql = ("update proxy set IP = %s,PORT =%s,DEGREE_OF_ANONYMITY=%s,TYPE=%s,GET_POST=%,POSITION=%,SPEED=%s,"
               "LAST_CHECK_TIME=%s where ipmd5id = %s")
        lis = (IP, PORT, DEGREE_OF_ANONYMITY, TYPE, GET_POST, POSITION, SPEED, LAST_CHECK_TIME, ipmd5id)
    else:
        sql = ("insert into proxy(ipmd5id,IP,PORT,DEGREE_OF_ANONYMITY,TYPE,GET_POST,POSITION,SPEED,"
               "LAST_CHECK_TIME) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        lis = (ipmd5id, IP, PORT, DEGREE_OF_ANONYMITY, TYPE, GET_POST, POSITION, SPEED, LAST_CHECK_TIME)
    try:
        cur.execute(sql, lis)
    except Exception, e:
        print "Insert error:", e
        con.rollback()
    else:
        con.commit()
    cur.close()
    con.close()

judge_ip()
