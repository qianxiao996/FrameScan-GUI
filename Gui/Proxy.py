# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Proxy.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QWidget)

class Ui_Proxy(object):
    def setupUi(self, Proxy):
        if not Proxy.objectName():
            Proxy.setObjectName(u"Proxy")
        Proxy.resize(254, 231)
        self.gridLayout_2 = QGridLayout(Proxy)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButton_proxy_enable = QRadioButton(Proxy)
        self.radioButton_proxy_enable.setObjectName(u"radioButton_proxy_enable")

        self.horizontalLayout.addWidget(self.radioButton_proxy_enable)

        self.radioButton_proxy_disabled = QRadioButton(Proxy)
        self.radioButton_proxy_disabled.setObjectName(u"radioButton_proxy_disabled")
        self.radioButton_proxy_disabled.setChecked(True)

        self.horizontalLayout.addWidget(self.radioButton_proxy_disabled)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Proxy)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.comboBox_proxy_type = QComboBox(Proxy)
        self.comboBox_proxy_type.addItem("")
        self.comboBox_proxy_type.addItem("")
        self.comboBox_proxy_type.addItem("")
        self.comboBox_proxy_type.setObjectName(u"comboBox_proxy_type")

        self.gridLayout.addWidget(self.comboBox_proxy_type, 0, 1, 1, 1)

        self.label_3 = QLabel(Proxy)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.lineEdit_proxy_ip = QLineEdit(Proxy)
        self.lineEdit_proxy_ip.setObjectName(u"lineEdit_proxy_ip")

        self.gridLayout.addWidget(self.lineEdit_proxy_ip, 1, 1, 1, 1)

        self.label_4 = QLabel(Proxy)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.lineEdit_proxy_port = QLineEdit(Proxy)
        self.lineEdit_proxy_port.setObjectName(u"lineEdit_proxy_port")

        self.gridLayout.addWidget(self.lineEdit_proxy_port, 2, 1, 1, 1)

        self.label_5 = QLabel(Proxy)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.lineEdit_proxy_username = QLineEdit(Proxy)
        self.lineEdit_proxy_username.setObjectName(u"lineEdit_proxy_username")
        self.lineEdit_proxy_username.setEnabled(False)

        self.gridLayout.addWidget(self.lineEdit_proxy_username, 3, 1, 1, 1)

        self.label_6 = QLabel(Proxy)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.lineEdit_proxy_passwd = QLineEdit(Proxy)
        self.lineEdit_proxy_passwd.setObjectName(u"lineEdit_proxy_passwd")
        self.lineEdit_proxy_passwd.setEnabled(False)

        self.gridLayout.addWidget(self.lineEdit_proxy_passwd, 4, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_proxy_save = QPushButton(Proxy)
        self.pushButton_proxy_save.setObjectName(u"pushButton_proxy_save")

        self.horizontalLayout_2.addWidget(self.pushButton_proxy_save)

        self.pushButton_proxy_close = QPushButton(Proxy)
        self.pushButton_proxy_close.setObjectName(u"pushButton_proxy_close")

        self.horizontalLayout_2.addWidget(self.pushButton_proxy_close)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)


        self.retranslateUi(Proxy)
        self.pushButton_proxy_close.clicked.connect(Proxy.close)

        QMetaObject.connectSlotsByName(Proxy)
    # setupUi

    def retranslateUi(self, Proxy):
        Proxy.setWindowTitle(QCoreApplication.translate("Proxy", u"Proxy", None))
        self.radioButton_proxy_enable.setText(QCoreApplication.translate("Proxy", u"\u542f\u7528", None))
        self.radioButton_proxy_disabled.setText(QCoreApplication.translate("Proxy", u"\u5173\u95ed", None))
        self.label.setText(QCoreApplication.translate("Proxy", u"\u7c7b\u578b", None))
        self.comboBox_proxy_type.setItemText(0, QCoreApplication.translate("Proxy", u"HTTP", None))
        self.comboBox_proxy_type.setItemText(1, QCoreApplication.translate("Proxy", u"SOCKS4", None))
        self.comboBox_proxy_type.setItemText(2, QCoreApplication.translate("Proxy", u"SOCKS5", None))

        self.label_3.setText(QCoreApplication.translate("Proxy", u"\u5730\u5740", None))
        self.lineEdit_proxy_ip.setText(QCoreApplication.translate("Proxy", u"127.0.0.1", None))
        self.label_4.setText(QCoreApplication.translate("Proxy", u"\u7aef\u53e3", None))
        self.lineEdit_proxy_port.setText(QCoreApplication.translate("Proxy", u"8080", None))
        self.label_5.setText(QCoreApplication.translate("Proxy", u"\u8d26\u6237", None))
        self.lineEdit_proxy_username.setText("")
        self.label_6.setText(QCoreApplication.translate("Proxy", u"\u5bc6\u7801", None))
        self.lineEdit_proxy_passwd.setText("")
        self.pushButton_proxy_save.setText(QCoreApplication.translate("Proxy", u"\u4fdd\u5b58", None))
        self.pushButton_proxy_close.setText(QCoreApplication.translate("Proxy", u"\u5173\u95ed", None))
    # retranslateUi

