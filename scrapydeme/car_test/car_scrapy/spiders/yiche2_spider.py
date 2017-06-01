# coding=utf-8
from scrapy import Request
from scrapy import Spider
import demjson
from car_scrapy.items import CarScrapyItem


class YiCheAddSpider(Spider):
    name = "yiche2"
    start_urls = [
        'http://car.m.yiche.com/brandlist.html'
    ]

    def parse(self, response):
        IdList = response.xpath('//*/a/@data-id').extract()
        for i in IdList:
            url = 'http://api.car.bitauto.com/CarInfo/GetCarDataJson.ashx?action=serial&pid=' + i + \
                  '&datatype=1&callback=a'
            yield Request(url,  callback=self.parse1)

    def parse1(self, response):
        txt1 = response.xpath('/html/body/p/text()').extract()
        json_data = txt1[0][2:-1]
        for BrandList in demjson.decode(json_data):
            for child in BrandList['Child']:
                item = CarScrapyItem()
                item['brand'] = BrandList['BrandName']
                item['url'] = 'car.m.yiche.com/' + child['Allspell'] + '/'
                item['name'] = child['SerialName']
                item['type'] = None
                yield item
