# coding=utf-8
from scrapy import Request
from scrapy import Spider
from car_scrapy.items import CarScrapyItem


class WuBaCheSpider(Spider):
    name = "58che"
    start_urls = [
        'http://m.58che.com/car/brand.html?f=index'
    ]

    def parse(self, response):
        href_list = set(response.xpath('//*[@id="hotBrands"]/ul/li/a/@href').extract())
        for href in href_list:
            url = 'http://m.58che.com' + href
            yield Request(url, callback=self.parse1)

    def parse1(self, response):
        namelist = response.xpath('//*[@id="rollPC1"]/div/dl/dd[1]/text()').extract()
        brand = response.xpath('/html/body/section[1]/dl/dd/strong/text()').extract()
        url_list = response.xpath('//*[@id="rollPC1"]/div/dl/dt/a/@href').extract()
        for i in range(len(namelist)):
            item = CarScrapyItem()
            item['brand'] = brand[0]
            item['type'] = None
            item['url'] = url_list[i].split('//')[1]
            item['name'] = namelist[i]
            yield item
