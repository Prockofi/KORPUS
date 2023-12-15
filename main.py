from tkinter import *
from tkinter import ttk
from get_pincode import func1

pincode = func1()
if pincode == '':
    exit()

#Настройки экрана
screen = Tk()  
screen.title("КОРПUS 1.0")  
screen.iconbitmap('icon.ico')
screen.geometry('300x450')
screen.resizable(width=False, height=False)
screen.configure(background='white')

#Размещение логотипа
canvas = Canvas(screen, bg = 'white', height = 200, width = 200, highlightthickness=0)
canvas.pack()
canvas.place(x=50, y=10)

logo = PhotoImage(file='img.png')
logoimg = canvas.create_image(0,0, anchor = NW, image = logo)

#Размещение кнопок
ttk.Style().configure("TButton",  font="helvetica 13", foreground="#144E8F", padding=8, background="#144E8F") 

btn1 = ttk.Button(screen, text="Сгенерировать пароль")
btn1.place(x=48, y=190)

btn2 = ttk.Button(screen, text="Посмотреть пароли")
btn2.place(x=60, y=250)

btn3 = ttk.Button(screen, text="Удалить все данные")
btn3.place(x=55, y=310)

btn4 = ttk.Button(screen, text="Закрыть приложение")
btn4.place(x=55, y=370)



screen.mainloop()