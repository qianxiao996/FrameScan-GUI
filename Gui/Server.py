# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Server.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Server(object):
    def setupUi(self, Server):
        if not Server.objectName():
            Server.setObjectName(u"Server")
        Server.resize(359, 189)
        self.gridLayout = QGridLayout(Server)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_server = QLabel(Server)
        self.label_server.setObjectName(u"label_server")

        self.horizontalLayout.addWidget(self.label_server)

        self.lineEdit_server = QLineEdit(Server)
        self.lineEdit_server.setObjectName(u"lineEdit_server")

        self.horizontalLayout.addWidget(self.lineEdit_server)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_user = QLabel(Server)
        self.label_user.setObjectName(u"label_user")

        self.horizontalLayout_2.addWidget(self.label_user)

        self.lineEdit_user = QLineEdit(Server)
        self.lineEdit_user.setObjectName(u"lineEdit_user")

        self.horizontalLayout_2.addWidget(self.lineEdit_user)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_passwd = QLabel(Server)
        self.label_passwd.setObjectName(u"label_passwd")

        self.horizontalLayout_3.addWidget(self.label_passwd)

        self.lineEdit_passwd = QLineEdit(Server)
        self.lineEdit_passwd.setObjectName(u"lineEdit_passwd")

        self.horizontalLayout_3.addWidget(self.lineEdit_passwd)


        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 3)

        self.pushButton_ceshi = QPushButton(Server)
        self.pushButton_ceshi.setObjectName(u"pushButton_ceshi")

        self.gridLayout.addWidget(self.pushButton_ceshi, 3, 0, 1, 1)

        self.pushButton_save = QPushButton(Server)
        self.pushButton_save.setObjectName(u"pushButton_save")

        self.gridLayout.addWidget(self.pushButton_save, 3, 1, 1, 1)

        self.pushButton_exit = QPushButton(Server)
        self.pushButton_exit.setObjectName(u"pushButton_exit")

        self.gridLayout.addWidget(self.pushButton_exit, 3, 2, 1, 1)


        self.retranslateUi(Server)
        self.pushButton_exit.clicked.connect(Server.close)

        QMetaObject.connectSlotsByName(Server)
    # setupUi

    def retranslateUi(self, Server):
        Server.setWindowTitle(QCoreApplication.translate("Server", u"\u63d2\u4ef6\u670d\u52a1\u5668\u8bbe\u7f6e", None))
        self.label_server.setText(QCoreApplication.translate("Server", u"\u670d\u52a1\u5668\uff1a", None))
        self.lineEdit_server.setText(QCoreApplication.translate("Server", u"http://127.0.0.1:8088/", None))
        self.label_user.setText(QCoreApplication.translate("Server", u"\u7528\u6237\u540d\uff1a", None))
        self.lineEdit_user.setText(QCoreApplication.translate("Server", u"admin", None))
        self.label_passwd.setText(QCoreApplication.translate("Server", u"\u5bc6  \u7801\uff1a", None))
        self.lineEdit_passwd.setText(QCoreApplication.translate("Server", u"admin", None))
        self.pushButton_ceshi.setText(QCoreApplication.translate("Server", u"\u6d4b\u8bd5\u8fde\u63a5", None))
        self.pushButton_save.setText(QCoreApplication.translate("Server", u"\u4fdd\u5b58", None))
        self.pushButton_exit.setText(QCoreApplication.translate("Server", u"\u53d6\u6d88", None))
    # retranslateUi

