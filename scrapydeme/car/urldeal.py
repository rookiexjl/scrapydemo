# coding:utf-8
import os

dirname = 'findKeyString'
for parent, dirnames, filenames in os.walk(dirname):
    for filename in filenames:
        fp = open('findKeyString/'+filename)
        #
        # string = ['http://m.chinatruck.org/video/64350.html	24.63L/100km
        #           24.63L/100km 中国重汽曼技术产品高效节油实况挑战赛首战成都',
        #           'w.auto.qq.com/car_serial/1545/ AC Schnitzer    AC Schnitzer    AC Schnitzer M3',
        #           'car.m.yiche.com/acgaizhuangbaomax6/	AC Schnitzer		AC Schnitzer ACS6',
        #           'm.autohome.com.cn/2148/	AC Schnitzer-		AC Schnitzer 7系',
        #           'a.xcar.com.cn/1285/	DS(进口)		DS 5(进口)',
        #           'http://product.m.360che.com/s26/6711_63_index.html	奥驰汽车	奥驰X系?自卸车	奥驰X系',
        #           'http://www.cvworld.cn/series_65.html	北奔重汽		北奔重卡',
        #           'auto.3g.163.com/baojun/16795/			宝骏乐驰'
        #           'http://m.pcauto.com.cn/auto/sg4494/'
        #           'm.haomaiche.com/hz/car_parity_detail/00fa5a6551ca4dbf84217f04240ddfe0'
        #           'db.m.auto.sohu.com/model_5174/?param=320&from=list'
        #           'a.cheshi.com/bseries_1906/'
        #           'db.auto.sina.cn/1685	smart		smart forjeremy'
        #           'm.58che.com/2467/'
        #           'm.chexun.com/auto/2033/	��������		ս��'
        #           ‘auto.m.315che.com/changanzhixing2/	长安商用	长安商用	长安之星2’]
        for i in fp.readlines():
            lines = i.split(' ')[0].split('\t')[0]
            if lines.find('chinatruck.org') != -1:
                lines = lines.split('//m')[1]
                a = lines.split('/')[0]
                b = lines.split('org')[1]
                lines = a + ' ' + b
            elif lines.find('qq.com') != -1:
                lines = lines.split('w.')[1]
                a = lines.split('/')[0]
                b = lines.split('com')[1]
                lines = '.' + a + ' ' + b
            elif lines.find('yiche.com') != -1:
                lines = lines.split('car.m')[1]
                a = lines.split('/')[0]
                b = lines.split('com')[1]
                lines = a + ' ' + b
            elif lines.find('autohome.com') != -1:
                lines = lines.split('autohome')[1]
                a = lines.split('/')[0]
                b = lines.split('com.cn')[1]
                lines = '.autohome' + a + ' ' + b
            elif lines.find('xcar.com') != -1:
                lines = lines.split('xcar')[1]
                a = lines.split('/')[0]
                b = lines.split('com.cn')[1]
                lines = '.xcar' + a + ' ' + b
            elif lines.find('360che.com') != -1:
                lines = lines.split('360che')[1]
                a = lines.split('/')[0]
                b = lines.split('.com')[1]
                lines = '.360che' + a + ' ' + b
            elif lines.find('cvworld.cn') != -1:
                lines = lines.split('cvworld')[1]
                a = lines.split('/')[0]
                b = lines.split('.cn')[1]
                lines = '.cvworld' + a + ' ' + b
            elif lines.find('163.com') != -1:
                a = lines.split('/')[0]
                b = lines.split('com')[1]
                lines = a + ' ' + b
            elif lines.find('m.haomaiche.') != -1:
                lines = lines.split('haomaiche')[1]
                a = lines.split('/')[0]
                b = lines.split('hz')[1]
                lines = '.haomaiche' + a + ' ' + b
            elif lines.find('m.pcauto') != -1:
                lines = lines.split('pcauto')[1]
                a = lines.split('/')[0]
                b = lines.split('com.cn')[1]
                lines = '.pcauto' + a + ' ' + b
            elif lines.find('m.58che') != -1:
                lines = lines.split('58che')[1]
                a = lines.split('/')[0]
                b = lines.split('com')[1]
                lines = '.58che' + a + ' ' + b
            elif lines.find('m.chexun') != -1:
                lines = lines.split('chexun')[1]
                a = lines.split('/')[0]
                b = lines.split('com')[1]
                lines = '.chenxun' + a + ' ' + b
            elif lines.find('a.cheshi') != -1:
                lines = lines.split('cheshi')[1]
                a = lines.split('/')[0]
                b = lines.split('com')[1]
                lines = 'a.cheshi' + a + ' ' + b
            elif lines.find('.auto.sina.') != -1:
                lines = lines.split('sina')[1]
                a = lines.split('/')[0]
                b = lines.split('cn')[1]
                lines = '.auto.sina' + a + ' ' + b
            elif lines.find('m.315che.') != -1:
                a = lines.split('/')[0]
                b = lines.split('/')[1]
                lines = a + ' /' + b + '/'
            elif lines.find('m.auto.sohu.') != -1:
                a = lines.split('/')[1]
                lines = '.m.auto.sohu.com' + ' /' + a + '/'
            elif lines.find('17.com') != -1:
                a = lines.split('17.com')[1]
                lines = '.17.com ' + a
            elif lines.find('iauto.ifeng') != -1:
                a = lines.split('/')[0]
                b = lines.split('&')[2]
                lines = a + ' ' + b
            newdir = 'result/' + filename
            with open(newdir, "a") as f:
                f.write(lines + '\n')
