#Escribir una aplicación GUI (llamada ContDecreciente) como la que se 
#ve en la figura. Cada vez que se haga clic en el botón "-",
#el valor del contador se reducira en 1.

from tkinter import *

root = Tk()
root.title("ContDecreciente")
root.resizable(0,0)


def close_window():
    root.destroy()

def plus_num():
    num = e.get()
    e.config(state="normal")
    e.delete(0, END)
    e.insert(0, int(num) - 1)
    e.config(state="readonly")

label_1 = Label(root, text="Contador decremental", fg="#9500FF")
label_1.grid(row=0, padx=15, pady=2)

e = Entry(root, width=10, borderwidth=5, font=("elephant", 12))
e.grid(row=1, padx=2, pady=2)
e.insert(0, 88)
e.config(state="readonly")

plus_button = Button(root, text="-", width=5, borderwidth=5, bg="#E42140", command=lambda : plus_num())
plus_button.grid(row=1, padx=2, pady=2, column=1)

close_button = Button(root, text="Close", bg="#00FF00", command=close_window)
close_button.grid(row=4, column=0)

root.mainloop()