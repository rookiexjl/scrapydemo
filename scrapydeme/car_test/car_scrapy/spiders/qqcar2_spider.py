# coding=utf-8
from scrapy import Request
from scrapy import Spider

from car_scrapy.items import CarScrapyItem


class KacheSpider(Spider):
    name = "qqcar2"
    start_urls = [
        'http://w.auto.qq.com/car_brand/index.shtml'
    ]

    def parse(self, response):
        _href_list = response.xpath('//*[@id="brand_filter"]/section/ul/li/a/@_href').extract()
        for href in _href_list:
            url = 'http://w.auto.qq.com' + href
            yield Request(url, callback=self.parse1)

    def parse1(self, response):
        data_id = response.xpath('//*[@id="brand2list"]/section/ul/li/a/div/div/div/div/@data-id').extract()
        namelist = response.xpath('//*[@id="brand2list"]/section/ul/li/a/div/div/div/div[1]/text()').extract()
        for i in range(len(namelist)):
            item = CarScrapyItem()
            item['brand'] = response.xpath('//*[@id="brand2list"]/header/div/text()').extract()[0]
            item['type'] = None
            item['url'] = 'w.auto.qq.com/car_serial/' + data_id[i] + '/'
            item['name'] = namelist[i]
            yield item

