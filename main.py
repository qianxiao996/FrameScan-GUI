from PyQt5.QtCore import QThread ,  pyqtSignal,  QDateTime 
from PyQt5.QtWidgets import QApplication,  QDialog,  QLineEdit
import time
import sys


class Window(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle('PyQt 5界面实时更新例子')
        self.resize(400, 100)
        self.input = QLineEdit(self)
        self.input.resize(400, 100)
        self.initUI()

    def initUI(self):
        # from BackendThread import BackendThread
          # 创建线程
        aaa='aaa'
        bbb='adsd'
        module  =__import__("1.BackendThread", fromlist=['xxx']) #引入模块
        cls = getattr(module, "BackendThread2") #引入类
        self.backend  = cls()  #实例化类
        self.backend.name='aaa'
        self.backend.path='nnnn'
        # self.backend = BackendThread()
          # 连接信号
        self.backend.update_date.connect(self.handleDisplay)
          # 开始线程
        self.backend.start()

    # 将当前时间输出到文本框
    def handleDisplay(self, data):
        self.input.setText(data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show() 
    sys.exit(app.exec_())