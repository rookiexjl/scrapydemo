# coding=utf-8
from scrapy import Request
from scrapy import Spider

from car_scrapy.items import CarScrapyItem


class KacheSpider(Spider):
    name = "truck"
    start_urls = [
        'http://m.chinatruck.org/brand/'
    ]
    def parse(self, response):
        xPath = u'//div[@class="brand-name"]/a/@href'
        resList1 = response.xpath(xPath).extract()
        if len(resList1) > 0:
            for i in resList1:
                yield Request(i, callback=self.parse1)

    def parse1(self, response):
        xpath = u'/html/body/div[2]/div/div[@class="brand-sellists"]/ul/li/a/@href'
        resList1 = response.xpath(xpath).extract()
        for i in resList1:
            if i.find('http')==-1:
                i = 'http://m.chinatruck.org' + i
            yield Request(i, callback=self.parse2)

    def parse2(self, response):
        item = CarScrapyItem()
        xpath = u'/html/body/div[2]/div/div/div/div[@class="news-tit"]/h2/a/text()'
        resList2 = response.xpath(xpath).extract()
        xpath = u'/html/body/div[2]/div/div/div/div[@class="news-tit"]/h2/a/@href'
        resList3 = response.xpath(xpath).extract()
        for i in resList2:
            if i.find('video') == -1:
                item['name'] = i
                item['brand'] = unicode(item['name'].split(' ')[0])
        for i in resList3:
            if i.find('video') == -1:
                item['url'] = i
        yield item
