import os
from tkinter import *
from tkinter import ttk
from cripted_data import decripted

def func3(pincode):
    screen = Tk()  
    screen.title("КОРПUS 1.0")  
    screen.iconbitmap('icon.ico')
    screen.geometry('690x385')
    screen.resizable(width=False, height=False)
    screen.configure(background='white')

    scripts_file = []
    for file in os.listdir():
        if file[-3:] == '.kp':
            scripts_file.append(file)

    data = []
    for file in scripts_file:
        with open(file, 'r', encoding='utf-8') as f:
            for s in f:
                data.append(decripted(s, pincode))
    if len(data) == 0:
        lbl = Label(screen, width=92, text="Нет сохранённых паролей")  
        lbl.place(x=20, y=20)  
    for i in range(0, len(data)):
        name, pas = data[i]
        txtLen = Entry(screen, width=12)  
        txtLen.place(x=20, y=20+(30*i))
        txtLen.insert(0, name)

        txtLen = Entry(screen, width=90)  
        txtLen.place(x=120, y=20+(30*i))
        txtLen.insert(0, pas)