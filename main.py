import sys
from PyQt5 import QtWidgets, QtTest
from design import design
from metods.morse import *
from metods.caesar import *
from metods.vigenere import *

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
                from metods.caesar import encrypted_text
                self.textEdit_2.setText(encrypted_text)
        if morse_radio == True:
            if empty_check == "":
                empty_check_true()
            else:
                to_encrypt = self.textEdit.toPlainText()
                morse_crypt()
                from metods.morse import encrypted_text
                self.textEdit_2.setText(encrypted_text)
        if vigenere_radio == True:
            if empty_check == "":
                empty_check_true()
            else:
                to_encrypt = self.textEdit.toPlainText()
                vigenere_crypt()
                from metods.vigenere import encrypted_text,encryption_key
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
                from metods.caesar import decrypted_text
                self.textEdit_2.setText(decrypted_text)
        if morse_radio == True:
            if empty_check == "":
                empty_check_true()
            else:
                to_decrypt = self.textEdit.toPlainText()
                morse_decrypt()
                from metods.morse import decrypted_text
                self.textEdit_2.setText(decrypted_text)
        if vigenere_radio == True:
            if empty_check == "":
                empty_check_true()
            else:
                to_decrypt = self.textEdit.toPlainText()
                global encryption_key
                encryption_key = self.lineEdit.text()
                vigenere_decrypt()
                from metods.vigenere import decrypted_text
                self.textEdit_2.setText(str(decrypted_text))
        self.textEdit.setText("")
        self.lineEdit.setText("")
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton.clicked.connect(self.crypt)
        self.pushButton_2.clicked.connect(self.decrypt)

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()    
