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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./img/main.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.show_Plugins = QtWidgets.QTableWidget(Form)
        self.show_Plugins.setGeometry(QtCore.QRect(-1, 20, 1461, 801))
        self.show_Plugins.setSizeIncrement(QtCore.QSize(0, 0))
        self.show_Plugins.setTabletTracking(False)
        self.show_Plugins.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
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
        self.show_Plugins.horizontalHeader().setCascadingSectionResizes(True)
        self.show_Plugins.horizontalHeader().setDefaultSectionSize(291)
        self.show_Plugins.horizontalHeader().setHighlightSections(False)
        self.show_Plugins.horizontalHeader().setSortIndicatorShown(False)
        self.show_Plugins.horizontalHeader().setStretchLastSection(True)
        self.show_Plugins.verticalHeader().setVisible(True)
        self.show_Plugins.verticalHeader().setCascadingSectionResizes(False)
        self.show_Plugins.verticalHeader().setSortIndicatorShown(False)
        self.show_Plugins_comboBox = QtWidgets.QComboBox(Form)
        self.show_Plugins_comboBox.setGeometry(QtCore.QRect(0, 0, 111, 21))
        self.show_Plugins_comboBox.setObjectName("show_Plugins_comboBox")
        self.show_Plugins_comboBox.addItem("")

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
        self.show_Plugins_comboBox.setItemText(0, _translate("Form", "ALL"))

