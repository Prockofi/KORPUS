from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from cripted_data import cripted

def create(password, pin):
    global screen, pincode, txt, txt1
    pincode = pin
    screen = Tk()  
    screen.title("КОРПUS 1.0")  
    screen.iconbitmap('icon.ico')
    screen.geometry('350x180')
    screen.resizable(width=False, height=False)
    screen.configure(background='white')

    lbl = Label(screen, text="Название для пароля:")  
    lbl.place(x=10, y=10)  
    txt = Entry(screen, width=24)  
    txt.place(x=150, y=10)

    lbl = Label(screen, text="Пароль:")  
    lbl.place(x=10, y=50)  
    txt1 = Entry(screen, width=24)  
    txt1.place(x=150, y=50)
    txt1.insert(0, f'{password}')

    btn1 = Button(screen, text='Сохранить пароль', command=save)
    btn1.place(x=120, y=120)

def save():
    global screen, incode, txt, txt1
    password = txt.get()
    name = txt1.get()
    data = cripted(password, name, pincode)
    try:
        file_name = filedialog.asksaveasfilename(filetypes=(("Scripts files", "*.kp"), ("All files", "*.*")))
        f = open(file_name, 'w', encoding='utf-8')
        f.write(data)
        f.close()
    except:
        pass
    screen.destroy()
