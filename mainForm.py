# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(291, 382)
        self.leFIO = QtWidgets.QLineEdit(Form)
        self.leFIO.setGeometry(QtCore.QRect(10, 30, 271, 21))
        self.leFIO.setObjectName("leFIO")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 55, 18))
        self.label.setObjectName("label")
        self.leEMAIL = QtWidgets.QLineEdit(Form)
        self.leEMAIL.setGeometry(QtCore.QRect(10, 70, 271, 21))
        self.leEMAIL.setObjectName("leEMAIL")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 55, 18))
        self.label_2.setObjectName("label_2")
        self.lePHONE = QtWidgets.QLineEdit(Form)
        self.lePHONE.setGeometry(QtCore.QRect(10, 110, 271, 21))
        self.lePHONE.setObjectName("lePHONE")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 55, 18))
        self.label_3.setObjectName("label_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 149, 271, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gvIMAGE = QtWidgets.QGraphicsView(self.verticalLayoutWidget)
        self.gvIMAGE.setObjectName("gvIMAGE")
        self.verticalLayout.addWidget(self.gvIMAGE)
        self.pbCREATE = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pbCREATE.setObjectName("pbCREATE")
        self.verticalLayout.addWidget(self.pbCREATE)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "QR-??????????????????"))
        self.label.setText(_translate("Form", "??.??.??:"))
        self.label_2.setText(_translate("Form", "Email:"))
        self.label_3.setText(_translate("Form", "??????:"))
        self.pbCREATE.setText(_translate("Form", "?????????????? QR ??????"))
