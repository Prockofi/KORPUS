from tkinter import *
from tkinter import ttk

def func2(pincode):
    global screen, txtLen, bool1, bool2, bool3, bool4, bool5, bool6
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

    button1 = ttk.Checkbutton(screen, text="Использовать доп.символы", variable=bool1)
    button1.pack(padx=6, pady=6, anchor=NW)
  
    button2 = ttk.Checkbutton(screen, text="Большая кириллица", variable=bool2)
    button2.pack(padx=6, pady=6, anchor=NW)
 
    button3 = ttk.Checkbutton(screen, text="Маленькая кириллица", variable=bool3)
    button3.pack(padx=6, pady=6, anchor=NW)
 
    button4 = ttk.Checkbutton(screen, text="Большая латинница", variable=bool4)
    button4.pack(padx=6, pady=6, anchor=NW)

    button5 = ttk.Checkbutton(screen, text="Маленькая латинница", variable=bool5)
    button5.pack(padx=6, pady=6, anchor=NW)

    button6 = ttk.Checkbutton(screen, text="Использовать цифры", variable=bool6)
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

    btnCopy = ttk.Button(screen, text="Скопировать")
    btnCopy.place(x=600, y=355)

    btnCreate = ttk.Button(screen, text="Создать запись")
    btnCreate.place(x=490, y=355)

def menu1():
    global screen, txtLen, bool1, bool2, bool3, bool4, bool5, bool6
    print(bool1.get(), txtLen.get())
    screen.mainloop()
