# coding=utf-8
import json
import demjson
import simplejson as simplejson
from scrapy import Request
from scrapy import Spider
from car_scrapy.items import CarScrapyItem


class QQSpider(Spider):
    name = "qq"
    start_urls = [
    'http://data.auto.qq.com/car_brand/index.shtml'
    ]
    header={
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Cookie':'eas_sid=a1n4q7Q0R4p6k6A7M9J6L294M6; tvfe_boss_uuid=3986a0a9242c1609; pac_uid=1_784814747; h_uid=H076610136aa; sdi_stat_uid=b4b8605a-703f-4dc4-bf9f-c7ddd0f0d07d; sdi_from_2016101418224701169=0; h_lloc={"FLastOpenCitySubName":"nj","FLocationCitySubName":"nj"}; mobileUV=1_1586c3ad64d_2fcab; ptui_loginuin=784814747@qq.com; ts_refer=www.baidu.com/link; ts_uid=5394612784; ptcz=204be56124f3802097bc17e4bff8399b59fcb99c0aa4e0a42c149d5ae0216ff8; pt2gguin=o0784814747; uin=o0784814747; skey=@Pal8PRgHy; ptisp=ctc; ad_play_index=45; pgv_info=ssid=s7809003137; ts_last=data.auto.qq.com/car_brand/index.shtml; pgv_pvid=7886152520; o_cookie=784814747; ts_uid=5394612784',
        'Host':'data.auto.qq.com',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36',
    }
    #cookie={
    #     'ad_play_index': '45',
    #     'eas_sid': 'a1n4q7Q0R4p6k6A7M9J6L294M6',
    #     'h_lloc': '{"FLastOpenCitySubName":"nj","FLocationCitySubName":"nj"}',
    #     'h_uid': 'H076610136aa',
    #     'mobileUV': '1_1586c3ad64d_2fcab',
    #     'o_cookie': '784814747',
    #     'pac_uid': '1_784814747',
    #     'pgv_info': 'ssid=s7809003137',
    #     'pgv_pvid': '7886152520',
    #     'pt2gguin': 'o0784814747',
    #     'ptcz': '204be56124f3802097bc17e4bff8399b59fcb99c0aa4e0a42c149d5ae0216ff8',
    #     'ptisp': 'ctc',
    #     'ptui_loginuin': '784814747@qq.com',
    #     'sdi_from_2016101418224701169': '0',
    #     'sdi_stat_uid': 'b4b8605a-703f-4dc4-bf9f-c7ddd0f0d07d',
    #     'skey': '@Pal8PRgHy',
    #     'ts_last': 'data.auto.qq.com/car_brand/index.shtml',
    #     'ts_refer': 'www.baidu.com/link',
    #     'ts_uid': '5394612784',
    #    # 'ts_uid': '5394612784',
    #
    #     'tvfe_boss_uuid': '3986a0a9242c1609',
    #     'uin': 'o0784814747'
    # }
    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, headers=self.header,callback=self.parse)

    def parse(self, response):
        item=CarScrapyItem()
        xPath = u'//script'
        resList1 = response.xpath(xPath).extract()

        json_data=resList1[15][resList1[15].find('list')-1:resList1[15].find('}]}]}]}]}')+9]
        json_str=json_data.encode("utf-8")
        #print json_data
        # encodedjson = json.dumps(json_data,'gbk')
        # #strjson = json.loads(encodedjson)
        # decodejson = json.loads(encodedjson)
        f=open('a.txt','w')
        f.write(json_str)
        print '========'
        for BrandList in demjson.decode(json_str)['list']:
            print '-------'
            #print BrandList
            brand=BrandList['BrandList']
            #print type(brand)
            for b in brand:
                item['brand']=b['brandName']
                manName=b['manList']
                print type(manName)
                if len(manName)>0:
                    for man in manName:
                        item['type']=man['manName']
                        ser=man['serialList']
                        if len(ser)>0:
                            for detail in ser:
                                item['name']=detail['serialName']
                                id=detail['serialID']
                                url='w.auto.qq.com/car_serial/'+id+'/'
                                item['url']=url
                                print item
                                yield item

            # baseItem['brand'] = carURL
            # baseItem['brand'] = carURL meta={'brand': baseItem},
#             yield Request(carURL,  callback=self.parse_detail)
#     def parse_detail(self,response):
#
#         xPath = u'//*[@id="data_table_MasterSerialList_0"]/div/ul/li[1]/a/@href'
#         resList1 = response.xpath(xPath).extract()
#         for i in range(1, len(resList1) + 1):
#             # for i in range(1,2):
#             carURL = 'http://car.bitauto.com'+resList1[i - 1]
#             print carURL
#             print '================================'
#
#             # baseItem['brand'] = carURL
#             # baseItem['brand'] = carURL meta={'brand': baseItem},
#             yield Request(carURL,  callback=self.item)
#     def item(self,response):
#         baseItem = CarScrapyItem()
#         xPath = u'//*[@id="topBox"]/div[1]/div/div/strong/text()'
#         name = response.xpath(xPath).extract()
#
#         baseItem['name'] = name[0]
# #'preceding-sibling::*[1]'
#         xPath = u'//*[@id="topBox"]/div[1]/div/div/strong/preceding-sibling::*[1]/text()'
#         brand = response.xpath(xPath).extract()
#
#         baseItem['brand'] = brand[0]
#
#         URL=response.url.replace('http://car.bitauto.com','car.m.yiche.com ')
#         baseItem['url'] = URL
#         print baseItem
#         yield baseItem
