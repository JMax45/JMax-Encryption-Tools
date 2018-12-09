from tkinter import *
from tkinter import messagebox, Menu, Frame
import tkinter as tk

def PopUp_CaesarCipher():
    window2 = Toplevel()
    window2.title('INFO | Caesar Cipher')        
    window2.geometry('700x150')
    window2.resizable(width=False, height=False)
    

    Label(window2, text='il Cifrario di Cesare è uno dei più antichi algoritmi crittografici,').pack()
    Label(window2, text='È un cifrario a sostituzione monoalfabetica in cui ogni lettera del testo in chiaro').pack()
    Label(window2, text='è sostituita nel testo cifrato dalla lettera che si trova un certo numero di posizioni dopo nel alfabeto').pack()

    window2.mainloop()
