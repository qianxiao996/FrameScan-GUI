import eventlet
import importlib
from urllib.parse import urlparse

from PyQt5.QtCore import QThread, pyqtSignal


class Vuln_Exp(QThread):
    """该线程用于计算耗时的累加操作"""
    _data = pyqtSignal(dict)  # 信号类型 str
    def __init__(self,exp_path,url,heads_dict,exp_data,parent=None):
        super(Vuln_Exp,self).__init__(parent)
        self.exp_path = exp_path
        self.url = url
        self.heads_dict = heads_dict
        self.exp_data = exp_data

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
                        url = scheme + '://' + hostname +'/'
                    elif port is None:
                        port = 80
                        url = scheme + '://' + hostname + '/'
                    else:
                        url = scheme + '://' + hostname + ':' + str(port) + '/'
                    # print(url)
                    nnnnnnnnnnnn1 = importlib.machinery.SourceFileLoader(self.exp_path[:-3], self.exp_path).load_module()
                    vuln_info = nnnnnnnnnnnn1.do_exp(url,hostname,port,scheme,self.heads_dict,self.exp_data)
                    # print(vuln_info)
                    self._data.emit((vuln_info))  # 计算结果完成后，发送结果
                    return
                except Exception as  e:
                    self._data.emit({'Error_Info':str(e)})
                    return
            self._data.emit({'Error_Info':str(e)})
            return
        except Exception as e:
            self._data.emit({'Error_Info':str(e)})
            return