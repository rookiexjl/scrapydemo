# coding=utf-8
from scrapy import Request
from scrapy import Spider

from kache.items import KacheItem


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
        xpath = u'//div[@class="brand-sellists"]/ul/li/a/@href'
        resList1 = response.xpath(xpath).extract()
        for i in resList1:
            if i.find('http')==-1:
                i = 'http://m.chinatruck.org/' + i
            yield Request(i,callback=self.parse2)

    def parse2(self,response):
        item=KacheItem()
        xpath = u'//div[@class="news-tit"]/h2/a/text()'
        resList2 = response.xpath(xpath).extract()
        xpath = u'//div[@class="news-tit"]/h2/a/@href'
        resList3 = response.xpath(xpath).extract()
        for i in resList2:
            item['name'] = i
            item['brand'] = unicode(item['name'].split(' ')[0])
        for i in resList3:
            item['url'] = i
        yield item
        # for i in range(1, len(resList2)):
        #     print i
        # /html/body/div[2]/div/div[4]
        # item['url']=response.url
        # xPath = u'/html/body/div[6]/div[1]/div[2]/div/a[3]/text()'
        # resList1 = response.xpath(xPath).extract()
        # item['brand']=resList1[0]
        # xPath = u'/html/body/div[6]/div[1]/div[2]/div/a[4]/text()'
        # resList1 = response.xpath(xPath).extract()
        # item['name'] = resList1[0]
        # xPath = u'/html/body/div[6]/div[1]/div[2]/div/a[5]/text()'
        # resList1 = response.xpath(xPath).extract()
        # item['type'] = resList1[0]
        # yield item
