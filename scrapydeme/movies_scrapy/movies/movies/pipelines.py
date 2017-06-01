# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb

class MoviesPipeline(object):

    def process_item(self, item, spider):
        DBKWARGS = spider.settings.get('DBKWARGS')
        con = MySQLdb.connect(**DBKWARGS)
        cur = con.cursor()

        if isinstance(item, ):
            table_name = item.pop('moviesurl')
            col_str = ''
            row_str = ''
            for key in item.keys():
                col_str = col_str + " " + key + ","
                row_str = "{}'{}',".format(row_str,
                                           item[key] if "'" not in item[key] else item[key].replace("'", "\\'"))
                sql = "insert INTO {} ({}) VALUES ({}) ON DUPLICATE KEY UPDATE ".format(table_name, col_str[1:-1],
                                                                                        row_str[:-1])
            for (key, value) in item.items():
                sql += "{} = '{}', ".format(key, value if "'" not in value else value.replace("'", "\\'"))
            sql = sql[:-2]
            cur.execute(sql)  # 执行SQL
            cur.commit()  # 写入操作
        con.close()
        return item
