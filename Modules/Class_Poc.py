from random import *
from colorama import  Fore
import re,os,importlib
import random,sys
from tqdm import tqdm
import operator
from string import Template
import requests,string
import datetime
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
#屏蔽SSl警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    
application_path = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "modules")
if application_path not in sys.path:
    sys.path.append(application_path)
# 遍历目录下的所有模块并导入
for module in os.listdir(application_path):
    if module.endswith('.py') and not module.startswith("Class_") and not module.startswith("Main.py"):
        try:
            module_name = module[:-3]  # 假设您的模块名为my_module.py
            module = importlib.import_module(module_name)
            # 将模块注册到全局变量中
            globals()[module_name] = module
        except Exception as e:
            print("引入模块失败："+str(e))
            # print(str(e) + '----' + str(e.__traceback__.tb_lineno) + '行')
retry_times = 3  # 设置重试次数
retry_backoff_factor = 1  # 设置重试间隔时间
user_agent_list = [
    'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36'
    'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36'
    'Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1'
    'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.109 Safari/537.36 CrKey/1.54.248666'
    'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320'
    'Mozilla/5.0 (BB10; Touch) AppleWebKit/537.10+ (KHTML, like Gecko) Version/10.0.9.2372 Mobile Safari/537.10+'
    'Mozilla/5.0 (PlayBook; U; RIM Tablet OS 2.1.0; en-US) AppleWebKit/536.2+ (KHTML like Gecko) Version/7.2.1.0 Safari/536.2+'
    'Mozilla/5.0 (Linux; U; Android 4.3; en-us; SM-N900T Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
    'Mozilla/5.0 (Linux; U; Android 4.1; en-us; GT-N7100 Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
    'Mozilla/5.0 (Linux; U; Android 4.0; en-us; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
    'Mozilla/5.0 (Linux; Android 7.0; SM-G950U Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36'
    'Mozilla/5.0 (Linux; Android 8.0.0; SM-G965U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36'
    'Mozilla/5.0 (Linux; Android 8.1.0; SM-T837A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.80 Safari/537.36'
    'Mozilla/5.0 (Linux; U; en-us; KFAPWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.13 Safari/535.19 Silk-Accelerated=true'
    'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LGMS323 Build/KOT49I.MS32310c) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.0.0 Mobile Safari/537.36'
    'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 550) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/14.14263'
    'Mozilla/5.0 (Linux; Android 6.0.1; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 10 Build/MOB31T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5X Build/OPR4.170623.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    'Mozilla/5.0 (Linux; Android 7.1.1; Nexus 6 Build/N6F26U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 6P Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 7 Build/MOB30X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 520)'
    'Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13'
    'Mozilla/5.0 (Linux; Android 9; Pixel 3 Build/PQ1A.181105.017.A1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Mobile Safari/537.36'
    'Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36'
    'Mozilla/5.0 (Linux; Android 11; Pixel 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36'
    'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'
    'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
]
class Class_Poc:
    def __init__(self,url,poc,timeout,debug):
        self.url = url.strip()
        self.poc=poc
        self.timeout=timeout
        self.session = requests.Session()
        retry = Retry(total=retry_times, backoff_factor=retry_backoff_factor)
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount('http://', adapter)
        self.session.mount('https://', adapter)
        self.all_global_var={}#存放所有的全局变量
        self.all_global_payload = {} #所有payload
        self.all_request_name_list={}
        self.debug=debug
    def main(self):
        poc_name = self.poc.get("name")
        poc_transport = self.poc.get("transport")
        poc_rules = self.poc.get("rules")
        poc_expression = self.poc.get("expression")
        poc_detail = self.poc.get("detail")
        poc_re_str = self.poc.get("output")
        poc_set = self.poc.get("set")
        poc_payload = self.poc.get("payload")
        self.set_bianliang(poc_set)
        self.set_payload(poc_payload)
        # print(self.all_global_var)
        if poc_transport.lower()=="http":
            try:
                response = self.poc_request_http(poc_rules)                
                if  type(response) !=requests.models.Response:
                    result =  {"url":self.url,"poc":self.poc,"result":False,"others":response}
                else:
                    is_success = self.main_poc_expression(poc_expression)
                    resultaa=""
                    if is_success:
                        resultaa = self.re_others(response,poc_re_str)
                    result  = {"url":self.url,"poc":self.poc,"result":is_success,"others":resultaa}
                    if self.debug:
                        tqdm.write(self.out_debug_info("Replace Main Output","原始字符串：%s 替换后:%s"%(poc_re_str,resultaa)))
            except Exception as e:
                result =  {"url":self.url,"poc":self.poc,"result":False,"others":'Error:'+str(e)+' 行:'+str(e.__traceback__.tb_lineno)}
        elif poc_transport.lower()=="tcp":
            result =  {"url":self.url,"name":self.poc.get("name"),"result":"False","others":"暂不支持此协议，待开发！"}
        elif poc_transport.lower()=="udp":
            result =  {"url":self.url,"name":self.poc.get("name"),"result":"False","others":"暂不支持此协议，待开发！"}
        else:
            result =  {"url":self.url,"name":self.poc.get("name"),"result":"False","others":"协议不正确"}
        if self.debug:
            tqdm.write(self.out_debug_info("Return","输出结果:%s"%(result)))
        return result
    def re_others(self,response,poc_re_str):
        #此处先匹配{{}}进行代码执行替换，然后实现字符串模板替换。$a形式
        poc_re_str = self.replace_Template_var(poc_re_str)
        if poc_re_str:
            pattern = r'\{\{(.*?)\}\}'
            result = re.findall(pattern, poc_re_str)
            if result:
                for item in result:
                    try:
                        try:
                            var_str = str(eval(item))
                        except Exception as e:
                            self.out_error_info("eval code",e,"代码["+item+"] 执行错误："+str(e))
                            var_str=""
                        poc_re_str =poc_re_str.replace("{{%s}}"%item,var_str)
                    except Exception as e:
                        self.out_error_info("eval code",e,str(e))
            # poc_re_str = self.replace_Template_var(poc_re_str)
            return poc_re_str
        else:
            return ""

    def out_error_info(self,type_str,e,text):
        tqdm.write(Fore.RED+"[E] ["+str(e.__traceback__.tb_lineno).strip()+"行]["+self.poc.get("name")+"]["+type_str+"] "+text)
    def out_debug_info(self,type,text):
        return Fore.MAGENTA +"["+Fore.CYAN+"Debug"+Fore.MAGENTA+"]["+Fore.CYAN+type+Fore.MAGENTA+"] "+text
    def main_poc_expression(self,expression):
        poc_expression = self.replace_Template_var(expression)
        poc_expression =expression.replace("&&"," and ").replace("||"," or ")
        for i in self.all_request_name_list:
            poc_expression = poc_expression.replace(str(i)+"()",str(self.all_request_name_list[i]))
            # print(poc_expression)
        if self.debug:
            tqdm.write(self.out_debug_info("Main Expression","原始字符串：%s 替换后:%s"%(expression,poc_expression)))
        try:
            if eval(poc_expression):
                return True
            else:
                return False
        except Exception as e:
            self.out_error_info("eval code",e,"代码["+poc_expression+"] 执行错误："+str(e))

    def set_payload(self,poc_set):
        try:
            if  poc_set:
                for i in poc_set.keys():
                    try:
                        self.all_global_payload[i]=poc_set[i]
                    except Exception as e:
                        self.out_error_info("set payload",e,"Payload名:"+i+" Payload值:"+poc_set[i]+" 错误信息:"+str(e))
                    if self.debug:
                        tqdm.write(self.out_debug_info("set payload", "Payload名%s Payload值:%s"%(i,poc_set[i])))
                    # exec(f'global {i}\n{i}={poc_set[i]}')
        except Exception as e:
            self.out_error_info("set var",e,"设置变量出错:"+str(e))

    def set_bianliang(self,poc_set):
        try:
            if  poc_set:
                for i in poc_set.keys():
                    try:
                        exec(f'self.all_global_var[i]={poc_set[i]}')
                    except Exception as e:
                        self.out_error_info("set var",e,"变量名:"+i+" 变量值:"+poc_set[i]+" 错误信息:"+str(e))
                    if self.debug:
                        tqdm.write(self.out_debug_info("set var", "变量名：%s 变量Str:%s 变量值:%s"%(i,poc_set[i],self.all_global_var[i])))
                    # exec(f'global {i}\n{i}={poc_set[i]}')
        except Exception as e:
            self.out_error_info("set var",e,"设置变量出错:"+str(e))
    def poc_request_http(self,poc_rules):
        try:
            # r = s.post(url,headers=headers)
            for i in poc_rules:
                request_methods= poc_rules[i].get("request").get("method").strip()
                request_path= poc_rules[i].get("request").get("path").strip()
                request_headers= poc_rules[i].get("request").get("headers")
                request_body= poc_rules[i].get("request").get("body")
                request_body =self.replace_Template_var(request_body)
                request_headers =self.replace_Template_var_headers(request_headers)
                if not request_headers.get("User-Agent"):
                    request_headers['User-Agent']  =  random.choice(user_agent_list)
                if self.debug:
                    #debug
                    http_request_str="[%s] HTTP请求:%s\n%s\n%s %s\nHost: %s\n"%(self.poc.get("name"),i,"-"*100,request_methods,request_path,self.url)
                    if len(request_headers)>0:
                        for header in request_headers:
                            if header:
                                http_request_str+="%s: %s\n"%(header,str(request_headers[header]))
                    if request_body:
                        http_request_str+="\n%s"%(str(request_body)+"\n"+"-"*100)
                        
                    tqdm.write(self.out_debug_info("Request",http_request_str) )
                if request_path.startswith("^"):
                    request_url = self.url
                elif  request_path.strip().startswith("/"):
                    if self.url.strip().endswith("/"):
                        request_url = self.url[:-1].strip()+ request_path.strip()
                    else:
                        request_url = self.url.strip()+ request_path.strip()
                else:
                    request_url = self.url.strip()+ "/"+request_path.strip()
                # request_methods= poc_rules[i].get("request").get("method")
                request_url =self.replace_Template_var(request_url)
                # print(request_url)
                output_list= poc_rules[i].get("output")

                if poc_rules[i].get("request").get("follow_redirects"):
                    request_follow_redirects= True
                else:
                    request_follow_redirects= False
                try:
                    response = self.single_request_http(request_url,request_methods,request_body,request_headers,request_follow_redirects)
                except requests.exceptions.RequestException as e:
                    response="HTTP请求异常:"+str(e) 
                    # tqdm.write(response)
                    continue
                if self.debug:
                    #debug
                    return_result_str= "[%s][%s] HTTP返回:%s\n%s\n"%(self.poc.get("name"),request_url,i,'-'*100)
                    return_result_str += "HTTP/1.1 %s %s\n"%(response.status_code,response.reason)
                    if response.headers:
                        for zz in response.headers:
                            return_result_str += "%s: %s\n"%(zz,response.headers[zz])
                    if response.text:
                        return_result_str += "\n%s"%(response.text)
                    tqdm.write(self.out_debug_info("Response",return_result_str+"\n"+'-'*100) )
                expression =poc_rules[i].get("expression")
                expression = self.replace_Template_var(expression)
                expression =expression.replace("&&","and").replace("||","or")
                if self.is_expression(response,expression):
                    if self.debug:
                        tqdm.write(self.out_debug_info("Expression","判断条件:%s 判断结果:%s"%(expression,'True')))
                    self.all_request_name_list[i] = True
                    # exec(f'global {i}\n{i}=True')
                    self.output_var(response,output_list)
                    #匹配成功读取output做环境变量
                else:
                    self.all_request_name_list[i] = False
                    if self.debug:
                        tqdm.write(self.out_debug_info("Expression","判断条件:%s 判断结果:%s"%(expression,'Flase')))
                    # exec(f'global {i}\n{i}=False')
                    #失败则下一个请求

            return response
        except Exception as e:
            self.out_error_info("poc rquests",e,str(e))
            # tqdm.write(Fore.RED+"[E] ["+self.poc.get("name")+"]"+str(e) + '----' + str(e.__traceback__.tb_lineno) + '行')
            return None
    def replace_Template_var(self,body):
        if body:
            temp_request_body = Template(body)
            try:
                # body = temp_request_body.substitute(self.all_global_var)
                body = temp_request_body.safe_substitute(self.all_global_var)
                temp2_request_body = Template(body)
                body = temp2_request_body.safe_substitute(self.all_global_payload)
            except Exception as e:
                self.out_error_info("replace template",e,"模板替换异常:"+str(e))
                # tqdm.write(Fore.RED+"[E] ["+self.poc.get("name")+"]"+str(e) + '----' + str(e.__traceback__.tb_lineno) + '行')
        return body
    def replace_Template_var_headers(self,headers):
        for i in headers:
            headers[i] = self.replace_Template_var(headers[i])
        return headers
    def is_expression(self,response,expression):
        # print(expression)
        # if response.status_code==200 and operator.contains(response.text,'html'):
        try:
            if eval(expression):
                return True
            else:
                return False
        except Exception as e:
            self.out_error_info("eval code",e,"代码["+expression+"] 执行错误："+str(e))
    
    def output_var(self,response,output_list):

        try:
            if output_list:
                for i in output_list:
                    replace_result = self.re_others(response,output_list[i])
                    self.all_global_var[i]   = replace_result
                    if self.debug:
                        tqdm.write(self.out_debug_info("Replace Output","变量名：%s 替换前:%s 替换后:%s"%(i,output_list[i],replace_result)))
        except Exception as e:
            self.out_error_info("output",e,str(e))
            # tqdm.write(Fore.RED+"[E] ["+self.poc.get("name")+"]"+str(e) + '----' + str(e.__traceback__.tb_lineno) + '行')

    def single_request_http(self,request_url,request_methods,data,headers,request_follow_redirects):
        response = self.session.request(request_methods.upper(), request_url,data=data,headers=headers,allow_redirects=request_follow_redirects,verify=False,timeout=self.timeout)
        # print(type(response.status_code), response.status_code)
        return response
# print(type(response.status_code), response.status_code)
# print(type(response.headers), response.headers)
# print(type(response.cookies), response.cookies)
# print(type(response.url), response.url)
# print(type(response.history), response.history)