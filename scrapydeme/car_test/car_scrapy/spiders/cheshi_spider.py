# coding=utf-8
from scrapy import Request
from scrapy import Spider
import demjson
from car_scrapy.items import CarScrapyItem


class CheShiSpider(Spider):
    name = "cheshi"
    start_urls = [
        'http://a.cheshi.com/product/'
    ]

    def parse(self, response):
        brandlist = response.xpath('//*[@class="cheshi_pplist"]/ul/li/a/@id').extract()
        for signid in brandlist:
            url = 'http://a.cheshi.com/ajax/car/get_prd_series_list.php?type=sign&&signid=' +\
                  signid.split('_')[2]
            yield Request(url, callback=self.parse1)

    def parse1(self, response):
        txt1 = response.xpath('/html/body/p/text()').extract()
        try:
            for list in demjson.decode(txt1[0]):
                for sub_list in list["bcatesub_list"]:
                    item = CarScrapyItem()
                    item['brand'] = list["brandName"]
                    item['type'] = None
                    item['url'] = 'a.cheshi.com/bseries_' + sub_list["bcatesub_id"] + '/'
                    item['name'] = sub_list["name"]
                    yield item
        except:
            pass
