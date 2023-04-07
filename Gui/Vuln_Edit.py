# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Vuln_Edit.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Form_Vuln_Edit(object):
    def setupUi(self, Form_Vuln_Edit):
        if not Form_Vuln_Edit.objectName():
            Form_Vuln_Edit.setObjectName(u"Form_Vuln_Edit")
        Form_Vuln_Edit.resize(1459, 821)
        icon = QIcon()
        icon.addFile(u":/logo/main.png", QSize(), QIcon.Normal, QIcon.Off)
        Form_Vuln_Edit.setWindowIcon(icon)
        Form_Vuln_Edit.setLayoutDirection(Qt.LeftToRight)
        Form_Vuln_Edit.setAutoFillBackground(False)
        Form_Vuln_Edit.setStyleSheet(u"")
        Form_Vuln_Edit.setInputMethodHints(Qt.ImhNone)
        self.gridLayout = QGridLayout(Form_Vuln_Edit)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_10 = QLabel(Form_Vuln_Edit)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 0))
        self.label_10.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout.addWidget(self.label_10)

        self.label_vuln_id = QLabel(Form_Vuln_Edit)
        self.label_vuln_id.setObjectName(u"label_vuln_id")
        self.label_vuln_id.setMinimumSize(QSize(30, 0))

        self.horizontalLayout.addWidget(self.label_vuln_id)

        self.label = QLabel(Form_Vuln_Edit)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.comboBox_vuln_cms = QComboBox(Form_Vuln_Edit)
        self.comboBox_vuln_cms.setObjectName(u"comboBox_vuln_cms")
        self.comboBox_vuln_cms.setMinimumSize(QSize(150, 0))
        self.comboBox_vuln_cms.setEditable(True)

        self.horizontalLayout.addWidget(self.comboBox_vuln_cms)

        self.label_9 = QLabel(Form_Vuln_Edit)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(70, 35))
        self.label_9.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.label_9)

        self.lineEdit_vuln_file = QLineEdit(Form_Vuln_Edit)
        self.lineEdit_vuln_file.setObjectName(u"lineEdit_vuln_file")

        self.horizontalLayout.addWidget(self.lineEdit_vuln_file)

        self.pushButton_vuln_save = QPushButton(Form_Vuln_Edit)
        self.pushButton_vuln_save.setObjectName(u"pushButton_vuln_save")

        self.horizontalLayout.addWidget(self.pushButton_vuln_save)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.vuln_exp_textEdit_shell = QTextEdit(Form_Vuln_Edit)
        self.vuln_exp_textEdit_shell.setObjectName(u"vuln_exp_textEdit_shell")

        self.verticalLayout.addWidget(self.vuln_exp_textEdit_shell)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Form_Vuln_Edit)

        QMetaObject.connectSlotsByName(Form_Vuln_Edit)
    # setupUi

    def retranslateUi(self, Form_Vuln_Edit):
        Form_Vuln_Edit.setWindowTitle(QCoreApplication.translate("Form_Vuln_Edit", u"\u6f0f\u6d1e\u63d2\u4ef6\u7f16\u8f91", None))
        self.label_10.setText(QCoreApplication.translate("Form_Vuln_Edit", u"ID:", None))
        self.label_vuln_id.setText(QCoreApplication.translate("Form_Vuln_Edit", u"None", None))
        self.label.setText(QCoreApplication.translate("Form_Vuln_Edit", u"\u5e94\u7528\u540d\u79f0:", None))
        self.label_9.setText(QCoreApplication.translate("Form_Vuln_Edit", u"\u63d2\u4ef6\u6587\u4ef6\u540d\u79f0:", None))
        self.pushButton_vuln_save.setText(QCoreApplication.translate("Form_Vuln_Edit", u"\u4fdd\u5b58\u63d2\u4ef6", None))
    # retranslateUi

