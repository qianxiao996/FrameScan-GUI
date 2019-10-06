#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: ElasticSearch未授权漏洞
referer: https://www.cnblogs.com/KevinGeorge/p/8038138.html
author: Lucifer
description: 该漏洞导致攻击者可以拥有Elasticsearch的所有权限。可以对数据进行任意操作。
'''
import sys
import warnings
import requests
import tempfile,sys
from elasticsearch import Elasticsearch

from urllib.parse import urlparse

sys.stderr=tempfile.TemporaryFile()

class unauth_BaseVerify:
    def __init__(self, url):
        self.url = url

    def run(self):
        result = ['shellshock漏洞', '', '']
        port = 9200
        if r"http" in self.url:
            #提取host
            host = urlparse(self.url)[1]
            try:
                port = int(host.split(':')[1])
            except:
                pass
            flag = host.find(":")
            if flag != -1:
                host = host[:flag]
        else:
            if self.url.find(":") >= 0:
                host = self.url.split(":")[0]
                port = int(self.url.split(":")[1])
            else:
                host = self.url

        try:
            es = Elasticsearch([host], port=port, timeout=6)
            if es.ping():
                result[2] = '存在'
                result[1]=host+":"+str(port)
            else:
                result[2] = '不存在'

        except:
            result[2] = '未知'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = unauth_BaseVerify(sys.argv[1])
    testVuln.run()