#Escribir una aplicación GUI (llamada Calculadora) que funcione como 
#una simple calculadora.

from tkinter import *

root = Tk()
root.title("Calculator")
root.resizable(0,0)

def close_window():
    root.destroy()

def clear_button():
    e.delete(0, END)
    e_2.delete(0, END)
    e_3.config(state="normal")
    e_3.delete(0, END)
    e_3.config(state="readonly")

def plus_button():
    num1 = e.get()
    num2 = e_2.get()
    try:
        result = float(num1) + float(num2)
        e_3.config(state="normal")
        e_3.delete(0, END)
        e_3.insert(0, result)
        e_3.config(state="readonly")
    except ValueError:
        e_3.config(state="normal")
        e_3.delete(0, END)
        e_3.insert(0, "Error")
        e_3.config(state="readonly")

def minus_button():
    num1 = e.get()
    num2 = e_2.get()
    try:
        result = float(num1) - float(num2)
        e_3.config(state="normal")
        e_3.delete(0, END)
        e_3.insert(0, result)
        e_3.config(state="readonly")
    except ValueError:
        e_3.config(state="normal")
        e_3.delete(0, END)
        e_3.insert(0, "Error")
        e_3.config(state="readonly")

def multiplication_button():
    #Por alguna razon (que no logre comprender) los valores salen correctamente pero salen con coma (.)
    # Ej: 5 * 5 = 0.25 / / /  2 * 8 = 0.16 / / / -3 * 9 = -0.27
    num1 = e.get()
    num2 = e_2.get()
    try:
        result = float(num1) * float(num2)
        e_3.config(state="normal")
        e_3.delete(0, END)
        e_3.insert(0, result)
        e_3.config(state="readonly")
    except ValueError:
        e_3.config(state="normal")
        e_3.delete(0, END)
        e_3.insert(0, "Error")
        e_3.config(state="readonly")

def division_button():
    num1 = e.get()
    num2 = e_2.get()
    try:
        result = float(num1) / float(num2)
        e_3.config(state="normal")
        e_3.delete(0, END)
        e_3.insert(0, result)
        e_3.config(state="readonly")
    except ValueError:
        e_3.config(state="normal")
        e_3.delete(0, END)
        e_3.insert(0, "Error")
        e_3.config(state="readonly")

def percentage_button():
    num1 = e.get()
    num2 = e_2.get()
    try:
        result = (float(num1) * float(num2)) / 100
        e_3.config(state="normal")
        e_3.delete(0, END)
        e_3.insert(0, result)
        e_3.config(state="readonly")
    except ValueError:
        e_3.config(state="normal")
        e_3.delete(0, END)
        e_3.insert(0, "Error")
        e_3.config(state="readonly")

l = Label(root, text="First number", width=15, border=10)
l.grid(row=0, column=0)
l_2 = Label(root, text="Second number", width=15, border=10)
l_2.grid(row=1, column=0)
l_3 = Label(root, text="Result", width=15, border=10)
l_3.grid(row=2, column=0)

e = Entry(root, width=15)
e.grid(row=0, column=1)
e_2 = Entry(root, width=15)
e_2.grid(row=1, column=1)
e_3 = Entry(root, width=15, state="readonly")
e_3.grid(row=2, column=1)

b = Button(root, width=15, text="+", command=plus_button).grid(row=3, column=0)
b = Button(root, width=15, text="-", command=minus_button).grid(row=3, column=1)
b = Button(root, width=15, text="*", command=percentage_button).grid(row=4, column=0)
b = Button(root, width=15, text="/", command=division_button).grid(row=4, column=1)
b = Button(root, width=15, text="%", command=percentage_button).grid(row=5, column=0)
b = Button(root, width=15, text="CLEAR", command=clear_button).grid(row=5, column=1)

close_button = Button(root, text="Close", bg="#00FF00", command=close_window, width=15)
close_button.grid(row=7, column=0, columnspan=2)

root.mainloop()