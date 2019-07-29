# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about_jet.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_popup_about_jet(object):
    def setupUi(self, popup_about_jet):
        popup_about_jet.setObjectName("popup_about_jet")
        popup_about_jet.resize(534, 251)
        self.centralwidget = QtWidgets.QWidget(popup_about_jet)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        popup_about_jet.setCentralWidget(self.centralwidget)

        self.retranslateUi(popup_about_jet)
        QtCore.QMetaObject.connectSlotsByName(popup_about_jet)

    def retranslateUi(self, popup_about_jet):
        _translate = QtCore.QCoreApplication.translate
        popup_about_jet.setWindowTitle(_translate("popup_about_jet", "About JET"))
        self.textBrowser.setHtml(_translate("popup_about_jet", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">JET</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This program was developed by one of the founders of JZ-Software.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">It was initially created for personal purposes but then we wanted to improve it by adding new encryption methods and new features.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Now it\'s one of our best projects and we hope you enjoy the user experience as we have enjoyed programming this software.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Of course this program is still under development and will be improved over time, this process is a bit long as we have other personal things to do and we take care of the programming only in the free time.</p></body></html>"))

