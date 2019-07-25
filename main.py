import sys
from PyQt5 import QtWidgets
from design import design
from metods.caesar import *
from metods.morse import *
import string
import random

vigenere_translate = [("T","  ")]
class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def crypt(self):
        caesar_radio = self.radioButton_2.isChecked()
        morse_radio = self.radioButton.isChecked()
        vigenere_radio = self.radioButton_3.isChecked()
        if caesar_radio == True:
            mytext = self.textEdit.toPlainText()
            crypted_text = mytext.translate(str.maketrans(dict(caesar_dict1)))
            self.textEdit_2.setText(crypted_text)
        if morse_radio == True:
            mytext = self.textEdit.toPlainText()
            decrypted_text = mytext.upper().translate(str.maketrans(dict(morse_dict1)))
            self.textEdit_2.setText(decrypted_text)
        if vigenere_radio == True:
            mytext = self.textEdit.toPlainText()
            m=str(mytext.upper())
            def randomStringDigits(stringLength=6):
                var1SET = ("")
                var2SET = ("")
                var3SET = ("")
                var1SET = string.ascii_letters
                var2SET = string.digits
                var3SET = string.punctuation

                lettersAndDigits = var1SET + var2SET + var3SET
                return ''.join(random.choice(lettersAndDigits) for i in range(6))
            
            generated_password = randomStringDigits(8)
            k=str(generated_password)
            k*=len(m)//len(k)+1 
            c=""
            for i,j in enumerate(m):
                    gg=(ord(j)+ord(k[i])) 
                    c+=chr(gg%26+65) 
            self.textEdit_2.setText(str(c))
            self.lineEdit.setText(k)
        self.textEdit.setText("")     
    def decrypt(self):
        caesar_radio = self.radioButton_2.isChecked()
        morse_radio = self.radioButton.isChecked()
        vigenere_radio = self.radioButton_3.isChecked()
        if caesar_radio == True:
            mytext = self.textEdit.toPlainText()
            decrypted_text = mytext.translate(str.maketrans(dict(caesar_dict2)))
            self.textEdit_2.setText(decrypted_text)
        if morse_radio == True:
            mytext = self.textEdit.toPlainText()
            morse_to_letter3 = dict(morse_dict2)
            morse_to_decrypt = mytext.strip()
            decrypted_text = ("".join([morse_to_letter3.get(c + " ", "#error#")
                                    for c in morse_to_decrypt.split(" ")]))
            self.textEdit_2.setText(decrypted_text)
        if vigenere_radio == True:
            mytext = self.textEdit.toPlainText()
            mykey = self.lineEdit.text()
            c=str(mytext)
            k=str(mykey)
            d="" 
            for i,j in enumerate(c): 
                    gg=(ord(j)-ord(k[i])) 
                    d+=chr(gg%26+65)
            decrypted_text = d.upper().translate(str.maketrans(dict(vigenere_translate)))        
            self.textEdit_2.setText(str(d))
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
