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
name: POC测试漏洞
referer: http://baidu.com
author: qianxiao996
description: 百度测试。
'''
import requests
import warnings
def run(url):
    #返回一个列表，参数一为检测结果，参数二为Payload
    result = ['Payload','存在']
    return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
```

exp

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: POC测试漏洞
referer: http://baidu.com
author: qianxiao996
description: 百度测试。
'''
import sys
import json
import requests
import warnings


def run(url,heads='',cookie='',cmd='whoami',lhost='',lport=8888):
    #命令执行
    if lhost=='':
        return('root')

    #反弹shell    
    if lhost!='':
        return('反弹成功！')
 



if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run('http://baidu.com','','','whoami')
    te2stVuln = run('http://baidu.com','','','whoami','127.0.0.1',8888)
```

插件目录下

exp后缀为_exp.py

poc后缀为_poc.py

请规范编写

## 鸣谢

POC：无

Exp：无

部分为自己编写，欢迎投递POC

邮箱地址：qianxiao996@126.com

## 警告！
**请勿用于非法用途！否则自行承担一切后果**
