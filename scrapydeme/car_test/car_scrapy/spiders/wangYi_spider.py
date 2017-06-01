# coding=utf-8
from scrapy import Request
from scrapy import Spider

from car_scrapy.items import CarScrapyItem


class WangYSpider(Spider):
    name = "163"
    start_urls = [
        'http://auto.3g.163.com/'
    ]

    def parse(self, response):
        xPath = u'//div[@class="list-group"]/ul/li/@_brandurl'
        resList1 = response.xpath(xPath).extract()
        if len(resList1)>0:
            for i in resList1:
                yield Request('http://auto.3g.163.com'+i, callback=self.parse1)

    def parse1(self,response):
        xPath = u"//a[@class='car_link']/@href"
        resList1 = response.xpath(xPath).extract()
        for i in resList1:
            yield Request('http://auto.3g.163.com'+i, callback=self.parse2)

    def parse2(self,response):
        item = CarScrapyItem()
        item['url']= response.url.replace('#cc0101', '').replace('http://auto.3g.163.com', 'auto.3g.163.com')
        xPath = u"//*[@id='wrap']/div[3]/h2/span/text()"
        resList1 = response.xpath(xPath).extract()
        item['name']=resList1[0]
        item['brand'] = None
        item['type'] = None
        yield item
