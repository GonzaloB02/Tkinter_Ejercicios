#Escribir una aplicación GUI (llamada Películas). Su función será: al 
#pulsar el botón Añadir, agregará en el listWidget el contenido de 
#lineEdit (Películas).

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Movies")

def close_window():
    root.destroy()

def add_movie():
    global value
    add = e.get()
    if add.strip() != "":
        box["values"] = value + [add]
        box.config(state="normal")
        box.delete(0, END)
        box.insert(0, add)
        box.set(add)
        e.delete(0, END)
        box.config(state="readonly")
    else:
        return

l = Label(root, text="Write a movie tittle", width=20, border=20)
l.grid(row=0, column=0)
l_2 = Label(root, text="Movies", width=20, border=20)
l_2.grid(row=0, column=1)

e = Entry(root, width=20)
e.grid(row=1, column=0)

b = Button(root, text="Add", width=15,command=add_movie)
b.grid(row=2, column=0)

box = ttk.Combobox(root, width=20, height=10, state="readonly")
value = list(box["values"])
box.set(value + ["Select a movie"])
box.grid(row=1, column=1)

close_button = Button(root, text="Close", bg="#00FF00", command=close_window, width=15)
close_button.grid(row=3, column=1, rowspan=2)

root.mainloop()