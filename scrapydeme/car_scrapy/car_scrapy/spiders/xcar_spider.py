# coding=utf-8
from scrapy import Request
from scrapy import Spider

from car_scrapy.items import CarScrapyItem


class YicheSpider(Spider):
    name = "xcar"
    start_urls = [
        'http://newcar.xcar.com.cn/price/'
    ]

    def parse(self, response):

        xPath = u'//div[@class="item_list"]/a/@href'
        resList1 = response.xpath(xPath).extract()
        for i in resList1:
            yield Request('http://newcar.xcar.com.cn'+i,callback=self.parse1)

    def parse1(self,response):
        item=CarScrapyItem()
        #http://a.xcar.com.cn/2490/
        item['url']=response.url.replace('http://newcar.xcar.com.cn','a.xcar.com.cn')
        xPath = u"//div[@class='tt_h1']/span[2]/text()"
        resList1 = response.xpath(xPath).extract()
        item['brand']= resList1[0].replace('-','')

        xPath = u"//div[@class='tt_h1']/h1/text()"
        resList1 = response.xpath(xPath).extract()
        item['name']=resList1[0]

        print item
        yield item
    #     yield Request('http://newcar.xcar.com.cn'+resList1[0],meta={'item':item},callback=self.parse2)
    #
    # def parse2(self,response):
    #     item=response.meta['item']
