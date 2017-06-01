# coding=utf-8
from scrapy import Request
from scrapy import Spider
import demjson
from car_scrapy.items import CarScrapyItem


class PacutoSpider(Spider):
    name = "pcauto"
    start_urls = [
        'http://m.pcauto.com.cn/auto/',
    ]

    def parse(self, response):
        idList = response.xpath('//*/ul/li/a/@data-id').extract()
        for id in idList:
            url = 'http://price.pcauto.com.cn/auto/api/hcs/serial_group_list?bid=' + id + \
                  '&status=0&callback=window.getDateCK_0'
            yield Request(url, callback=self.parse1)

    def parse1(self, response):
        txt1 = response.xpath('/html/body/p/text()').extract()
        for man in demjson.decode(txt1[0][19:-1])["manufacturers"]:
            for serial in man["serials"]:
                item = CarScrapyItem()
                item['brand'] = man["brandName"]
                item['type'] = man["name"]
                item['url'] = 'm.pcauto.com.cn/auto/sg' + str(serial["sgid"]) + '/'
                item['name'] = serial["sgname"]
                yield item
