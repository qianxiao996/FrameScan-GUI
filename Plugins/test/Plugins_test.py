# -*- coding: UTF-8 -*-
#!/usr/bin/python
import requests,time
def vuln_info():
    info={
        'vuln_name': 'POC测试漏洞',  #漏洞名称
        'vuln_referer':'http://baidu.com',  #漏洞来源
        'vuln_author':'qianxiao996',  #插件作者
        'cms_name':'test',#cms_name需要和上级目录保持一致。扫描器自动添加会调用。GUI版本不会调用
        'vuln_description':'''漏洞描述''',
        'vuln_identifier':'''漏洞编号。''',
        'vuln_class':'漏洞分类',#如：信息泄漏、远程命令执行、任意文件上传、SQL注入、XML注入、任意文件读取、本地文件包含、认证绕过/未认证、弱口令、目录遍历、其他、反序列化漏洞、OGNL表达式注入、SSRF、后门、任意文件下载、鉴权绕过、暴力破解、命令注入、路径泄露、XSS、远程文件包含、CSRF、任意文件包含、代码注入、任意文件写入、密码硬编码、文件包含、任意用户注册、缓冲区溢出、用户枚举漏洞、任意文件删除、任意页面上传、管理权限等
        'vuln_solution':'''修复建议。''',
        'FofaQuery_link':'/', #此处的路径会加在url拼接访问，进行FofaQuery的条件匹配 此处为all为全部页面都检测
        'FofaQuery':'title="百度"',#header="JSESSIONID" || body="Struts Problem Report" || body="There is no Action mapped for namespace" || body="No result defined for action and result input" || header="Servlet" || header="JBoss",port="60001"
        
        #header', 'body', 'title', 'banner','port','banner','service','protocol','server'
        
        'ispoc':1, #是否有poc
        'isexp':1  #是否有exp
    }
    return info
# url：url  hostname：主机地址  port：端口  scheme：服务  heads：http自定义头信息
def do_poc(url,hostname,port,scheme,heads={}):
    # time.sleep(20)
    # 返回参数
    #参数一为返回的类型，参数二结果，参数三为Payload  参数四为输出的颜色（可为空）
    #Result为结果
    #Debug debug信息 默认不会显示，勾选显示调试信息会输出此结果
    #其他均会输出
    result = {"type":'Result', "value":"不存在", "payload":"payload","color":"black"}
    result['value'] = '存在'
    result['payload']= 'payload'
    return result
    
# url:url   heads:自定义请求头 exp_type:两个选项（cmd,shell） exp_cmd：命令执行的命令 lhost：反弹shell的IP lport：反弹shell的端口
def do_exp(url,heads={},exp_type='cmd',exp_cmd='whoami',lhost='127.0.0.1',lport=8888):
    # 返回参数
    # time.sleep(22)
    # 参数一为返回的类型，参数二为返回的值，参数三为输出的颜色
    result = {"type":'Result', "value":"root", "color":"black"}
    #命令执行
    if exp_type=='cmd':
        result['value'] = "root"
        return result
    #反弹shell    
    if exp_type=='shell':
        result['type'] = "log"
        result['value'] = "反弹成功"
        result['color'] = "green"
        return result
