# -*- coding:utf-8-*-
import logging

ips = [
       '111.23.10.56:80',
       '111.23.10.30:80',
       '111.23.10.37:8080'
       ]


class ProxyMiddleware(object):
    http_n = 0

    def process_request(self, request, spider):
        if request.url.startswith("http://"):
            try:
                n = ProxyMiddleware.http_n
                request.meta['proxy'] = "http://%s" % ips[n]
                logging.info('Squence - http: %s - %s' % (n, str(ips['http'][n])))
                ProxyMiddleware.http_n = n + 1
            except:
                pass