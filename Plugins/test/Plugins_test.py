#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

def vuln_info():
    info={
        'vuln_name': 'POC测试漏洞',
        'vuln_referer':'http://baidu.com',
        'vuln_author':'qianxiao996',
        'vuln_description':'''漏洞描述''',
        'vuln_identifier':'''漏洞编号。''',
        'vuln_solution':'''修复建议。''',
        'ispoc':1,
        'isexp':1

    }
    return info
# url：url  hostname：主机地址  port：端口  scheme：服务
def do_poc(url,hostname,port,scheme):
    # 返回参数
    #参数一为返回的类型，参数二结果，参数三为Payload  参数四为输出的颜色（可为空）
    #Result为结果
    #Debug debug信息 默认不会显示，勾选显示调试信息会输出此结果
    #其他均会输出
    result = {"type":'Result', "value":"不存在", "payload":"payload","color":"black"}
    result['value'] = '存在'
    result['payload']= 'payload'
    return result
    

# url:url   heads:自定义请求头 cookie:cookie  exp_type:两个选线（cmd,shell） exp_cmd：命令执行的命令 lhost：反弹shell的IP lport：反弹shell的端口
def do_exp(url,heads='',cookie='',exp_type='cmd',exp_cmd='whoami',lhost='127.0.0.1',lport=8888):
    # 返回参数
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