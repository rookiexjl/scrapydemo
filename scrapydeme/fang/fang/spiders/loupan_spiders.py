# coding:utf-8
from scrapy import Request
from scrapy import Spider

from fang.items import FangItem


class LoupanSpider(Spider):

    name = "loupan"
    start_urls = [
        'http://m.loupan.com/hz/loupan/'
    ]

    def parse(self, response):
        for i in range(1, 84):
            url =  'http://m.loupan.com/hz/loupan/p' + str(i) +'/'
            yield Request(url, callback=self.parse1)

    def parse1(self, response):
        xPath = u'//body/a/@href'
        resList1 =  response.xpath(xPath).extract()
        for i in resList1:
            url = 'http://m.loupan.com' + i
            yield Request(url, callback=self.parse2)

    def parse2(self, response):
        item = FangItem()
        item['url'] = response.url
        xPath = u'//body/div[1]/div[1]/h2/text()'
        item['name'] = response.xpath(xPath).extract()
        yield item