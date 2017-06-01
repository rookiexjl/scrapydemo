# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
from twisted.enterprise import adbapi
from datetime import datetime
from hashlib import md5
import MySQLdb
import MySQLdb.cursors
from scrapy import signals


class JsonWithEncodingCnblogsPipeline(object):
    def __init__(self):
        self.file = codecs.open('car_scrapy.json', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()

    # 获取item
    def _get_item(self, item):
        print item
        return item


class MySQLStoreCnblogsPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbargs = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
        return cls(dbpool)

    # pipeline默认调用
    def process_item(self, item, spider):
        d = self.dbpool.runInteraction(self._do_upinsert, item, spider)
        d.addErrback(self._handle_error, item, spider)
        d.addBoth(lambda _: item)
        return d

    # 将每行更新或写入数据库中
    def _do_upinsert(self, conn, item, spider):
        urlmd5id = self._get_urlmd5id(item)
        now = datetime.now().replace(microsecond=0).isoformat(' ')
        conn.execute("""
            select 1 from car where urlmd5id = %s
        """, (urlmd5id, ))
        ret = conn.fetchone()
        if ret:
            conn.execute("""
                update car set url = %s, name = %s, brand = %s, type = %s, updated = %s where urlmd5id = %s
            """, (item['url'], item['name'], item['brand'], item['type'], now, urlmd5id))
            # print """
            # update cnblogsinfo set title = %s, description = %s, link = %s,
            # listUrl = %s, updated = %s where linkmd5id = %s
            # """, (item['title'], item['desc'], item['link'], item['listUrl'], now, linkmd5id)
        else:
            conn.execute("""
                insert into car(urlmd5id, url, name, brand, type, updated)
                values(%s, %s, %s, %s, %s, %s)
            """, (urlmd5id, item['url'], item['name'], item['brand'], item['type'], now))
            # print """
            #    insert into cnblogsinfo(linkmd5id, title, description, link, listUrl, updated)
            #    values(%s, %s, %s, %s, %s, %s)
            # """, (linkmd5id, item['title'], item['desc'], item['link'], item['listUrl'], now)

    # 获取url的md5编码
    def _get_urlmd5id(self, item):
        # url进行md5处理，为避免重复采集设计
        return md5(item['url']).hexdigest()

    # 异常处理
    def _handle_error(self, failue, item, spider):
        log.err(failure)
