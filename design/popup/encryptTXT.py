# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'encryptTXT.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from PyQt5.Qt import QFileDialog
import os
import pyAesCrypt
import string
import random

class Ui_encryptTXT(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(690, 404)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_4.addWidget(self.lineEdit_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_2.addWidget(self.textEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionAbout_JET = QtWidgets.QAction(MainWindow)
        self.actionAbout_JET.setObjectName("actionAbout_JET")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def back_to_jet(self):
        from __main__ import window1, window4, window4_global
        window4_global_y = window4_global.geometry().y() - 30
        window1.move(window4_global.geometry().x(), window4_global_y)
        window1.show()
        window4_global.hide()
    def window4_choose_a_file(self):
        file_to_load1 = QFileDialog.getOpenFileName()[0]
        global window4_file_to_load2
        window4_file_to_load2 = str(file_to_load1)
        global file_extension, filename
        filename, file_extension = os.path.splitext(window4_file_to_load2)
        self.lineEdit.setText(window4_file_to_load2)
        self.label_2.show()
        self.lineEdit_2.show()
        self.pushButton.show()
        global window4_encryption
        window4_encryption = "null"
        if file_extension == ".aes":
            self.pushButton.setText("Decrypt")
            window4_encryption = "decrypt"
        else:
            self.pushButton.setText("Encrypt")
            window4_encryption = "encrypt"
    def window4_encryption(self):
        if window4_encryption == "encrypt":
            window4_password = self.lineEdit_2.text()
            if window4_password == "":
                self.lineEdit_2.setText("A password is necessary")
                QtTest.QTest.qWait(3000)
                self.lineEdit_2.setText("")
            else:
                self.textEdit.setText("")
                bufferSize = 64 * 1024
                self.textEdit.append("Setting the buffer size...")
                QtTest.QTest.qWait(1000)
                window4_password = self.lineEdit_2.text()
                self.textEdit.append("Recovering the password...")
                QtTest.QTest.qWait(1000)
                self.textEdit.append("Encrypting the file...")
                def randomStringDigits(stringLength=6):
                    var1SET = string.ascii_letters
                    var2SET = string.digits
                    #var3SET = string.punctuation

                    lettersAndDigits = var1SET + var2SET #+ var3SET
                    return ''.join(random.choice(lettersAndDigits) for i in range(6))
            
                window4_random_name = randomStringDigits(8)
                window4_file_name = ("saves/encryptTXT/"+window4_random_name+".aes")
                pyAesCrypt.encryptFile(window4_file_to_load2, window4_file_name, window4_password, bufferSize)
                QtTest.QTest.qWait(1000)
                self.textEdit.append("Cleaning up the tracks...")
                QtTest.QTest.qWait(1000)
                self.lineEdit.setText("")
                QtTest.QTest.qWait(1000)
                self.lineEdit_2.setText("")
                QtTest.QTest.qWait(1000)
                self.textEdit.append("Encryption complete, you can find your file in the saves/encryptEXE folder with the name: "+window4_random_name+".aes")
        if window4_encryption == "decrypt":
            window4_password = self.lineEdit_2.text()
            if window4_password == "":
                self.lineEdit_2.setText("A password is necessary")
                QtTest.QTest.qWait(3000)
                self.lineEdit_2.setText("")
            else:
                self.textEdit.setText("")
                bufferSize = 64 * 1024
                self.textEdit.append("Setting the buffer size...")
                QtTest.QTest.qWait(1000)
                window4_password = self.lineEdit_2.text()
                self.textEdit.append("Recovering the password...")
                QtTest.QTest.qWait(1000)
                self.textEdit.append("Decrypting the file...")
                def randomStringDigits(stringLength=6):
                    var1SET = string.ascii_letters
                    var2SET = string.digits
                    #var3SET = string.punctuation

                    lettersAndDigits = var1SET + var2SET #+ var3SET
                    return ''.join(random.choice(lettersAndDigits) for i in range(6))
            
                window4_random_name = randomStringDigits(8)
                window4_file_name = ("saves/encryptTXT/"+window4_random_name+".txt")
                pyAesCrypt.decryptFile(window4_file_to_load2, window4_file_name, window4_password, bufferSize)
                QtTest.QTest.qWait(1000)
                self.textEdit.append("Cleaning up the tracks...")
                QtTest.QTest.qWait(1000)
                self.lineEdit.setText("")
                QtTest.QTest.qWait(1000)
                self.lineEdit_2.setText("")
                QtTest.QTest.qWait(1000)
                self.textEdit.append("Decryption is complete, you can find your file in the saves/encryptEXE folder with the name: "+window4_random_name+".txt")
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "JET"))
        self.pushButton_2.setText(_translate("MainWindow", "Back"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.label_2.setText(_translate("MainWindow", "Password:"))
        self.pushButton.setText(_translate("MainWindow", "Encrypt"))
        self.label.setText(_translate("MainWindow", "Operation successfull"))
        self.actionAbout_JET.setText(_translate("MainWindow", "About JET"))
        self.pushButton_2.clicked.connect(self.back_to_jet)
        self.toolButton.clicked.connect(self.window4_choose_a_file)
        self.pushButton.clicked.connect(self.window4_encryption)
        self.label.hide()
        self.label_2.hide()
        self.pushButton.hide()
        self.lineEdit_2.hide()
        self.lineEdit.setReadOnly(True)
        self.textEdit.setReadOnly(True)
