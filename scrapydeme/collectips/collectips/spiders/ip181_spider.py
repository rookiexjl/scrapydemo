# -*- coding: utf-8 -*-
import scrapy
from collectips.items import CollectipsItem
import re

class KuaiDaiLiSpider(scrapy.Spider):
    name = "kuaidaili"
    start_urls = ['http://www.ip181.com/']
    # for i in range(1, 100):
    #     # print '**********************************'
    #     # print "http://www.kuaidaili.com/free/inha/%s/" % i
    #     start_urls.append("http://www.kuaidaili.com/free/inha/%s/" % i)

    def parse(self, response):
        ip_list = response.xpath('//*/table/tbody')
        trs = ip_list.xpath('tr')
        items = []
        for ip in trs:
            if ip.xpath('td[4]/text()')[0].extract() == 'HTTP, HTTPS':
                pass
            else:
                pre_item = CollectipsItem()
                pre_item['IP'] = ip.xpath('td[1]/text()')[0].extract()
                pre_item['PORT'] = ip.xpath('td[2]/text()')[0].extract()
                pre_item['DEGREE_OF_ANONYMITY'] = ip.xpath('td[3]/text()')[0].extract()
                pre_item['TYPE'] = ip.xpath('td[4]/text()')[0].extract()
                pre_item['GET_POST'] = None
                pre_item['POSITION'] = ip.xpath('td[6]/text()')[0].extract().strip()
                pre_item['SPEED'] = ip.xpath('td[5]/text()').re('\d{0,2}\.\d{0,}|\d')[0]
                pre_item['LAST_CHECK_TIME'] = ip.xpath('td[7]/text()')[0].extract()
                items.append(pre_item)
        return items
