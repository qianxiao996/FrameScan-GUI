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

## 插件模板

以下为POC模板，请尽量规范编写。脚本中为示例代码。

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from urllib.parse import urlparse

def vuln_info():
    info={
        'name': 'POC测试漏洞',
        'referer':'http://baidu.com',
        'author':'qianxiao996',
        'description':'''百度测试。'''

    }
    return info
def run(MainWindows,url,all):
    #一定要把all这个参数返回回去。
    # all =  0=url  1=filename  2=pocmethods  3=pocname


    #传递过来的是url。如果需要IP和端口可以使用代码
    _url = urlparse(url)
    dhost = _url.hostname
    dip = socket.getaddrinfo(dhost, None)[0][4][0]
    dport = _url.port
    result = '存在'
    padload= 'payload'
    #debug信息 默认不会显示，勾选显示调试信息会输出此结果 
    MainWindows.vuln_scanner_log('Debug','denbug信息') 
    #返回的结果
    MainWindows.vuln_scanner_log('result', result,padload,all)
    #自定义输出
    MainWindows.vuln_scanner_log('Error','运行错误','',all)
```

exp

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
import requests
import warnings

def vuln_info():
    info={
        'name': 'POC测试漏洞',
        'referer':'http://baidu.com',
        'author':'qianxiao996',
        'description':'''expddddd'''

    }
    return info

def run(MainWindows,url,heads='',cookie='',cmd='whoami',lhost='',lport=8888):
    #命令执行
    if lhost=='':
        MainWindows.vuln_exp_log('result','root')

    #反弹shell    
    if lhost!='':
        MainWindows.vuln_exp_log('log','反弹成功','red')
 
```

插件目录下

exp后缀为_exp.py

poc后缀为_poc.py

请规范编写

## POC and EXP

POC and EXP 为内部使用。需要POC及EXP请编写POC或EXP联系作者交换。

邮箱地址：qianxiao996@126.com

## 警告！
**请勿用于非法用途！否则自行承担一切后果**







```
pyinstaller -F FrameScan-GUI.py -i main.ico  --hidden-import eventlet.hubs.epolls --hidden-import eventlet.hubs.kqueue    --hidden-import  eventlet.hubs.selects --hidden-import dns --hidden-import dns.dnssec --hidden-import dns.e164  --hidden-import dns.hash  --hidden-import dns.namedict  --hidden-import   dns.tsigkeyring --hidden-import dns.update --hidden-import dns.version --hidden-import dns.zone -w
```

