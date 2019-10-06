# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'showPlugins.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1452, 821)
        self.show_Plugins = QtWidgets.QTableWidget(Form)
        self.show_Plugins.setGeometry(QtCore.QRect(-1, 0, 1461, 821))
        self.show_Plugins.setSizeIncrement(QtCore.QSize(0, 0))
        self.show_Plugins.setObjectName("show_Plugins")
        self.show_Plugins.setColumnCount(5)
        self.show_Plugins.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.show_Plugins.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.show_Plugins.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.show_Plugins.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.show_Plugins.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.show_Plugins.setHorizontalHeaderItem(4, item)
        self.show_Plugins.horizontalHeader().setVisible(True)
        self.show_Plugins.horizontalHeader().setCascadingSectionResizes(False)
        self.show_Plugins.horizontalHeader().setDefaultSectionSize(279)
        self.show_Plugins.horizontalHeader().setHighlightSections(True)
        self.show_Plugins.horizontalHeader().setSortIndicatorShown(False)
        self.show_Plugins.verticalHeader().setSortIndicatorShown(False)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Show Plugins"))
        item = self.show_Plugins.horizontalHeaderItem(0)
        item.setText(_translate("Form", "CMS_NAME"))
        item = self.show_Plugins.horizontalHeaderItem(1)
        item.setText(_translate("Form", "POC_NAME"))
        item = self.show_Plugins.horizontalHeaderItem(2)
        item.setText(_translate("Form", "POC_REFERER"))
        item = self.show_Plugins.horizontalHeaderItem(3)
        item.setText(_translate("Form", "POC_DESCRIPTION"))
        item = self.show_Plugins.horizontalHeaderItem(4)
        item.setText(_translate("Form", "FILE_NAME"))

