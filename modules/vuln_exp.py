import importlib,eventlet
from urllib.parse import urlparse

from PyQt5.QtCore import QThread, pyqtSignal

class Vuln_exp(QThread):
    """该线程用于计算耗时的累加操作"""
    _sum = pyqtSignal(dict)  # 信号类型 str

    def __init__(self,exp_path,url,heads_dict,cookie,exp_type,cmd,ip,port):
        super().__init__()
        self.exp_path = exp_path
        self.url = url
        self.heads_dict = heads_dict
        self.cookie = cookie
        self.exp_type = exp_type
        self.cmd =cmd
        self.ip =ip
        self.port =port

    def run(self):
        try:
            eventlet.monkey_patch(time=True)
            with eventlet.Timeout(20,False):
                try:
                    _url = urlparse(self.url)
                    hostname = _url.hostname
                    port = _url.port
                    scheme = _url.scheme
                    if port is None and scheme == 'https':
                        port = 443
                    elif port is None:
                        port = 80
                    url = scheme + '://' + hostname + ':' + str(port) + '/'
                    # print(url)
                    nnnnnnnnnnnn1 = importlib.machinery.SourceFileLoader(self.exp_path[:-3], self.exp_path).load_module()            
                    vuln_info = nnnnnnnnnnnn1.do_exp(url,self.heads_dict,self.cookie,self.exp_type,self.cmd,self.ip,int(self.port))
                    # print(vuln_info)
                    self._sum.emit((vuln_info))  # 计算结果完成后，发送结果
                    return
                except Exception as  e:
                    self._sum.emit((['Error',str(e),'black']))
                    return
            self._sum.emit((['Error', self.exp_path+"插件运行超时",'black']))
        except Exception as e:
            self._sum.emit((['Error',str(e),'black']))
            return