from PyQt5 import QtWidgets, QtTest
from design.popup.encryptTXT import Ui_encryptTXT

def main():
    from __main__ import window1, x_encryptTXT, y_encryptTXT
    window3 = QtWidgets.QMainWindow()
    ui = Ui_encryptTXT()
    ui.setupUi(window3)
    window3.show()
def open_encryptTXT_page():
    main()
