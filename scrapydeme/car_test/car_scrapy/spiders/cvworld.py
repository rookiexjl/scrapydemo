# coding:utf-8
from scrapy import Request
from scrapy import Spider
from car_scrapy.items import CarScrapyItem


class CVWorldSpider(Spider):

    name = "cvworld"
    start_urls = [
        "http://www.cvworld.cn/index_bus.html",
        "http://www.cvworld.cn/index_truck.html"
    ]

    def parse(self, response):
        item = CarScrapyItem()
        xPath = u'//form[@id="form1"]/div[@class="wrap fix"]/div[@class="main all_news"]/div[@class="pinpai_ms1_con"]'
        resListdiv = response.xpath(xPath).extract()
        for i in range(len(resListdiv)+1):
            string = '//form[@id="form1"]/div[@class="wrap fix"]/div[@class="main all_news"]/div[@class="pinpai_' \
                     'ms1_con"]' + '[' + str(i) + ']'
            string6 = string + '/table/tbody/tr/td[2]/dl'
            xPath = unicode(string6)
            resListdd = response.xpath(xPath).extract()
            for i in range(1, len(resListdd)+1):
                string7 = string6 + '[' + str(i) + ']'
                string1 = string7  + '/dd/font'
                string2 = string + '/table/tbody/tr/td[1]/a[2]/text()'
                xPath = unicode(string1)
                resList3 = response.xpath(xPath).extract()
                xPath = unicode(string2)
                brand = response.xpath(xPath).extract()
                if len(resList3) > 0:
                    for j in range(1, len(resList3)+1):
                        string3 = string1 + '[' + str(j) + ']'
                        try:
                            string4 = string3 + '/b/a/@href'
                            xPath = unicode(string4)
                            link = response.xpath(xPath).extract()
                            url = 'http://www.cvworld.cn/' + link[0]
                        except:
                            break
                        string5 = string3 + '/b/a/text()'
                        xPath = unicode(string5)
                        name = response.xpath(xPath).extract()
                        if len(name) and len(link) > 0:
                            item['name'] = name[0].strip()
                            item['brand'] = brand[0].strip()
                            item['url'] = url.strip()
                            item['type'] = None
                            yield item
