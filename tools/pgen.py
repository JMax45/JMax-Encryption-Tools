from tkinter import *
from tkinter import Text
import tkinter as tk
import random
import string
import sys

window = Tk()
window.geometry("400x430")
stringLenght = 6

def randomStringDigits(stringLength=6):
    zevergay = e2.get()
    stringLength2 = int(zevergay)
    
    var1IF = var1.get()
    var2IF = var2.get()
    var3IF = var3.get()

    var1SET = ("")
    var2SET = ("")
    var3SET = ("")
    
    if var1IF == 1:
        var1SET = string.ascii_letters
    if var2IF == 1:
        var2SET = string.digits
    if var3IF == 1:
        var3SET = string.punctuation

    lettersAndDigits = var1SET + var2SET + var3SET
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength2))

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

R1 = Checkbutton(window, text = "Letters", variable = var1, onvalue = 1, offvalue = 0)
R1.pack( anchor = W )

R2 = Checkbutton(window, text = "Numbers", variable = var2, onvalue = 1, offvalue = 0)
R2.pack( anchor = W )

R3 = Checkbutton(window, text = "Symbols", variable = var3, onvalue = 1, offvalue = 0)
R3.pack( anchor = W )

def Generate():
    generated_password = randomStringDigits(8)
    print(generated_password)
    e.delete('1.0',END)
    e.insert(INSERT,generated_password)
def save_password():
    generated_password = e.get('1.0',END)

    class popupWindow(object):
        def __init__(self,master):
            top=self.top=Toplevel(master)
            screen_width = window.winfo_screenwidth()
            screen_height = window.winfo_screenheight()
            width = window.winfo_reqwidth()
            height = window.winfo_reqheight()

            x = screen_width / 2 - width / 2
            y = screen_height / 2 - height / 2
            top.geometry('%dx%d+%d+%d' % (width, height, x, y))
    
            self.l=Label(top,text="Password Name:")
            self.l.pack()
            self.e=Entry(top)
            self.e.pack()
            self.b=Button(top,text='Ok',command=self.cleanup)
            self.b.pack()
        def cleanup(self):
            self.value=self.e.get()
            self.top.destroy()
            print(self.value)
            saved_password = open("save.txt","a")
            pussy = (self.value + ": ")
            save_pass = (pussy + generated_password)
            saved_password.write("\n" + save_pass)
    popupWindow(window)

Button(window, text="Generate", command=Generate).pack()

e = Text(window, height=17, width=45)
e.pack()

e2 = Entry(window,width=10)
e2.place(x=100)
e2.insert(0,"6")

Button(window, text="Save", command=save_password).pack()
