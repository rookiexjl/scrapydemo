# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
from hashlib import md5

class CollectipsPipeline(object):

    def process_item(self, item, spider):
        ipmd5id = self._get_ipmd5id(item)
        DBKWARGS = spider.settings.get('DBKWARGS')
        con = MySQLdb.connect(**DBKWARGS)
        cur = con.cursor()
        cur.execute("""
            select 1 from proxy where ipmd5id = %s
        """, (ipmd5id, ))
        ret = cur.fetchone()
        if ret:
            sql = ("update proxy set IP = %s,PORT =%s,DEGREE_OF_ANONYMITY=%s,TYPE=%s,GET_POST=%,POSITION=%,SPEED=%s,"
                   "LAST_CHECK_TIME=%s where ipmd5id = %s")
            lis = (item['IP'], item['PORT'], item['DEGREE_OF_ANONYMITY'], item['TYPE'], item['GET_POST'],
                   item['POSITION'], item['SPEED'], item['LAST_CHECK_TIME'], ipmd5id)
        else:
            sql = ("insert into proxy(ipmd5id,IP,PORT,DEGREE_OF_ANONYMITY,TYPE,GET_POST,POSITION,SPEED,"
                   "LAST_CHECK_TIME) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)")
            lis = (ipmd5id, item['IP'], item['PORT'], item['DEGREE_OF_ANONYMITY'], item['TYPE'], item['GET_POST'],
                   item['POSITION'], item['SPEED'], item['LAST_CHECK_TIME'])
        try:
            cur.execute(sql, lis)
        except Exception, e:
            print "Insert error:", e
            con.rollback()
        else:
            con.commit()
        cur.close()
        con.close()
        return item

    # 获取url的md5编码
    def _get_ipmd5id(self, item):
        # url进行md5处理，为避免重复采集设计
        return md5(item['IP']).hexdigest()
