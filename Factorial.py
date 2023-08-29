#Escribir una aplicación GUI (llamada Factorial) como la que se ve en 
#la figura. Cada ves que se haga clic en el botón "Siguiente", debe 
#calcular el factorial del primer lineEdit y mostrarlo en el segundo. Al 
#dar siguiente (n se incrementa en 1) n = 2 con su factorial 
#correspondiente.

from tkinter import *

count = 0

root = Tk()
root.title("Factorial")
root.resizable(0,0)

def close_window():
    root.destroy()

def fac_button():
    global count
    count += 1
    fac = 1
    for i in range(1, count + 1):
        fac *= i
    e.config(state="normal")
    e.delete(0, END)
    e.insert(0, count)
    e.config(state="readonly")
    e_2.config(state="normal")
    e_2.delete(0, END)
    e_2.insert(0, fac)
    e_2.config(state="readonly")
        

e = Entry(root, width=15, borderwidth=5, font=("Bernard MT Condensed", 12))
e.grid(row=1, column=1)
e.insert(0, 0)
e.config(state="readonly")
e_2 = Entry(root, width=15, borderwidth=5, font=("Bernard MT Condensed", 12))
e_2.insert(0, 0)
e_2.grid(row=1, column=4)
e_2.config(state="readonly")


l = Label(root, text="N°", padx= 5, pady=5)
l.grid(row=1, column=0)
l_2 = Label(root, text="Factorial(N°)")
l_2.grid(row=1, column=3)

b = Button(root, text="Next", width=5, command=fac_button)
b.grid(row=1, column=5)

close_button = Button(root, text="Close", bg="#00FF00", command=close_window)
close_button.grid(row=2, column=3)

root.mainloop()