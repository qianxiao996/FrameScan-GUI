import importlib
import json
import queue
import sys
import threading
import time
from socket import *
from urllib.parse import urlparse

sys.path.append('./Modules')
import BaseInfo
import CyberCalculate
import eventlet
from PyQt5.QtCore import QThread, pyqtSignal
class Vuln_Scanner(QThread):
    _data = pyqtSignal(dict)  # 信号类型 str  更新table
    _log = pyqtSignal(str)  # 信号类型 str 更新日志
    def __init__(self,plugins_dir_name,logger,timeout,jump_url,jump_fofa,threadnum,heads,target,poc_data,parent=None):
        super(Vuln_Scanner,self).__init__(parent)
        self.timeout = timeout
        self.vuln_portQueue = queue.Queue()
        self.plugins_dir_name =plugins_dir_name
        self.logger  =logger
        self.jump_url =jump_url
        self.jump_fofa =jump_fofa
        self.threadnum =threadnum
        self.heads =heads
        self.target =target
        self.poc_data =poc_data
    def run(self):
        #获取是否跳过fofa检测

        if self.jump_fofa:
            check_fofa ="1"
        else:
            check_fofa="0"
        heads = self.heads.splitlines()
        self.heads={}
        for head in heads:
            head = head.split(':')
            self.heads[head[0].strip()] = head[1].strip()


        if not self.target:
            self._log.emit('未获取到URL地址')
            self._log.emit("扫描结束")

            return

        # print(poc_data)
        if not self.poc_data:
            self._log.emit("未选择插件。")
            self._log.emit("扫描结束。")

            return
        else:
            self._log.emit("共加载%s个插件。" % (len(self.poc_data)))
            self._log.emit("共获取到%s个URL地址。" % (len(self.target)))
            self._log.emit( "正在创建队列...")
            self.add_queue(check_fofa)
    def add_queue(self,check_fofa):
        # print(poc_data)
        num = 0
        if not self.jump_url:
            num= len(self.target)
            for u in self.target:
                _url = urlparse(u)
                hostname = _url.hostname
                port = _url.port
                scheme = _url.scheme
                if port is None and scheme == 'https':
                    port = 443
                elif port is None:
                    port = 80
                if scheme=="http" and port == 80 or scheme=="https" and port == 443:
                    u = scheme + '://' + hostname +'/'
                else:
                    u = scheme + '://' + hostname + ':' + str(port) + '/'
                for xuanzhong_data in self.poc_data:
                    # print(xuanzhong_data)
                    filename =self.plugins_dir_name+'/' + xuanzhong_data['cms_name'] + '/' + xuanzhong_data['vuln_file']
                    #url  filename heads poc fofa_link  fofa  check_fofa
                    self.vuln_portQueue.put(u + '$$$' + filename + '$$$' + json.dumps(self.heads)+'$$$'+xuanzhong_data['vuln_name'] +'$$$'+xuanzhong_data['FofaQuery_link'] +'$$$'+xuanzhong_data['FofaQuery']+'$$$'+check_fofa)

        elif self.jump_url:
            self._log.emit("正在进行地址存活检测...")
            false_url =[]
            for u in self.target:
                _url = urlparse(u)
                hostname = _url.hostname
                port = _url.port
                scheme = _url.scheme
                if port is None and scheme == 'https':
                    port = 443
                    u = scheme + '://' + hostname + '/'
                elif port is None:
                    port = 80
                    u = scheme + '://' + hostname + '/'
                else:
                    u = scheme + '://' + hostname + ':' + str(port) + '/'
                try:
                    if u not in false_url:
                        time22 =self.timeout
                        result = self.port_scanner(hostname,port,time22)
                        if result:
                            for xuanzhong_data in self.poc_data:
                                # print(poc_data)
                                filename = self.plugins_dir_name + '/' + xuanzhong_data['cms_name'] + '/' + \
                                           xuanzhong_data['vuln_file']
                                self.vuln_portQueue.put(
                                    u + '$$$' + filename + '$$$' + json.dumps(self.heads) + '$$$' + xuanzhong_data[
                                        'vuln_name'] + '$$$' + xuanzhong_data['FofaQuery_link'] + '$$$' +
                                    xuanzhong_data[
                                        'FofaQuery'] + '$$$' + check_fofa)

                            num += 1
                        else:
                            false_url.append(u)
                            self._log.emit("%s----无法访问。"%u)

                    else:
                        continue
                except Exception as  e:
                    self.logger.error(str(e) + '----' + str(e.__traceback__.tb_lineno) + '行')
                    false_url.append(u)
                    self._log.emit("%s----无法访问。" %u)

                    continue
                    # 限制线程数小于队列大小
        self._log.emit("共获取到%s个有效URL地址。"%num)
        if self.threadnum > self.vuln_portQueue.qsize():
            self.threadnum = self.vuln_portQueue.qsize()
        # print(portQueue.qsize())
        if num==0:
            self._log.emit("扫描结束。")
            return
        else:
            self._log.emit("扫描开始...")
            self.thread_list=[]
            for i in range(self.threadnum):
                thread = threading.Thread(target=self.vuln_scan, args=())
                thread.setDaemon(True)  # 设置为后台线程，这里默认是False，设置为True之后则主线程不用等待子线程
                self.thread_list.append(thread)

            for i in self.thread_list:
                i.start()
            for i in self.thread_list:
                i.join()
            self._log.emit("扫描结束!")


    def vuln_scan(self):
        # print(portQueue.queue)  #输出所有队列

        while 1:
            try:
                if self.vuln_portQueue.empty() :  # 队列空就结束
                    return
                else:
                    # url  filename heads vuln_name fofa_link  fofa  check_fofa
                    all = self.vuln_portQueue.get().split('$$$')  # 从队列中取出 #0
                    url = all[0]
                    filename = all[1]
                    heads_dict= json.loads(all[2])
                    vuln_name =all[3]
                    fofa_link = all[4]
                    fofa =  all[5]
                    check_fofa = all[6]
                    timeout = self.timeout
                    _url = urlparse(url)
                    hostname = _url.hostname
                    port = _url.port
                    scheme = _url.scheme
                    self.logger.info("Scanner:"+url+" "+vuln_name)
                    self._log.emit("正在扫描【%s】" % vuln_name)
                    if port is None and scheme == 'https':
                        port = 443
                    elif port is None:
                        port = 80
                    if check_fofa=="1":
                        if fofa and fofa_link!="all":
                            fofa_url= url+'/'+fofa_link
                        if fofa and fofa_link == "all":
                            fofa_url = url
                        fofaquery = fofa.lower()
                        responce = BaseInfo.http_info(fofa_url)
                        oOperand = {"data": responce}
                        oCyberCalc = CyberCalculate.CyberCalculate(szHayStack=oOperand, szRule=fofaquery,szSplit='=')
                        blMatch = oCyberCalc.Calculate()
                        # print(fofaquery[0])
                        if blMatch:
                            # 超时限制
                            try:
                                eventlet.monkey_patch(thread=False, time=True)
                                with eventlet.Timeout(timeout, False):
                                    nnnnnnnnnnnn1 = importlib.machinery.SourceFileLoader(filename[:-3], filename).load_module()
                                    result = nnnnnnnnnnnn1.do_poc(url,hostname,port,scheme,heads_dict)
                                    #存在
                                    self.scan_result_out(result,all)
                                    continue
                                self._log.emit("Error:%s脚本运行超时！" % filename)
                                continue
                            except Exception as e:
                                self.logger.error(str(e) + '----' + str(e.__traceback__.tb_lineno) + '行')
                                self._log.emit(
                                    "Error:%s----%s----%s。" % (url, vuln_name, '脚本运行超时'))
                                continue
                            #进行扫描
                        else:
                            self._log.emit("%s----%s----%s。" % (url, vuln_name, 'FoFA信息不匹配'))

                    else:
                        #超时限制
                        try:
                            eventlet.monkey_patch(thread=False,time=True)
                            with eventlet.Timeout(timeout,False):
                                try:
                                    # print(url)
                                    nnnnnnnnnnnn1 = importlib.machinery.SourceFileLoader(filename[:-3], filename).load_module()
                                    result = nnnnnnnnnnnn1.do_poc(url,hostname,port,scheme,heads_dict)
                                    # print(result)
                                    self.scan_result_out(result,all)
                                    continue
                                except Exception as  e:
                                    self.logger.error(str(e) + '----' + str(e.__traceback__.tb_lineno) + '行')
                                    self._log.emit(
                                        "Error:%s脚本执行错误！<br>[Exception]:<br>%s" % (filename, e))
                                    continue
                            self._log.emit(
                                "Error:%s脚本运行超时！" % (filename))
                        except Exception as e:
                            self.logger.error(str(e) + '----' + str(e.__traceback__.tb_lineno) + '行')
                            self._log.emit(
                                "Error:%s----%s----%s。" % (url, vuln_name, '脚本运行超时'))
                            continue
            except Exception as e:
                self.logger.error(str(e) + '----' + str(e.__traceback__.tb_lineno) + '行')
                self._log.emit(
                    "Error:%s脚本执行错误！<br>[Exception]:<br>%s" % (filename, str(e)))
                continue
    def scan_result_out(self,result,all):
        result['url'] = all[0]
        result['poc_file'] = all[1]
        result['poc_name'] = all[3]
        self._data.emit(result)



    def port_scanner(self,host,port,timeout):
        #返回0不存活 1存活
        try:
            tcp = socket(AF_INET, SOCK_STREAM)
            tcp.settimeout(int(timeout))  # 如果设置太小，检测不精确，设置太大，检测太慢
            # print(host,port)
            result = tcp.connect_ex((host, int(port)))  # 效率比connect高，成功时返回0，失败时返回错误码
            # print(port+"success")
            if result == 0:
                return 1
            else:
                return 0
        except Exception as e:
             self.logger.error(str(e) + '----' + str(e.__traceback__.tb_lineno) + '行')
             return 0
        finally:
            try:
                tcp.close()
            except:
                pass