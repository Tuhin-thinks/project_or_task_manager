# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project_manager.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(791, 611)
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
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_completebytime = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_completebytime.setObjectName("pushButton_completebytime")
        self.gridLayout.addWidget(self.pushButton_completebytime, 2, 2, 1, 1)
        self.pushButton_completestatus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_completestatus.setMinimumSize(QtCore.QSize(121, 61))
        self.pushButton_completestatus.setObjectName("pushButton_completestatus")
        self.gridLayout.addWidget(self.pushButton_completestatus, 0, 2, 1, 1)
        self.pushButton_editentriest = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_editentriest.setObjectName("pushButton_editentriest")
        self.gridLayout.addWidget(self.pushButton_editentriest, 3, 2, 1, 1)
        self.pushButton_loadprojectdef = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_loadprojectdef.setToolTipDuration(2)
        self.pushButton_loadprojectdef.setObjectName("pushButton_loadprojectdef")
        self.gridLayout.addWidget(self.pushButton_loadprojectdef, 2, 0, 1, 1)
        self.pushButton_projectprice = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_projectprice.setToolTipDuration(-1)
        self.pushButton_projectprice.setObjectName("pushButton_projectprice")
        self.gridLayout.addWidget(self.pushButton_projectprice, 3, 0, 1, 1)
        self.pushButton_addproject = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_addproject.sizePolicy().hasHeightForWidth())
        self.pushButton_addproject.setSizePolicy(sizePolicy)
        self.pushButton_addproject.setObjectName("pushButton_addproject")
        self.gridLayout.addWidget(self.pushButton_addproject, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.pushButton_addprojdef = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_addprojdef.setObjectName("pushButton_addprojdef")
        self.verticalLayout.addWidget(self.pushButton_addprojdef)
        self.textEdit_projectdefinition = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEdit_projectdefinition.setFont(font)
        self.textEdit_projectdefinition.setStyleSheet("background-color: rgba(255,255,255,200);")
        self.textEdit_projectdefinition.setObjectName("textEdit_projectdefinition")
        self.verticalLayout.addWidget(self.textEdit_projectdefinition)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 791, 22))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionCopy_Text = QtWidgets.QAction(MainWindow)
        self.actionCopy_Text.setObjectName("actionCopy_Text")
        self.actionPaste_Text = QtWidgets.QAction(MainWindow)
        self.actionPaste_Text.setObjectName("actionPaste_Text")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionClose_File = QtWidgets.QAction(MainWindow)
        self.actionClose_File.setObjectName("actionClose_File")
        self.actionDecrease_Project_Counter = QtWidgets.QAction(MainWindow)
        self.actionDecrease_Project_Counter.setObjectName("actionDecrease_Project_Counter")
        self.actionExplore = QtWidgets.QAction(MainWindow)
        self.actionExplore.setObjectName("actionExplore")
        self.actionReport = QtWidgets.QAction(MainWindow)
        self.actionReport.setObjectName("actionReport")
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionClose_File)
        self.menuMenu.addAction(self.actionExplore)
        self.menuMenu.addAction(self.actionReport)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.textEdit_projectdefinition, self.pushButton_projectprice)
        MainWindow.setTabOrder(self.pushButton_projectprice, self.pushButton_loadprojectdef)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Project Manager-by Tuhin"))
        self.pushButton_completebytime.setToolTip(_translate("MainWindow", "Add Project Deadline\n"
"None If not any"))
        self.pushButton_completebytime.setText(_translate("MainWindow", "COMPLETE BY TIME"))
        self.pushButton_completestatus.setToolTip(_translate("MainWindow", "Increases Project Counter\n"
"Consider Given Details as Your OFFICIAL PROJECT category"))
        self.pushButton_completestatus.setText(_translate("MainWindow", "Set Complete Status"))
        self.pushButton_editentriest.setToolTip(_translate("MainWindow", "<html><head/><body><p>Edit Entries in already in the database</p></body></html>"))
        self.pushButton_editentriest.setText(_translate("MainWindow", "Edit Entries"))
        self.pushButton_loadprojectdef.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Set  a short name to your project</span></p></body></html>"))
        self.pushButton_loadprojectdef.setText(_translate("MainWindow", "LOAD PROJECT NAME"))
        self.pushButton_projectprice.setToolTip(_translate("MainWindow", "<html><head/><body><p>Adds the project price</p><p>none if not any</p></body></html>"))
        self.pushButton_projectprice.setText(_translate("MainWindow", "DEFINE PROJECT PRICE"))
        self.pushButton_addproject.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">PRESS THIS AT THE END</span></p><p><br/></p><p><span style=\" color:#000000;\">TO ADD THE PROJECT TO THE RECORDS</span></p></body></html>"))
        self.pushButton_addproject.setText(_translate("MainWindow", "ADD PROJECT"))
        self.pushButton_addprojdef.setToolTip(_translate("MainWindow", "Add Written Definition To Records"))
        self.pushButton_addprojdef.setText(_translate("MainWindow", "ADD PROJECT\n"
"DEFINITION"))
        self.textEdit_projectdefinition.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionCopy_Text.setText(_translate("MainWindow", "Copy Text"))
        self.actionPaste_Text.setText(_translate("MainWindow", "Paste Text"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionClose_File.setText(_translate("MainWindow", "Close File"))
        self.actionDecrease_Project_Counter.setText(_translate("MainWindow", "Decrease Project Counter"))
        self.actionExplore.setText(_translate("MainWindow", "Explore"))
        self.actionReport.setText(_translate("MainWindow", "Report"))
