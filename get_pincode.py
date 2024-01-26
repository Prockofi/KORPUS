from tkinter import *
from cripted import func2

def func1():
    global pincode
    pincode = entry.get()
    if pincode != '':
        pincode = func2(pincode)
        screen.destroy()
    else:
        screen.mainloop()
    return pincode

pincode = ''
screen = Tk()  
screen.title("Вход")  
screen.iconbitmap('icon.ico')
screen.geometry('400x300')
screen.resizable(width=False, height=False)

entry = Entry(screen, width=30)  
entry.place(x=100, y=100)
entry.focus()

btn = Button(text="Отправить", command=func1)
btn.pack(anchor=NW, padx=150, pady=130)