# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detailswindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(843, 513)
        Dialog.setStyleSheet("QPushButton{\n"
"background-color: rgb(238, 238, 236);\n"
"}\n"
"QPushButton:hover:!pressed{\n"
"background-color: rgb(52, 101, 164);\n"
"}\n"
"QPushButton:pressed{\n"
"color: rgb(238, 238, 236);\n"
"background-color: rgb(85, 87, 83);\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit_details = QtWidgets.QTextEdit(Dialog)
        self.textEdit_details.setStyleSheet("")
        self.textEdit_details.setObjectName("textEdit_details")
        self.gridLayout.addWidget(self.textEdit_details, 2, 0, 1, 4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        self.pushButton_close = QtWidgets.QPushButton(Dialog)
        self.pushButton_close.setStyleSheet("border: 2px solid grey;\n"
"border-radius: 10px 5px;\n"
"padding: 2px;\n"
"font: 25 italic 16pt \"Ubuntu\";")
        self.pushButton_close.setObjectName("pushButton_close")
        self.gridLayout.addWidget(self.pushButton_close, 3, 3, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(3)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 25 italic 17pt \"Ubuntu\";\n"
"color: rgb(65, 142, 241);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "DETAILS WINDOW"))
        self.textEdit_details.setPlaceholderText(_translate("Dialog", "Fetch Details From The DataBase"))
        self.pushButton_close.setText(_translate("Dialog", "CLOSE"))
        self.label.setText(_translate("Dialog", "Your Required Details are as Follows:"))
