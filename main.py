import sys
from PyQt5 import QtWidgets
from design import design

AB_Dict1 = [("A","C"),("B","D"),("C","E"),("D","F"),("E","G"),("F","H"),("G","I"),("H","J"),
             ("I","K"),("J","L"),("K","M"),("L","N"),("M","O"),("N","P"),("O","Q"),
             ("P","R"),("Q","S"),("R","T"),("S","U"),("T","V"),("U","W"),
             ("V","X"),("W","Y"),("X","Z"),("Y","A"),("Z","B"),

             ("a","c"),("b","d"),("c","e"),("d","f"),("e","g"),("f","h"),("g","i"),("h","j"),
             ("i","k"),("j","l"),("k","m"),("l","n"),("m","o"),("n","p"),("o","q"),
             ("p","r"),("q","s"),("r","t"),("s","u"),("t","v"),("u","w"),
             ("v","x"),("w","y"),("x","z"),("y","a"),("z","b")]

AB_Dict2 = [("C","A"),("D","B"),("E","C"),("F","D"),("H","F"),("I","G"),("J","H"),
             ("K","I"),("L","J"),("M","K"),("N","L"),("O","M"),("P","N"),("Q","O"),
             ("R","P"),("S","Q"),("T","R"),("U","S"),("V","T"),("W","U"),
             ("X","V"),("Y","W"),("Z","X"),("A","Y"),("B","Z"),("G","E"),

             ("c","a"),("d","b"),("e","c"),("f","d"),("h","f"),("i","g"),("j","h"),
             ("k","i"),("l","j"),("m","k"),("n","l"),("o","m"),("p","n"),("q","o"),
             ("r","p"),("s","q"),("t","r"),("u","s"),("v","t"),("w","u"),
             ("x","v"),("y","w"),("z","x"),("a","y"),("b","z"),("g","e")]

letter_to_morse1 = [("A",".- "),("B","-... "),("C","-.-. "),
                   ("D","-.. "),("E",". "),("F","..-. "),
                   ("G","--. "),("H",".... "),("I",".. "),
                   ("J",".--- "),("K","-.- "),("L",".-.. "),
                   ("M","-- "),("N","-. "),("O","--- "),
                   ("P",".--. "),("Q","--.- "),("R",".-. "),
                   ("S","... "),("T","- "),("U","..- "),
                   ("V","...- "),("W",".-- "),("X","-..- "),
                   ("Y","-.-- "),("Z","--.. "),(" ","/ ")]

letter_to_morse2 = [(".- ","A"),("-... ","B"),("-.-. ","C"),
                    ("-.. ","D"),(". ","E"),("..-. ","F"),
                    ("--. ","G"),(".... ","H"),(".. ","I"),
                    (".--- ","J"),("-.- ","K"),(".-.. ","L"),
                    ("-- ","M"),("-. ","N"),("--- ","O"),
                    (".--. ","P"),("--.- ","Q"),(".-. ","R"),
                    ("... ","S"),("- ","T"),("..- ","U"),
                    ("...- ","V"),(".-- ","W"),("-..- ","X"),
                    ("-.-- ","Y"),("--.. ","Z"),("/ "," ")]

vigenere_translate = [("T"," ")]
class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def crypt(self):
        caesar_radio = self.radioButton_2.isChecked()
        morse_radio = self.radioButton.isChecked()
        vigenere_radio = self.radioButton_3.isChecked()
        if caesar_radio == True:
            mytext = self.textEdit.toPlainText()
            crypted_text = mytext.translate(str.maketrans(dict(AB_Dict1)))
            self.textEdit_2.setText(crypted_text)
        if morse_radio == True:
            mytext = self.textEdit.toPlainText()
            decrypted_text = mytext.upper().translate(str.maketrans(dict(letter_to_morse1)))
            self.textEdit_2.setText(decrypted_text)
        if vigenere_radio == True:
            mytext = self.textEdit.toPlainText()
            m=str(mytext.upper())
            k="ZEVER"
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
            decrypted_text = mytext.translate(str.maketrans(dict(AB_Dict2)))
            self.textEdit_2.setText(decrypted_text)
        if morse_radio == True:
            mytext = self.textEdit.toPlainText()
            morse_to_letter3 = dict(letter_to_morse2)
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
