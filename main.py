import sys
import json
from PyQt5 import QtWidgets, QtTest
from PyQt5.Qt import QApplication, QClipboard, QFileDialog
from design import design
from design.popup.about_jet import Ui_popup_about_jet
from design.popup.encryptTXT import Ui_encryptTXT
from design.popup.pgen import Ui_pgen
from methods.morse import *
from methods.caesar import *
from methods.vigenere import *
from methods.substitution import *

to_encrypt = ("")
to_decrypt = ("")
encryption_key = ("")
save_encryption_method = ("")

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def crypt(self):
        caesar_radio = self.radioButton_2.isChecked()
        morse_radio = self.radioButton.isChecked()
        vigenere_radio = self.radioButton_3.isChecked()
        substitution_radio = self.radioButton_4.isChecked()
        if caesar_radio + morse_radio + vigenere_radio + substitution_radio == 0:
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
        if substitution_radio == True:
            if empty_check == "":
                empty_check_true()
            else:
                to_encrypt = self.textEdit.toPlainText().upper()
                substitution_crypt()
                from methods.substitution import encrypted_text
                self.textEdit_2.setText(encrypted_text)       
        self.textEdit.setText("")     
    def decrypt(self):
        caesar_radio = self.radioButton_2.isChecked()
        morse_radio = self.radioButton.isChecked()
        vigenere_radio = self.radioButton_3.isChecked()
        substitution_radio = self.radioButton_4.isChecked()
        if caesar_radio + morse_radio + vigenere_radio + substitution_radio == 0:
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
        if substitution_radio == True:
            if empty_check == "":
                empty_check_true()
            else:
                to_decrypt = self.textEdit.toPlainText().upper()
                substitution_decrypt()
                from methods.substitution import decrypted_text
                self.textEdit_2.setText(decrypted_text)        
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
        self.pushButton_3.setStyleSheet("background-color:#5858FA;")
        self.pushButton_3.setText("COPY")
    def show_vigenere_keys(self):
        self.lineEdit.show()
        self.pushButton_3.show()
        self.label.show()
    def hide_vigenere_keys(self):
        self.lineEdit.hide()
        self.pushButton_3.hide()
        self.label.hide()
    def on_click_radioButton(self):
        caesar_radio = self.radioButton_2.isChecked()
        morse_radio = self.radioButton.isChecked()
        vigenere_radio = self.radioButton_3.isChecked()
        if self.radioButton.isChecked() == True:
            self.hide_vigenere_keys()
            global save_encryption_method
            save_encryption_method = "morse"
        if self.radioButton_2.isChecked() == True:
            self.hide_vigenere_keys()
            save_encryption_method = "caesar"
        if self.radioButton_3.isChecked() == True:
            save_encryption_method = "vigenere"
            self.show_vigenere_keys()
        if self.radioButton_4.isChecked() == True:
            save_encryption_method = "substitution"
            self.hide_vigenere_keys()
    def open_about_jet(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_popup_about_jet()
        self.ui.setupUi(self.window)
        self.window.show()
    def save_message2(self):
        file_name = self.lineEdit_2.text()
        file_name2 = ("saves/"+file_name+".txt")
        print(file_name2)
        with open(file_name2, 'w') as outfile:
            to_save = self.textEdit_2.toPlainText()
            encryption_key_save = self.lineEdit.text()
            data = {}
            data['encrypted_message'] = []
            if save_encryption_method == 'vigenere':
                data['encrypted_message'].append({
                    'message': to_save,
                    'encryption_method': save_encryption_method,
                    'encryption_key': encryption_key_save
                })
            else:    
                data['encrypted_message'].append({
                    'message': to_save,
                    'encryption_method': save_encryption_method
                })
            json.dump(data, outfile)
            self.check_save_message1 = "False"
            self.label_2.hide()
            self.lineEdit_2.hide()
            self.pushButton_4.hide()
            self.pushButton_5.setStyleSheet("")
            self.label_4.show()
            QtTest.QTest.qWait(3000)
            self.label_4.hide()
    def save_message(self):
        check_save_message2 = self.check_save_message1
        check_save_message3 = self.check_save_message4
        if check_save_message2 == "False":
            if check_save_message3 == "True":
                self.check_save_message4 = "False"
                self.pushButton_6.setStyleSheet("")
                self.toolButton.hide()
                self.lineEdit_3.hide()
                self.pushButton_7.hide()
            self.check_save_message1 = "True"
            self.label_2.show()
            self.lineEdit_2.show()
            
            self.pushButton_4.show()
            self.pushButton_5.setStyleSheet("background-color:#38A1CB")
        if check_save_message2 == "True":
            self.check_save_message1 = "False"
            self.label_2.hide()
            self.lineEdit_2.hide()
            self.pushButton_4.hide()
            self.pushButton_5.setStyleSheet("")
    def load_message(self):
        check_save_message3 = self.check_save_message4
        check_save_message2 = self.check_save_message1
        if check_save_message3 == "False":
            if check_save_message2 == "True":
                self.check_save_message1 = "False"
                self.label_2.hide()
                self.lineEdit_2.hide()
                self.pushButton_4.hide()
                self.pushButton_5.setStyleSheet("")
            self.check_save_message4 = "True"
            self.pushButton_6.setStyleSheet("background-color:#38A1CB")
            self.toolButton.show()
            self.lineEdit_3.show()
            self.pushButton_7.show()
        if check_save_message3 == "True":
            self.check_save_message4 = "False"
            self.pushButton_6.setStyleSheet("")
            self.toolButton.hide()
            self.lineEdit_3.hide()
            self.pushButton_7.hide()
    def choose_a_file_to_load(self):
        file_to_load1 = QFileDialog.getOpenFileName()[0]
        file_to_load2 = str(file_to_load1)
        self.lineEdit_3.setText(file_to_load2)
    def load_the_file(self):
        file_to_load = self.lineEdit_3.text()
        with open(file_to_load) as json_file:
            data = json.load(json_file)
        for p in data['encrypted_message']:
            print('Message: ' + p['message'])
            print('Encryption Method: ' + p['encryption_method'])
            print('')
            global to_decrypt
            to_decrypt = (p['message'])
            if p['encryption_method'] == 'caesar':
                caesar_decrypt()
                from methods.caesar import decrypted_text
            if p['encryption_method'] == 'morse':
                morse_decrypt()
                from methods.morse import decrypted_text
            if p['encryption_method'] == 'vigenere':
                global encryption_key
                encryption_key = p['encryption_key']
                vigenere_decrypt()
                from methods.vigenere import decrypted_text
            if p['encryption_method'] == 'substitution':
                substitution_decrypt()
                from methods.substitution import decrypted_text
            self.textEdit_2.setText(decrypted_text)
            self.check_save_message4 = "False"
            self.pushButton_6.setStyleSheet("")
            self.toolButton.hide()
            self.lineEdit_3.hide()
            self.pushButton_7.hide()
            self.label_3.show()
            QtTest.QTest.qWait(3000)
            self.label_3.hide()
    def open_encrypt_txt(self):
        window1.hide()
        height = self.geometry().y()
        height2 = (height-30)
        self.window4 = QtWidgets.QMainWindow()
        global window4_global
        window4_global = self.window4
        self.ui = Ui_encryptTXT()
        self.ui.setupUi(self.window4)
        self.window4.show()
        self.window4.move(self.geometry().x(), self.geometry().y())
    def open_pgen(self):
        window1.hide()
        height = self.geometry().y()
        height2 = (height-30)
        self.window5 = QtWidgets.QMainWindow()
        global window5_global
        window5_global = self.window5
        self.ui = Ui_pgen()
        self.ui.setupUi(self.window5)
        self.window5.show()
        self.window5.move(self.geometry().x(), self.geometry().y())
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton.clicked.connect(self.crypt)
        self.pushButton_2.clicked.connect(self.decrypt)
        self.pushButton_3.clicked.connect(self.copy_encryption_key)
        self.pushButton_4.clicked.connect(self.save_message2)
        self.pushButton_5.clicked.connect(self.save_message)
        self.pushButton_6.clicked.connect(self.load_message)
        self.radioButton.toggled.connect(self.on_click_radioButton)
        self.radioButton_2.toggled.connect(self.on_click_radioButton)
        self.radioButton_3.toggled.connect(self.on_click_radioButton)
        self.radioButton_4.toggled.connect(self.on_click_radioButton)
        self.toolButton.clicked.connect(self.choose_a_file_to_load)
        self.pushButton_7.clicked.connect(self.load_the_file)
        self.actionAbout_JET.triggered.connect(self.open_about_jet)
        self.actionEncryptTXT.triggered.connect(self.open_encrypt_txt)
        self.actionPGEN.triggered.connect(self.open_pgen)
        #hide and show stuff
        self.lineEdit.hide()
        self.lineEdit_2.hide()
        self.pushButton_3.hide()
        self.pushButton_7.hide()
        self.lineEdit_3.hide()
        self.label.hide()
        self.label_2.hide()
        self.label_3.hide()
        self.label_3.setStyleSheet("color:#0B610B;")
        self.label_4.hide()
        self.label_4.setStyleSheet("color:#0B610B;")
        self.toolButton.hide()
        self.pushButton_3.setStyleSheet("background-color:#5858FA;")
        self.pushButton_4.setStyleSheet("background-color:#5858FA;")
        self.pushButton_4.hide()
        self.lineEdit.setStyleSheet("background-color:#EFF2FB;")
        self.lineEdit_2.setStyleSheet("background-color:#EFF2FB;")
        self.textEdit.setStyleSheet("background-color:#EFF2FB;")
        self.textEdit_2.setStyleSheet("background-color:#EFF2FB;")
        self.check_save_message1 = ("False")
        self.check_save_message4 = ("False")
def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    global window1
    global window4
    global window5
    window4 = ("null")
    window1 = ExampleApp()  # Создаём объект класса ExampleApp
    window1.setStyleSheet("background-color:#CED8F6;")
    window1.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()    
