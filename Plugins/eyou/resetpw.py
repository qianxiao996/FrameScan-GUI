#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 亿邮邮件系统重置密码问题暴力破解
referer: http://www.wooyun.org/bugs/wooyun-2015-0162892
author: Lucifer
description: 亿邮邮件系统找回密码处，如果用户设置问题密码过于简单可被暴力破解。
'''
import sys
import requests
import warnings
def run(url):
        result = ['亿邮邮件系统重置密码问题暴力破解', '', '']
        payload = "/?q=resetpw"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, timeout=10, verify=False)

            if req.status_code == 200 and r"pw_intensity" in req.text:
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
    