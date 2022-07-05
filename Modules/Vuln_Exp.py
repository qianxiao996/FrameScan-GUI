import os

import eventlet
import importlib
from urllib.parse import urlparse
import platform
from PyQt5.QtCore import QThread, pyqtSignal
import frozen_dir
SETUP_DIR = frozen_dir.app_path()

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
                    path = _url.path

                    if port is None and scheme == 'https':
                        port = 443
                        url = scheme + '://' + hostname +'/'+path
                    elif port is None:
                        port = 80
                        url = scheme + '://' + hostname + '/'+path
                    else:
                        url = scheme + '://' + hostname + ':' + str(port) + '/'+path
                    # print(url)
                    if os.path.isfile(self.exp_path + '.py'):
                        self.exp_path = self.exp_path + '.py'
                        nnnnnnnnnnnn1 = importlib.machinery.SourceFileLoader(
                            os.path.splitext(self.exp_path)[0], self.exp_path).load_module()
                    elif os.path.isfile(self.exp_path + '.pyc'):
                        self.exp_path = self.exp_path + '.pyc'
                        module_spec = importlib.util.spec_from_file_location(self.exp_path[:-4],
                                                                             self.exp_path)
                        nnnnnnnnnnnn1 = importlib.util.module_from_spec(module_spec)
                        module_spec.loader.exec_module(nnnnnnnnnnnn1)
                    else:
                        sysstr = platform.system()
                        if (sysstr == "Windows"):
                            self.exp_path = SETUP_DIR + "/" + self.exp_path + '.pyd'

                            # self.exp_path = self.exp_path + '.pyd'
                        elif (sysstr == "Linux"):
                            self.exp_path = self.exp_path + '.so'
                        loader_details = (
                            importlib.machinery.ExtensionFileLoader,
                            importlib.machinery.EXTENSION_SUFFIXES
                        )
                        tools_finder = importlib.machinery.FileFinder(
                            os.path.dirname(self.exp_path), loader_details)
                        # print("FileFinder: ", tools_finder)
                        toolbox_specs = tools_finder.find_spec(
                            os.path.basename(os.path.splitext(self.exp_path)[0]))
                        # print("find_spec: ", toolbox_specs)
                        nnnnnnnnnnnn1 = importlib.util.module_from_spec(toolbox_specs)
                        # print("module: ", nnnnnnnnnnnn1)
                        toolbox_specs.loader.exec_module(nnnnnnnnnnnn1)
                        # print("导入成功 path_import(): ", nnnnnnnnnnnn1)

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