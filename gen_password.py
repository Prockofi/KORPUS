from random import *
from tkinter import *
from tkinter import ttk
from create_password import create

def func2(pin):
    global screen, text, txtLen, bool1, bool2, bool3, bool4, bool5, bool6, pincode
    pincode = pin
    bool1 = IntVar()
    bool2 = IntVar()    
    bool3 = IntVar()
    bool4 = IntVar()
    bool5 = IntVar()
    bool6 = IntVar()

    screen = Tk()  
    screen.title("КОРПUS 1.0")  
    screen.iconbitmap('icon.ico')
    screen.geometry('690x385')
    screen.resizable(width=False, height=False)

    button1 = ttk.Checkbutton(screen, text="Использовать доп.символы", variable=bool1, command=in1)
    button1.pack(padx=6, pady=6, anchor=NW)
  
    button2 = ttk.Checkbutton(screen, text="Большая кириллица", variable=bool2, command=in2)
    button2.pack(padx=6, pady=6, anchor=NW)
 
    button3 = ttk.Checkbutton(screen, text="Маленькая кириллица", variable=bool3, command=in3)
    button3.pack(padx=6, pady=6, anchor=NW)
 
    button4 = ttk.Checkbutton(screen, text="Большая латинница", variable=bool4, command=in4)
    button4.pack(padx=6, pady=6, anchor=NW)

    button5 = ttk.Checkbutton(screen, text="Маленькая латинница", variable=bool5, command=in5)
    button5.pack(padx=6, pady=6, anchor=NW)

    button6 = ttk.Checkbutton(screen, text="Использовать цифры", variable=bool6, command=in6)
    button6.pack(padx=6, pady=6, anchor=NW)

    lblLen = ttk.Label(screen, text="Длина:")  
    lblLen.place(x=10, y=205)  
    txtLen = ttk.Entry(screen, width=10)  
    txtLen.place(x=60, y=205)
    txtLen.insert(0, 16)

    btnGen = ttk.Button(screen, text="Сгенерировать пароль", command=menu1)
    btnGen.place(x=30, y=245)

    text = Text(screen, width=60, height=21, bg="white", fg='black', wrap=WORD)
    text.pack()
    text.place(x=200, y=10)

    btnCreate = ttk.Button(screen, text="Создать запись", command=menu2)
    btnCreate.place(x=490, y=355)

    btnCopy = ttk.Button(screen, text="Скопировать", command=copy)
    btnCopy.place(x=600, y=355)

def menu1():
    global screen, text, txtLen, bool1, bool2, bool3, bool4, bool5, bool6, password
    try:
        lenght = int(txtLen.get())
        if lenght > 300:
            lenght = 256
    except:
        lenght = 16
    alfabet = ''
    if bool1.get() == 1:
        alfabet += '!#$-+=&?/()'
    if bool2.get() == 1:
        alfabet += 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    if bool3.get() == 1:
        alfabet += 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    if bool4.get() == 1:
        alfabet += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if bool5.get() == 1:
        alfabet += 'abcdefghijklmnopqrstuvwxyz'
    if bool6.get() == 1:
        alfabet += '0123456789'
    password = ''
    try:
        for i in range(lenght):
            password += alfabet[randint(0, len(alfabet)-1)]
    except:
        password = 'Выберите не менее одного пункта'
    text.delete('0.0', END)
    text.insert('0.0', f'{password}')

def menu2():
    global password, pincode
    create(password, pincode)

def in1():
    global bool1
    if bool1.get() == 0:
        bool1.set(1)
    else:
        bool1.set(0)

def in2():
    global bool2
    if bool2.get() == 0:
        bool2.set(1)
    else:
        bool2.set(0)

def in3():
    global bool3
    if bool3.get() == 0:
        bool3.set(1)
    else:
        bool3.set(0)

def in4():
    global bool4
    if bool4.get() == 0:
        bool4.set(1)
    else:
        bool4.set(0)

def in5():
    global bool5
    if bool5.get() == 0:
        bool5.set(1)
    else:
        bool5.set(0)

def in6():
    global bool6
    if bool6.get() == 0:
        bool6.set(1)
    else:
        bool6.set(0)

def copy():
    text.clipboard_clear()
    text.clipboard_append(text.get(1.0, END))