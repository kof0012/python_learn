# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(489, 300)
        self.name = QtWidgets.QLabel(Form)
        self.name.setGeometry(QtCore.QRect(50, 60, 54, 12))
        self.name.setObjectName("name")
        self.pwss = QtWidgets.QLabel(Form)
        self.pwss.setGeometry(QtCore.QRect(50, 90, 54, 12))
        self.pwss.setObjectName("pwss")
        self.text_browser = QtWidgets.QTextBrowser(Form)
        self.text_browser.setGeometry(QtCore.QRect(230, 0, 256, 192))
        self.text_browser.setObjectName("text_browser")
        self.name_edit = QtWidgets.QLineEdit(Form)
        self.name_edit.setGeometry(QtCore.QRect(90, 60, 113, 20))
        self.name_edit.setObjectName("name_edit")
        self.pwss_edit = QtWidgets.QLineEdit(Form)
        self.pwss_edit.setGeometry(QtCore.QRect(90, 90, 113, 20))
        self.pwss_edit.setObjectName("pwss_edit")
        self.ok = QtWidgets.QPushButton(Form)
        self.ok.setGeometry(QtCore.QRect(10, 150, 75, 23))
        self.ok.setObjectName("ok")
        self.no = QtWidgets.QPushButton(Form)
        self.no.setGeometry(QtCore.QRect(120, 150, 75, 23))
        self.no.setObjectName("no")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.name.setText(_translate("Form", "名字"))
        self.pwss.setText(_translate("Form", "密码"))
        self.ok.setText(_translate("Form", "ok"))
        self.no.setText(_translate("Form", "no"))
