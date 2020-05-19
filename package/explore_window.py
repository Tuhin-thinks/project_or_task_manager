# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'explore_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(644, 300)
        Dialog.setMinimumSize(QtCore.QSize(644, 300))
        Dialog.setMaximumSize(QtCore.QSize(644, 300))
        Dialog.setStyleSheet("QPushButton{\n"
"border: 1px solid black;\n"
"border-radius: 5px 5px;\n"
"padding: 2px;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed{\n"
"border: 1px solid black;\n"
"border-radius: 5px 5px;\n"
"padding: 2px;\n"
"background-color: rgb(233, 185, 110);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border: 1px solid grey;\n"
"border-radius: 5px 5px;\n"
"padding: 2px;\n"
"background-color: rgb(193, 125, 17);\n"
"font: 25 italic 11pt \"Ubuntu\";\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setStyleSheet("font: 11pt \"URW Gothic L\";")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.options = QtWidgets.QComboBox(Dialog)
        self.options.setStyleSheet("border: 2px solid black;\n"
"border-radius: 5px 5px;\n"
"padding: 5px 5px;\n"
"font: 11pt \"URW Gothic L\";")
        self.options.setObjectName("options")
        self.options.addItem("")
        self.options.addItem("")
        self.options.addItem("")
        self.options.addItem("")
        self.options.addItem("")
        self.options.addItem("")
        self.options.addItem("")
        self.options.addItem("")
        self.options.addItem("")
        self.options.addItem("")
        self.options.addItem("")
        self.options.addItem("")
        self.options.addItem("")
        self.horizontalLayout_2.addWidget(self.options)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_cancel = QtWidgets.QPushButton(Dialog)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout.addWidget(self.pushButton_cancel)
        self.pushButton_ok = QtWidgets.QPushButton(Dialog)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.horizontalLayout.addWidget(self.pushButton_ok)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Explore"))
        self.label.setText(_translate("Dialog", "SELECT AN OPTION:"))
        self.options.setItemText(0, _translate("Dialog", "---------------------- SELECT AN ITEM--------------------"))
        self.options.setItemText(1, _translate("Dialog", "Show Pending Jobs"))
        self.options.setItemText(2, _translate("Dialog", "Show Total Worth of Pending Jobs"))
        self.options.setItemText(3, _translate("Dialog", "Show Last Submission"))
        self.options.setItemText(4, _translate("Dialog", "Show Nearest Submission"))
        self.options.setItemText(5, _translate("Dialog", "Show Project Ideas"))
        self.options.setItemText(6, _translate("Dialog", "Show Project With Maximum Time Required"))
        self.options.setItemText(7, _translate("Dialog", "Show Personal Projects"))
        self.options.setItemText(8, _translate("Dialog", "Show Highest Individual worth: Project"))
        self.options.setItemText(9, _translate("Dialog", "Show Lowest Individual Worth: Project"))
        self.options.setItemText(10, _translate("Dialog", "Create Report of All Pending Jobs"))
        self.options.setItemText(11, _translate("Dialog", "Create Report of All Jobs"))
        self.options.setItemText(12, _translate("Dialog", "Reinitialize Project ID\'s"))
        self.pushButton_cancel.setText(_translate("Dialog", "CANCEL"))
        self.pushButton_ok.setText(_translate("Dialog", "OK"))
