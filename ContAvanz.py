#Escribir una aplicación GUI (llamada Contador) como la que se ve en 
#la figura. Con 3 botones (Count Up - Para incrementar, Count Down -
#Para restar y Reset - Para comenzar de cero).

from tkinter import *

root = Tk()
root.title("Contador")
root.resizable(0,0)

def close_window():
    root.destroy()

def count_up():
    num = int(e.get())
    num += 1
    e.config(state="normal")
    e.delete(0, END)
    e.insert(0, num)
    e.config(state="readonly")

def count_down():
    num = int(e.get())
    num -= 1
    e.config(state="normal")
    e.delete(0, END)
    e.insert(0, num)
    e.config(state="readonly")    

def reset():
    e.config(state="normal")
    e.delete(0, END)
    e.insert(0, 0)
    e.config(state="readonly")           

l = Label(root, text="Contador", border=5)
l.grid(row=0, column=0)

e = Entry(root, width=15, font="ArialBlack")
e.grid(row=0, column=1, columnspan=3)
e.insert(0, 0)
e.config(state="readonly")

b = Button(root, text="CountUp", width=5, padx=15, command=count_up)
b.grid(row=0, column=4)
b_2 = Button(root, text="CountDown", width=5, padx=15, command=count_down)
b_2.grid(row=0, column=5)
b_3 = Button(root, text="Reset", width=5, padx=15, command=reset)
b_3.grid(row=0, column=6)


close_button = Button(root, text="Close", bg="#00FF00", command=close_window, width=10)
close_button.grid(row=2, column=3)

root.mainloop()