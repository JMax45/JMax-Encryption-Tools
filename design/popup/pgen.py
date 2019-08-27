# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pgen.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
import string
import random

class Ui_pgen(object):
    def setupUi(self, pgen):
        pgen.setObjectName("pgen")
        pgen.resize(690, 404)
        self.centralwidget = QtWidgets.QWidget(pgen)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setMaximum(256)
        self.spinBox.setMinimum(1)
        self.spinBox.setProperty("value", 6)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout.addWidget(self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout.addWidget(self.checkBox_5)
        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout.addWidget(self.checkBox_6)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_2.addWidget(self.textEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        pgen.setCentralWidget(self.centralwidget)
        self.actionAbout_JET = QtWidgets.QAction(pgen)
        self.actionAbout_JET.setObjectName("actionAbout_JET")

        self.retranslateUi(pgen)
        QtCore.QMetaObject.connectSlotsByName(pgen)

    def back_to_jet(self):
        from __main__ import window1, window5_global
        window5_global_y = window5_global.geometry().y() - 30
        window1.move(window5_global.geometry().x(), window5_global_y)
        window1.show()
        window5_global.hide()
    def generate_password(self):
        characters_number = self.spinBox.value()
        stringLenght = 6
        def randomStringDigits(stringLength=6):
            stringLength2 = int(characters_number)
    
            var1IF = self.checkBox_4.isChecked()
            var2IF = self.checkBox_5.isChecked()
            var3IF = self.checkBox_6.isChecked()

            var1SET = ("")
            var2SET = ("")
            var3SET = ("")

            if var1IF == True:
                var1SET = string.ascii_letters
            if var2IF == True:
                var2SET = string.digits
            if var3IF == True:
                var3SET = string.punctuation

            if var1SET + var2SET + var3SET == "":
                return ''
            else:
                lettersAndDigits = var1SET + var2SET + var3SET
                return ''.join(random.choice(lettersAndDigits) for i in range(stringLength2))
        generated_password = randomStringDigits()
        if generated_password == '':
            self.textEdit.setText("Choose at least one option")
            QtTest.QTest.qWait(2000)
            self.textEdit.setText("")
        else:
            self.textEdit.setText(generated_password)
    def retranslateUi(self, pgen):
        _translate = QtCore.QCoreApplication.translate
        pgen.setWindowTitle(_translate("pgen", "JET"))
        self.pushButton_2.setText(_translate("pgen", "Back"))
        self.pushButton_2.clicked.connect(self.back_to_jet)
        self.label.setText(_translate("pgen", "Characters:"))
        self.checkBox_4.setText(_translate("pgen", "Letters"))
        self.checkBox_5.setText(_translate("pgen", "Numbers"))
        self.checkBox_6.setText(_translate("pgen", "Symbols"))
        self.pushButton.setText(_translate("pgen", "GENERATE"))
        self.pushButton.clicked.connect(self.generate_password)
        self.actionAbout_JET.setText(_translate("pgen", "About JET"))

