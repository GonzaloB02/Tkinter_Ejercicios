#Escribir una aplicación GUI (llamada Generador de números). Su 
#función será: al pulsar el botón Generar, generará un número 
#aleatorio en el rango de los dos Spin Box.

from tkinter import *
import random 

generator = 0

root = Tk()
root.title("NumbersGenerator")

def close_window():
    root.destroy()

def num_gen():
    global generator
    num_1 = int(e.get())
    num_2 = int(e_2.get())
    if num_1 < num_2:
        generator = random.randint(num_1, num_2)
    else:
        generator = random.randint(num_2, num_1)
    e_3.config(state="normal")
    e_3.delete(0, END)
    e_3.insert(0, generator)
    e_3.config(state="readonly")


l = Label(root, text="First number", width=20, border=20)
l.grid(row=0, column=0)
l_2 = Label(root, text="Second number", width=20, border=20)
l_2.grid(row=1, column=0)
l_3 = Label(root, text="Generated number", width=20, border=20)
l_3.grid(row=2, column=0)


e = Spinbox(root, width=20, from_=-10, to=10, state="readonly")
e.grid(row=0, column=1)
e_2 = Spinbox(root, width=20,from_=-10, to=10, state="readonly")
e_2.grid(row=1, column=1)

e_3 = Entry(root, width=20, state="readonly")
e_3.grid(row=2, column=1)

b = Button(root, text="Generate", width=10, command=num_gen)
b.grid(row=3, column=0)

close_button = Button(root, text="Close", bg="#00FF00", command=close_window, width=15)
close_button.grid(row=3, column=1)

root.mainloop()