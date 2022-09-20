import inspect
import os
import eventlet
from urllib.parse import urlparse
from PyQt5.QtCore import QThread, pyqtSignal
import frozen_dir
import Public
SETUP_DIR = frozen_dir.app_path()


class Vuln_Exp(QThread):
    """该线程用于计算耗时的累加操作"""
    _data = pyqtSignal(dict)  # 信号类型 str

    def __init__(self, exp_path, url, heads_dict, exp_data, plugins_temp_data,parent=None):
        super(Vuln_Exp, self).__init__(parent)
        self.exp_path = exp_path
        self.url = url
        self.heads_dict = heads_dict
        self.exp_data = exp_data
        self.plugins_temp_data =plugins_temp_data


    def run(self):
        try:
            eventlet.monkey_patch(time=True)
            with eventlet.Timeout(20, False):
                try:
                    _url = urlparse(self.url)
                    hostname = _url.hostname
                    port = _url.port
                    scheme = _url.scheme
                    path = _url.path

                    if port is None and scheme == 'https':
                        port = 443
                    elif port is None:
                        port = 80
                    if (scheme == "http" and port == 80) or (scheme == "https" and port == 443):
                        url = scheme + '://' + hostname + path
                    else:
                        url = scheme + '://' + hostname + ':' + str(port) + path
                    if 'http://' not in url.lower() and 'http' not in url.lower():
                        url = 'http://' + hostname + ':' + str(port) + path
                    file_path = SETUP_DIR+"/"+os.path.splitext(self.exp_path)[0]
                    nnnnnnnnnnnn1 = Public.get_obj_by_path(file_path)
                    if nnnnnnnnnnnn1:
                        Function_Out = getattr(self, 'scan_log_out')  # 以字符串的形式执行函数
                        result = nnnnnnnnnnnn1.do_exp(url,hostname,port,scheme,self.heads_dict,self.exp_data,Function_Out,self.plugins_temp_data)
                        result['exp_type'] = 'result'
                        self._data.emit(result)  # 计算结果完成后，发送结果
                        return
                    else:
                        self.scan_log_out("Error", file_path + " 该模块未找到！")
                except Exception as  e:
                    self._update_log(str(e), 'Error')
                    return
            self._update_log('执行超时！')
            return
        except Exception as e:
            self._update_log(str(e), 'Error')
            return

    def _update_log(self, info, log_type='Info'):
        result = {"exp_type": "exp_log", "log_info": str(info), "log_type": log_type}
        self._data.emit(result)



    def scan_log_out(self, log_type="Debug", log_info=""):
        caller = inspect.stack()
        file_path = caller[1][1]
        file_path =os.path.splitext(file_path)[0]
        nnnnnnnnnnnn1 = Public.get_obj_by_path(file_path)
        if nnnnnnnnnnnn1:
            vuln_info = nnnnnnnnnnnn1.vuln_info()
            result = {
                "url": vuln_info.get('vuln_name'),
                "poc_file": file_path,
                "cms_name": vuln_info.get('cms_name'),
                'poc_name': vuln_info.get('vuln_name'),
                'exp_type': "exp_log",
                'log_info': str(log_info),
                'log_type': str(log_type)
            }
            self._data.emit(result)
        else:
            self.scan_log_out("Error", file_path + " 该模块未找到！")
