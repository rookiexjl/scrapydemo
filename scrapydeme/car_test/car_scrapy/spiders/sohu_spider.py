# coding=utf-8
from scrapy import Request
from scrapy import Spider
from car_scrapy.items import CarScrapyItem


class SohuSpider(Spider):
    name = "sohu"
    start_urls = [
        'http://db.m.auto.sohu.com/brand',
    ]

    def parse(self, response):
        hreflist = response.xpath('/html/body/section[3]/div/div/ul/li/a/@href').extract()
        for href in hreflist:
            url = 'http://db.m.auto.sohu.com/' + href
            yield Request(url, callback=self.parse1)

    def parse1(self, response):
        hreflist = response.xpath('//*[@id="modelListArea"]/ul/li/a/@href').extract()
        namelist = response.xpath('//*[@id="modelListArea"]/ul/li/a/div/strong/text()').extract()
        for i in range(0, len(hreflist)):
            item = CarScrapyItem()
            item['url'] = 'db.m.auto.sohu.com' + hreflist[i].split('?')[0]
            item['name'] = namelist[i]
            item['type'] = None
            item['brand'] = None
            yield item

