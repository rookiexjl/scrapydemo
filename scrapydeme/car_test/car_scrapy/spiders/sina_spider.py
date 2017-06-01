# coding=utf-8
from scrapy import Request
from scrapy import Spider
import demjson
import re
from car_scrapy.items import CarScrapyItem


class SinaSpider(Spider):

    name = "sina"
    start_urls = [
        'http://db.auto.sina.cn/cars/?vt=4&pos=25'
    ]

    def parse(self, response):
        data_idlist = response.xpath('/html/body/section[2]/div[2]/div/div/ul/li/a/@data-id').extract()
        for data_id in data_idlist:
            url = 'http://db.auto.sina.cn/api/car/getBrandDetail.json?brandid=' + data_id
            yield Request(url, callback=self.parse1)

    def parse1(self, response):
        txt1 = response.xpath('/html/body/p/text()').extract()
        for brand in demjson.decode(txt1[0])['result']['data']['data_list'].keys():
            for data in demjson.decode(txt1[0])['result']['data']['data_list'][brand]['data_list']['data']:
                item = CarScrapyItem()
                item['type'] = None
                item['brand'] = demjson.decode(txt1[0])['result']['data']['data_list'][brand]['cname']
                item['url'] = 'db.auto.sina.cn/' + data['serialId'] + '/'
                item['name'] = data['cname']
                yield item
