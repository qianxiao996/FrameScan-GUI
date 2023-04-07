# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Vuln_Info.ui'
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
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_From_Vuln_Info(object):
    def setupUi(self, From_Vuln_Info):
        if not From_Vuln_Info.objectName():
            From_Vuln_Info.setObjectName(u"From_Vuln_Info")
        From_Vuln_Info.resize(924, 594)
        icon = QIcon()
        icon.addFile(u":/logo/main.png", QSize(), QIcon.Normal, QIcon.Off)
        From_Vuln_Info.setWindowIcon(icon)
        self.gridLayout = QGridLayout(From_Vuln_Info)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(From_Vuln_Info)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(70, 35))
        self.label_2.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.vuln_name = QLabel(From_Vuln_Info)
        self.vuln_name.setObjectName(u"vuln_name")

        self.horizontalLayout_2.addWidget(self.vuln_name)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(From_Vuln_Info)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(70, 35))
        self.label.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout.addWidget(self.label)

        self.cms_name = QLabel(From_Vuln_Info)
        self.cms_name.setObjectName(u"cms_name")

        self.horizontalLayout.addWidget(self.cms_name)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_7 = QLabel(From_Vuln_Info)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(70, 32))
        self.label_7.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_13.addWidget(self.label_7)

        self.vuln_identifier = QLabel(From_Vuln_Info)
        self.vuln_identifier.setObjectName(u"vuln_identifier")
        self.vuln_identifier.setOpenExternalLinks(True)

        self.horizontalLayout_13.addWidget(self.vuln_identifier)


        self.verticalLayout_3.addLayout(self.horizontalLayout_13)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 3, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(From_Vuln_Info)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(40, 30))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.vuln_poc = QLabel(From_Vuln_Info)
        self.vuln_poc.setObjectName(u"vuln_poc")

        self.horizontalLayout_3.addWidget(self.vuln_poc)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_11 = QLabel(From_Vuln_Info)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(40, 30))

        self.horizontalLayout_5.addWidget(self.label_11)

        self.vuln_exp = QLabel(From_Vuln_Info)
        self.vuln_exp.setObjectName(u"vuln_exp")
        self.vuln_exp.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_5.addWidget(self.vuln_exp)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.pushButton_plugins_edit = QPushButton(From_Vuln_Info)
        self.pushButton_plugins_edit.setObjectName(u"pushButton_plugins_edit")
        self.pushButton_plugins_edit.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_6.addWidget(self.pushButton_plugins_edit)


        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 1, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(From_Vuln_Info)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(70, 32))
        self.label_4.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_4.addWidget(self.label_4)

        self.vuln_url = QLabel(From_Vuln_Info)
        self.vuln_url.setObjectName(u"vuln_url")
        self.vuln_url.setOpenExternalLinks(True)

        self.horizontalLayout_4.addWidget(self.vuln_url)


        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_9 = QLabel(From_Vuln_Info)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(70, 35))
        self.label_9.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_14.addWidget(self.label_9)

        self.vuln_file = QLabel(From_Vuln_Info)
        self.vuln_file.setObjectName(u"vuln_file")

        self.horizontalLayout_14.addWidget(self.vuln_file)


        self.gridLayout.addLayout(self.horizontalLayout_14, 2, 1, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(From_Vuln_Info)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(60, 32))

        self.verticalLayout_2.addWidget(self.label_5)

        self.vuln_miaoshu = QTextEdit(From_Vuln_Info)
        self.vuln_miaoshu.setObjectName(u"vuln_miaoshu")
        self.vuln_miaoshu.setMinimumSize(QSize(0, 0))
        self.vuln_miaoshu.setReadOnly(False)

        self.verticalLayout_2.addWidget(self.vuln_miaoshu)


        self.gridLayout.addLayout(self.verticalLayout_2, 3, 0, 1, 2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_13 = QLabel(From_Vuln_Info)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(60, 32))

        self.verticalLayout.addWidget(self.label_13)

        self.vuln_solution = QTextEdit(From_Vuln_Info)
        self.vuln_solution.setObjectName(u"vuln_solution")
        self.vuln_solution.setMinimumSize(QSize(0, 0))
        self.vuln_solution.setReadOnly(False)

        self.verticalLayout.addWidget(self.vuln_solution)


        self.gridLayout.addLayout(self.verticalLayout, 4, 0, 1, 2)


        self.retranslateUi(From_Vuln_Info)

        QMetaObject.connectSlotsByName(From_Vuln_Info)
    # setupUi

    def retranslateUi(self, From_Vuln_Info):
        From_Vuln_Info.setWindowTitle(QCoreApplication.translate("From_Vuln_Info", u"\u63d2\u4ef6\u8be6\u7ec6\u4fe1\u606f", None))
        self.label_2.setText(QCoreApplication.translate("From_Vuln_Info", u"\u6f0f\u6d1e\u540d\u79f0:", None))
        self.vuln_name.setText("")
        self.label.setText(QCoreApplication.translate("From_Vuln_Info", u"CMS\u540d\u79f0:", None))
        self.cms_name.setText("")
        self.label_7.setText(QCoreApplication.translate("From_Vuln_Info", u"\u6f0f\u6d1e\u7f16\u53f7:", None))
        self.vuln_identifier.setText("")
        self.label_3.setText(QCoreApplication.translate("From_Vuln_Info", u"POC:", None))
        self.vuln_poc.setText(QCoreApplication.translate("From_Vuln_Info", u"\u65e0", None))
        self.label_11.setText(QCoreApplication.translate("From_Vuln_Info", u"EXP:", None))
        self.vuln_exp.setText(QCoreApplication.translate("From_Vuln_Info", u"\u65e0", None))
        self.pushButton_plugins_edit.setText(QCoreApplication.translate("From_Vuln_Info", u"\u7f16\u8f91\u63d2\u4ef6", None))
        self.label_4.setText(QCoreApplication.translate("From_Vuln_Info", u"\u6f0f\u6d1e\u94fe\u63a5:", None))
        self.vuln_url.setText("")
        self.label_9.setText(QCoreApplication.translate("From_Vuln_Info", u"\u63d2\u4ef6\u4f4d\u7f6e:", None))
        self.vuln_file.setText("")
        self.label_5.setText(QCoreApplication.translate("From_Vuln_Info", u"\u8be6\u7ec6\u63cf\u8ff0", None))
        self.vuln_miaoshu.setHtml(QCoreApplication.translate("From_Vuln_Info", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("From_Vuln_Info", u"\u4fee\u590d\u5efa\u8bae", None))
        self.vuln_solution.setHtml(QCoreApplication.translate("From_Vuln_Info", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

