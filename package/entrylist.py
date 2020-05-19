# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'entrylist.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 496)
        MainWindow.setStyleSheet("QPushButton { \n"
"background-color:rgb(51, 153, 255); \n"
"border: 4px solid white;\n"
"padding: 6px 10px;\n"
"font: 75 12pt \"System\";\n"
"}\n"
"#centralwidget{\n"
"border: 2px solid cyan;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(153, 245, 230, 255), stop:0.09 rgba(220, 246, 236, 255), stop:0.14 rgba(150, 239, 246, 255), stop:0.187702 rgba(73, 187, 241, 255), stop:0.25 rgba(40, 151, 232, 255), stop:0.32 rgba(243, 248, 224, 255), stop:0.385 rgba(162, 249, 213, 237), stop:0.47 rgba(109, 168, 162, 227), stop:0.58 rgba(186, 232, 191, 232), stop:0.65 rgba(255, 255, 255, 255), stop:0.75 rgba(46, 142, 222, 255), stop:0.805 rgba(117, 187, 218, 255), stop:0.86 rgba(175, 254, 231, 255), stop:0.925566 rgba(254, 236, 244, 255), stop:1 rgba(191, 230, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(153, 245, 230, 255), stop:0.09 rgba(220, 246, 236, 255), stop:0.14 rgba(150, 239, 246, 255), stop:0.187702 rgba(73, 187, 241, 255), stop:0.25 rgba(40, 151, 232, 255), stop:0.32 rgba(243, 248, 224, 255), stop:0.385 rgba(162, 249, 213, 237), stop:0.47 rgba(109, 168, 162, 227), stop:0.58 rgba(186, 232, 191, 232), stop:0.65 rgba(255, 255, 255, 255), stop:0.75 rgba(46, 142, 222, 255), stop:0.805 rgba(117, 187, 218, 255), stop:0.86 rgba(175, 254, 231, 255), stop:0.925566 rgba(254, 236, 244, 255), stop:1 rgba(191, 230, 255, 255));\n"
"border: 3px solid white;\n"
"padding: 6px 10px;\n"
"font: 75 16pt \"System\";\n"
"}\n"
"\n"
"QTextEdit{\n"
"border:2px dot-dot-dash;\n"
"border-top-style: solid;\n"
"border-color: blue;\n"
"}\n"
"\n"
"QLineEdit{\n"
"border: 2px solid grey;\n"
"border-radius: 2px 2px;\n"
"}\n"
"\n"
"QLabel{\n"
"font: 10pt \"MS Gothic\";\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.item_list = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.item_list.setFont(font)
        self.item_list.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(141, 243, 181, 255), stop:0.316384 rgba(237, 255, 174, 255), stop:0.847458 rgba(174, 255, 201, 255));\n"
"border: 2px solid balck;\n"
"border-radius: 10px 5px;")
        self.item_list.setObjectName("item_list")
        self.horizontalLayout.addWidget(self.item_list)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.pushButton_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout.addWidget(self.pushButton_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Entry List Window"))
        self.pushButton_cancel.setText(_translate("MainWindow", "Cancel"))
