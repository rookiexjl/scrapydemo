# coding=utf-8
from scrapy import Request
from scrapy import Spider

from car_scrapy.items import CarScrapyItem


class KacheSpider(Spider):
    name = "360che"
    start_urls = [
        'http://product.360che.com/'
    ]

    def parse(self, response):
        resList1 = response.xpath(u'//h2/a/@href').extract()
        if len(resList1) > 0:
            for i in resList1:
                yield Request('http://product.360che.com'+i, callback=self.parse1)
        resList1 = response.xpath(u'//div[@class="article-page"]/a[last()]/@href').extract()
        if len(resList1) > 0:
            yield Request('http://product.360che.com'+resList1[0], callback=self.parse)

    def parse1(self,response):
        item = CarScrapyItem()
        item['url'] = response.url.replace("http://product.", "http://product.m.")
        x_path = u'/html/body/div[6]/div[1]/div[2]/div/a[3]/text()'
        resList1 = response.xpath(x_path).extract()
        item['brand'] = resList1[0]
        x_path = u'/html/body/div[6]/div[1]/div[2]/div/a[4]/text()'
        resList1 = response.xpath(x_path).extract()
        item['name'] = resList1[0]
        x_path = u'/html/body/div[6]/div[1]/div[2]/div/a[5]/text()'
        resList1 = response.xpath(x_path).extract()
        item['type'] = resList1[0]
        yield item
