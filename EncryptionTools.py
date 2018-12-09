import sys
from tkinter import *
from tkinter import messagebox, Menu, Frame
import tkinter as tk
import random
import os
import pyperclip
from PyFiles.PopUp_MorseCode import *
from PyFiles.PopUp_CaesarCipher import *


#Per un corretto funzionamento serve il modulo pyperclip
#pip install pyperclip

AB_Dict1 = [("A","C"),("B","D"),("C","E"),("D","F"),("E","G"),("F","H"),("G","I"),("H","J"),
             ("I","K"),("J","L"),("K","M"),("L","N"),("M","O"),("N","P"),("O","Q"),
             ("P","R"),("Q","S"),("R","T"),("S","U"),("T","V"),("U","W"),
             ("V","X"),("W","Y"),("X","Z"),("Y","A"),("Z","B")]

AB_Dict2 = [("C","A"),("D","B"),("E","C"),("F","D"),("H","F"),("I","G"),("J","H"),
             ("K","I"),("L","J"),("M","K"),("N","L"),("O","M"),("P","N"),("Q","O"),
             ("Q","O"),("R","P"),("S","Q"),("T","R"),("U","S"),("V","T"),("W","U"),
             ("X","V"),("Y","W"),("Z","X"),("A","Y"),("B","Z"),("G","E")]

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


def Copy_to_clipboard():
    mtext3 = text2.get("1.0",END)
    clear_copy = mtext3.strip()
    pyperclip.copy(clear_copy)   

def Crypt():
    mtext1 = text1.get("1.0",END)
    crypt_type = Type.get()

    if crypt_type == (0):
        window.label_text.config(text='È necessario scegliere un metodo di criptazione', fg='red')

    if crypt_type == (1):
        Crypted_Text_AB = mtext1.upper().translate(str.maketrans
                                                   (dict(AB_Dict1)))
        text2.delete('1.0',END)
        text2.insert(INSERT, Crypted_Text_AB)
        window.label_text.place_forget()

    if crypt_type == (2):
        Encrypted_Text_Morse = mtext1.upper().translate(str.maketrans
                                                     (dict(letter_to_morse1)))
        text2.delete('1.0', END)
        text2.insert(INSERT, Encrypted_Text_Morse)
        window.label_text.place_forget()
        

    
def Decrypt():
    mtext2 = text1.get("1.0",END)
    crypt_type = Type.get()

    if crypt_type == (0):
        window.label_text.config(text='È necessario scegliere un metodo di decriptazione', fg='red')
     
    if crypt_type == (1):
        Decrypted_Text_AB = mtext2.upper().translate(str.maketrans
                                                     (dict(AB_Dict2)))
        text2.delete('1.0', END)
        text2.insert(INSERT, Decrypted_Text_AB)
        window.label_text.place_forget()

    if crypt_type == (2):
        morse_to_letter = dict(letter_to_morse2)
        morse_to_decrypt = mtext2.strip()
        decrypted_morse = ("".join([morse_to_letter.get(c + " ", "#error#")
                                    for c in morse_to_decrypt.split(" ")]))

        if decrypted_morse == ("#error#"):
            window.label_text.config(text="""Nel testo inserito è presente un simbolo
non riconosciuto dalla libreria""", fg='red')
            window.label_text.place(x=490,y=120)
        else:
            text2.delete('1.0', END)
            text2.insert(INSERT, decrypted_morse)
            window.label_text.place_forget()

        
window = Tk()
text1 = StringVar()

Type = IntVar()
Type.set(0)

Caesar_Cipher = Radiobutton(window,text="Caesar cipher", variable = Type,
                value = 1)
Caesar_Cipher.place(y=100,x=200)
Morse_Cipher = Radiobutton(window,text="Morse Code", variable = Type,
                value = 2)
Morse_Cipher.place(y=100, x=90)

window.geometry('814x574')
window.title('JMax Encryption Tools')
window.resizable(width=False, height=False)

ment = StringVar()

text1 = Text(window, width=30, height=15.4)
text2 = Text(window, width=30, height=15.4)
window.label_text = tk.Label(window, text='')
text1.place(y=160,x=90)
text2.place(y=160,x=478)
window.label_text.place(x=474,y=135)

Button1 = Button(text="COPIA", command=Copy_to_clipboard)
Button1.place(y=423,x=578)
Button2 = Button(text="Cripta", command=Crypt)
Button2.place(y=200,x=385)
Button3 = Button(text="Decripta", command=Decrypt)
Button3.place(y=250,x=379)

m = Menu(window)                                       
fn2 = Menu(m, tearoff=0)
                        
m.add_cascade(label='Types', menu=fn2)
fn2.add_command(label='Caesar Cipher', command=PopUp_CaesarCipher)
fn2.add_command(label='Morse Code', command=PopUp_MorseCode)
                                          
window.config(menu=m)
