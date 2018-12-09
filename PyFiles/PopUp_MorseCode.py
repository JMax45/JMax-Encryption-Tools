from tkinter import *
from tkinter import messagebox, Menu, Frame
import tkinter as tk

def PopUp_MorseCode():
    window2 = Toplevel()
    window2.title('INFO | Morse Code')        
    window2.geometry('700x150')
    window2.resizable(width=False, height=False)

    Label(window2, text='Il codice Morse, detto anche alfabeto Morse,').pack()
    Label(window2, text=' è un sistema per trasmettere lettere, numeri e segni di punteggiatura per mezzo di un segnale in codice').pack()
    Label(window2, text='ad intermittenza').pack()

    window2.mainloop()
