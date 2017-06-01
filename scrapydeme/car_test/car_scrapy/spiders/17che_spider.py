# coding=utf-8
from scrapy import Request
from scrapy import Spider
from car_scrapy.items import CarScrapyItem


class YiQiTuanGouSpider(Spider):
    name = "17che"
    start_urls = []
    for i in range(1, 46):
        start_urls.append('http://www.17.com/tuangou/?page=' + str(i))

    def parse(self, response):
        url_list = response.xpath('/html/body/div[5]/div/div[2]/i/a/@href').extract()
        for i in range(len(url_list)):
            url = 'http://www.17.com' + url_list[i]
            yield Request(url, callback=self.parse1)

    def parse1(self, response):
        item = CarScrapyItem()
        try:
            item['brand'] = response.xpath('//*[@id="tuan-title"]/span/img/@alt').extract()[0]
            item['name'] = response.xpath('/html/body/div[5]/div/div[2]/div[1]/ul/li[1]/h3/text()')\
                .extract()[0].encode('utf8').split('团购')[0]
        except:
            item['brand'] = None
            item['name'] = response.xpath('/html/body/div[5]/div/div[2]/div[1]/ul/li[1]/h3/text()').extract()[0]
        item['type'] = None
        item['url'] = response.url.split('//')[1]
        yield item

    # def parse(self, response):
    #     url_list = response.xpath('/html/body/div[5]/div/div[2]/i/a/@href').extract()
    #     namelist = response.xpath('/html/body/div[5]/div/div[2]/i/a/text()').extract()
    #     # brand = response.xpath('/html/body/div[5]/div/h2/a/text()').extract()
    #     for i in range(len(url_list)):
    #         item = CarScrapyItem()
    #         item['brand'] = None
    #         item['type'] = '团购'
    #         item['url'] = url_list[i]
    #         item['name'] = namelist[i]
    #         yield item

    # def parse1(self, response):
    #     # print response.url
    #     # namelist = response.xpath('//*[@id="rollPC1"]/div/dl/dd[1]/text()').extract()
    #     #
    #     item = CarScrapyItem()
    #     item['brand'] = response.xpath('//*[@id="tuan-title"]/span/img/@alt').extract()[0]
    #     item['type'] = None
    #     item['url'] = response.url.split('//')[1]
    #     item['name'] = response.xpath('/html/body/div[5]/div/div[2]/div[1]/ul/li[1]/h3/text()') \
    #         .extract()[0].encode('utf8').split('团购')[0]
    #     yield item
