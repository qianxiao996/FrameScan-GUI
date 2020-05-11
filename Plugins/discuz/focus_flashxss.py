#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: discuz X3 focus.swf flashxss漏洞
referer: unknown
author: Lucifer
description: 文件中focus.swf存在flashxss。
'''
import sys
import urllib
import hashlib
import warnings
def run(url):
        result = ['discuz X3 focus.swf flashxss漏洞', '', '']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        flash_md5 = "c16a7c6143f098472e52dd13de85527f"
        payload = "/static/image/common/focus.swf"
        vulnurl = url + payload
        try:
            req = urllib.request.urlopen(vulnurl)
            data = req.read()
            md5_value = hashlib.md5(data).hexdigest()
            if md5_value in flash_md5:
                result[2]='存在'
                result[1] = vulnurl
            else:
                result[2]='不存在'
        except:
            result[2]='不存在'
        return result
if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
