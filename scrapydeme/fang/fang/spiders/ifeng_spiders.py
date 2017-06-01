# coding:utf-8
from scrapy import Request
from scrapy import Spider

from fang.items import FangItem


class LoupanSpider(Spider):

    name = "ifeng"
    start_urls = [
        'http://hz.house.ifeng.com/search'
    ]

    def parse(self, response):
        for i in range(24):
            url =  'http://hz.house.ifeng.com/search.shtml?page=' + str(i)
            yield Request(url, callback=self.parse1)

    def parse1(self, response):
        xPath = u'//*[@id="search_left_list"]/div/dl/dt/div[1]/a/@href'
        resList1 = response.xpath(xPath).extract()
        for i in resList1:
            yield Request(i, callback=self.parse2)

    def parse2(self, response):
        item = FangItem()
        item['url'] = response.url
        xPath = u'//body/div[3]/div/span/h3/text()'
        item['name'] = response.xpath(xPath).extract()
        yield item
