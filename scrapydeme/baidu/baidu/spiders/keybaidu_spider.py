# # coding=utf-8
# from scrapy import Request
# from scrapy import Spider
#
# from baidu.items import BaiduItem
#
#
# class KacheSpider(Spider):
#     name = "baidukey"
#     start_urls = [
#         'https://m.baidu.com/s?word=重庆航宇股票配资',
#     ]
#
#     def parse(self, response):
#         xPath = u'//*[@id="results"]/div/div/div/div/a[1]/@href'
#         resList1 = response.xpath(xPath).extract()
#         xPath = u'//*[@id="kw"]/text()'
#         name = response.xpath(xPath).extract()[0]
#         for url in resList1:
#             yield Request(url, callback = self.parse1, meta={'name': name})
#         print "************************************"
#         xPath = u'//*[@id="page-controller"]/div/a/@href'
#         resList1 = response.xpath(xPath).extract()
#         if len(resList1) > 0:
#             yield Request(resList1[0], callback=self.parse)
#
#     def parse1(self, response):
#         item = BaiduItem()
#         name = response.meta['name']
#         item['url'] = response.url
#         print name
#         item['name'] = name
#         yield item
