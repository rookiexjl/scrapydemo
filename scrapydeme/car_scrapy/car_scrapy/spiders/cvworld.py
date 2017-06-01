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
        # div num
        xPath = u'//form[@id="form1"]/div[@class="wrap fix"]/div[@class="main all_news"]/div[@class="pinpai_ms1_con"]'
        resListdiv = response.xpath(xPath).extract()
        # print len(resListdiv)
        for i in range(len(resListdiv)+1):
            #//form[@id="form1"]/div[@class="wrap fix"]/div[@class="main all_news"]/div[@class="pinpai_ms1_con"][i]
            # div num
            string = '//form[@id="form1"]/div[@class="wrap fix"]/div[@class="main all_news"]/div[@class="pinpai_ms1_con"]' + '[' + str(i) + ']'
            # .xpath('//div[@class="pinpai_ms1_con"]/table/tbody/tr/td[2]/dl/dd/font').extract()
            #// *[ @ id = "form1"] / div[5] / div[3] / div[97] / table / tbody / tr / td[2] / dl[1]
            # dl num
            string6 = string + '/table/tbody/tr/td[2]/dl'
            xPath = unicode(string6)
            resListdd = response.xpath(xPath).extract()
            for i in range(1, len(resListdd)+1):
                # dl num
                string7 = string6 + '[' + str(i) + ']'
                string1 = string7  + '/dd/font'
                string2 = string + '/table/tbody/tr/td[1]/a[2]/text()'
                xPath = unicode(string1)
                resList3 = response.xpath(xPath).extract()
                xPath = unicode(string2)
                brand = response.xpath(xPath).extract()
                if len(resList3) > 0:
                    for j in range(1,len(resList3)+1):
                        # font num
                        string3 = string1 + '[' + str(j) + ']'
                        try:
                            # url
                            string4 = string3 + '/b/a/@href'
                            xPath = unicode(string4)
                            link = response.xpath(xPath).extract()
                            url = 'http://www.cvworld.cn/' + link[0]
                        except:
                            break
                        # name
                        string5 = string3 + '/b/a/text()'
                        xPath = unicode(string5)
                        name = response.xpath(xPath).extract()
                        # return item
                        if len(name) and len(link) > 0:
                            item['name'] = name
                            item['brand'] = brand
                            item['url'] = url
                            yield item
