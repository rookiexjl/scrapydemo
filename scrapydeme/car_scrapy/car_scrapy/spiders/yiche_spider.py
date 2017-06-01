# coding=utf-8
from scrapy import Request
from scrapy import Spider

from car_scrapy.items import CarScrapyItem


class YicheSpider(Spider):
    name = "yiche"
    start_urls = [
        'http://car.bitauto.com/brandlist.html'
    ]
    def parse(self, response):
        xPath = u'//div[@class="brandname"]/a/@href'
        resList1 = response.xpath(xPath).extract()

        for i in range(1, len(resList1) + 1):
            # for i in range(1,2):
            carURL = 'http://car.bitauto.com'+resList1[i - 1]
            #print carURL

            # baseItem['brand'] = carURL
            # baseItem['brand'] = carURL meta={'brand': baseItem},
            yield Request(carURL,  callback=self.parse_detail)
    def parse_detail(self,response):

        xPath = u'//*[@id="data_table_MasterSerialList_0"]/div/ul/li[1]/a/@href'
        resList1 = response.xpath(xPath).extract()
        for i in range(1, len(resList1) + 1):
            # for i in range(1,2):
            carURL = 'http://car.bitauto.com'+resList1[i - 1]
            print carURL
            print '================================'

            # baseItem['brand'] = carURL
            # baseItem['brand'] = carURL meta={'brand': baseItem},
            yield Request(carURL,  callback=self.item)
    def item(self,response):
        baseItem = CarScrapyItem()
        xPath = u'//*[@id="topBox"]/div[1]/div/div/strong/text()'
        name = response.xpath(xPath).extract()

        baseItem['name'] = name[0]
#'preceding-sibling::*[1]'
        xPath = u'//*[@id="topBox"]/div[1]/div/div/strong/preceding-sibling::*[1]/text()'
        brand = response.xpath(xPath).extract()

        baseItem['brand'] = brand[0]

        URL=response.url.replace('http://car.bitauto.com','car.m.yiche.com')
        baseItem['url'] = URL
        print baseItem
        yield baseItem
