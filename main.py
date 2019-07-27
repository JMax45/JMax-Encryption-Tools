import sys
from PyQt5 import QtWidgets, QtTest
from PyQt5.Qt import QApplication, QClipboard
from design import design
from methods.morse import *
from methods.caesar import *
from methods.vigenere import *

to_encrypt = ("")
to_decrypt = ("")
encryption_key = ("")

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def crypt(self):
        caesar_radio = self.radioButton_2.isChecked()
        morse_radio = self.radioButton.isChecked()
        vigenere_radio = self.radioButton_3.isChecked()
        if caesar_radio + morse_radio + vigenere_radio == 0:
            self.textEdit_2.setText("Choose an encryption metod")
            QtTest.QTest.qWait(1000)
            self.textEdit_2.setText("")
        empty_check = self.textEdit.toPlainText()
        def empty_check_true():
            self.textEdit_2.setText("The text field is empty")
            QtTest.QTest.qWait(1000)
            self.textEdit_2.setText("")
        if caesar_radio == True:
            if empty_check == "":
                empty_check_true()
            else:
                global to_encrypt
                to_encrypt = self.textEdit.toPlainText()
                caesar_crypt()
                from methods.caesar import encrypted_text
                self.textEdit_2.setText(encrypted_text)
        if morse_radio == True:
            if empty_check == "":
                empty_check_true()
            else:
                to_encrypt = self.textEdit.toPlainText()
                morse_crypt()
                from methods.morse import encrypted_text
                self.textEdit_2.setText(encrypted_text)
        if vigenere_radio == True:
            if empty_check == "":
                empty_check_true()
            else:
                to_encrypt = self.textEdit.toPlainText()
                vigenere_crypt()
                from methods.vigenere import encrypted_text,encryption_key
                self.textEdit_2.setText(encrypted_text)
                self.lineEdit.setText(encryption_key)
        self.textEdit.setText("")     
    def decrypt(self):
        caesar_radio = self.radioButton_2.isChecked()
        morse_radio = self.radioButton.isChecked()
        vigenere_radio = self.radioButton_3.isChecked()
        if caesar_radio + morse_radio + vigenere_radio == 0:
            self.textEdit_2.setText("Choose an encryption metod")
            QtTest.QTest.qWait(1000)
            self.textEdit_2.setText("")
        empty_check = self.textEdit.toPlainText()
        def empty_check_true():
            self.textEdit_2.setText("The text field is empty")
            QtTest.QTest.qWait(1000)
            self.textEdit_2.setText("")
        if caesar_radio == True:
            if empty_check == "":
                empty_check_true()
            else:
                global to_decrypt
                to_decrypt = self.textEdit.toPlainText()
                caesar_decrypt()
                from methods.caesar import decrypted_text
                self.textEdit_2.setText(decrypted_text)
        if morse_radio == True:
            if empty_check == "":
                empty_check_true()
            else:
                to_decrypt = self.textEdit.toPlainText()
                morse_decrypt()
                from methods.morse import decrypted_text
                self.textEdit_2.setText(decrypted_text)
        if vigenere_radio == True:
            if empty_check == "":
                empty_check_true()
            else:
                to_decrypt = self.textEdit.toPlainText()
                global encryption_key
                encryption_key = self.lineEdit.text()
                vigenere_decrypt()
                from methods.vigenere import decrypted_text
                self.textEdit_2.setText(str(decrypted_text))
        self.textEdit.setText("")
        self.lineEdit.setText("")
    def clear_encryption_key(self):
        self.lineEdit.setText("")
    def copy_encryption_key(self):
        copy_key = self.lineEdit.text()
        QApplication.clipboard().setText(copy_key)
        self.pushButton_3.setStyleSheet("background-color:#E75917;")
        self.pushButton_3.setText("COPIED")
        QtTest.QTest.qWait(1000)
        self.pushButton_3.setStyleSheet("background-color:None;")
        self.pushButton_3.setText("COPY")
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton.clicked.connect(self.crypt)
        self.pushButton_2.clicked.connect(self.decrypt)
        self.pushButton_3.clicked.connect(self.copy_encryption_key)
def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()    
