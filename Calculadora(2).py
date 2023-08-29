#Escribir una aplicación GUI (llamada Calculadora 2) como la que se ve 
#en la figura y que funcione como una calculadora.

from tkinter import *

root = Tk()
root.title("Calculator_2")

def close_window():
    root.destroy()

def calculate():
    e_3.config(state="normal")
    num_1 = float(e.get())
    num_2 = float(e_2.get())
    op = operational.get()
    try:
        result = None
        if op == "+":
            result = num_1 + num_2
        elif op == "-":
            result = num_1 - num_2
        elif op == "*":
            result = num_1 * num_2
        elif op == "/":
            if float(num_2) != 0:
                result = num_1 / num_2
            else:
                result = "Cannot divide by zero"
        e_3.delete(0, END)
        e_3.insert(0, result)
    except (SyntaxError, ZeroDivisionError, TypeError, ValueError):
        e_3.delete(0, END)
        e_3.insert(0, "Error")
    e_3.config(state="readonly")        

l = Label(root, text="First value", pady=15)
l.grid(row=1, column=0)
l_2 = Label(root, text="Second value", pady=15)
l_2.grid(row=2, column=0)
l_3 = Label(root, text="Result", pady=15)
l_3.grid(row=3, column=0)
l_4 = Label(root, text="Operations", pady=15)
l_4.grid(row=0, column=2)

e = Entry(root, width=20)
e.grid(row=1, column=1)
e_2 = Entry(root, width=20)
e_2.grid(row=2, column=1)
e_3 = Entry(root, width=20, state="readonly")
e_3.grid(row=3, column=1)

options = {"Addition" : "+",
           "Subtraction" : "-",
           "Multiplication" : "*",
           "Division" : "/"}

operational = StringVar()
operational.set("+")

for index, (option, value) in enumerate(options.items()):
    Radiobutton(root, text=option, value=value, variable=operational).grid(row=index+1, column=2, padx=20, pady=2, sticky=W)

b = Button(root, text="Calculate", width=15, command=calculate)
b.grid(row=4, column=1, padx=15)

close_button = Button(root, text="Close", bg="#00FF00", command=close_window, width=15)
close_button.grid(row=4, column=0, padx=5)

root.mainloop()