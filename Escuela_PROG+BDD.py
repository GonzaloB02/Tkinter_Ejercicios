from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

conexion = mysql.connector.connect(host="127.0.0.1", user="root", password="GonzaloB02", database="ESCUELA")

def eliminar_alumno():
    return

def cancelar_cambios():
    nombre_entry.delete(0, tk.END)
    apellido_entry.delete(0, tk.END)
    dni_entry.delete(0, tk.END)
    carrera_combobox.set("")

    guardar_button.grid(row=5, column=2, padx=5, pady=5, sticky="e")
    modificar_button.grid(row=5, column=0, padx=5,pady=5, sticky="w")
    eliminar_button.grid(row=5, column=1, padx=5,pady=5, sticky="nsew")
    cancelar_button.grid_forget()

def comprobar_dni(dni): #Verificar y agregar puntos al dni (Posiblemente no termiinado)
    dni_limpiar = "".join(filter(str.isdigit,dni))

    if len(dni_limpiar) == 8:
        dni = f"{dni_limpiar[:2]}.{dni_limpiar[2:5]}.{dni_limpiar[5:]}"
        return dni
    else:
        return None

def mostrar_alerta(mensaje):
    messagebox.showwarning("Alerta", mensaje)

def cargar_carreras():
    cursor = conexion.cursor()
    cursor.execute("SELECT ID_CARRERA, NOMBRE FROM CARRERAS ORDER BY NOMBRE")
    carreras = cursor.fetchall()
    carrera_combobox["values"] = [row[1] for row in carreras]
    return carreras

def modificar_alumno():
    modificar_button.grid_forget()
    eliminar_button.grid_forget()
    cancelar_button.grid(row=5, column=0, padx=5,pady=5, sticky="w")
    seleccion = tree.selection()
    if len(seleccion) == 1:
        alumno_seleccion = tree.item(seleccion[0])
        values = alumno_seleccion.get("values")
        if len(values) >= 4:
            nombre = alumno_seleccion["values"][0]
            apellido = alumno_seleccion["values"][1]
            dni = alumno_seleccion["values"][2]
            carrera = alumno_seleccion["values"][3]

            nombre_entry.delete(0, tk.END)
            apellido_entry.delete(0, tk.END)
            dni_entry.delete(0, tk.END)

            nombre_entry.insert(0, nombre)
            apellido_entry.insert(0, apellido)
            dni_entry.insert(0, dni)
            carrera_combobox.set(carrera)
        
def guardar_alumno():        
    nombre = nombre_entry.get().lower()
    apellido = apellido_entry.get().lower()
    dni = dni_entry.get()
    carrera_nombre = carrera_combobox.get()
    estado_alumno = 1
    dni_validado = comprobar_dni(dni)

    if nombre is not None and apellido is not None and carrera_nombre is not None:
        mostrar_alerta("Debe llenar los espacios en blanco")
    elif dni_validado is None:
        mostrar_alerta("DNI no valido")
        return

    if nombre and apellido and dni and carrera_nombre:
        carreras = cargar_carreras()
        carrera_id = None
        for carrera in carreras:
            if carrera[1] == carrera_nombre:
                carrera_id = carrera[0]
                break
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO ALUMNOS (NOMBRE, APELLIDO, DNI, ID_CARRERA, ID_ESTADO_ALUMNO) VALUES (%s, %s, %s, %s, %s)", (nombre, apellido, dni, carrera_id, estado_alumno))
        conexion.commit()
        cargar_datos()
        nombre_entry.delete(0, tk.END)
        apellido_entry.delete(0, tk.END)
        dni_entry.delete(0, tk.END)
        carrera_combobox.set("")  

def cargar_datos():
    tree.delete(*tree.get_children())
    cursor = conexion.cursor()
    cursor.execute("SELECT ALUMNOS.NOMBRE, ALUMNOS.APELLIDO, ALUMNOS.DNI, CARRERAS.NOMBRE FROM ALUMNOS JOIN CARRERAS ON ALUMNOS.ID_CARRERA = CARRERAS.ID_CARRERA")
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)

root = Tk()
root.title("Consulta de alumnos")

formulario_frame = tk.Frame(root, bd=2, relief=tk.SOLID)
formulario_frame.pack(padx=10, pady=10)

titulo_label = tk.Label(formulario_frame,text="Formulario Inscripcion", font=("Helvetica", 14))
titulo_label.grid(row=0, column=0, columnspan=2, pady=10)

nombre_label = tk.Label(formulario_frame, text="Nombre:")
nombre_label.grid(row=1, column=0)
nombre_entry = tk.Entry(formulario_frame)
nombre_entry.grid(row=1, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")

apellido_label = tk.Label(formulario_frame, text="Apellido:")
apellido_label.grid(row=2, column=0)
apellido_entry = tk.Entry(formulario_frame)
apellido_entry.grid(row=2, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")

dni_label = tk.Label(formulario_frame, text="DNI:")
dni_label.grid(row=3, column=0)
dni_entry = tk.Entry(formulario_frame)
dni_entry.grid(row=3, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")

carrera_label = tk.Label(formulario_frame, text="Carrera:")
carrera_label.grid(row=4, column=0)
carrera_combobox = ttk.Combobox(formulario_frame, state="readonly")
carrera_combobox.grid(row=4, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")

carreras = cargar_carreras()

guardar_button = tk.Button(formulario_frame, text="Guardar",  command=guardar_alumno)
guardar_button.grid(row=5, column=2, padx=5, pady=5, sticky="e")

modificar_button = tk.Button(formulario_frame, text="Modificar",  command=modificar_alumno,)
modificar_button.grid(row=5, column=0, padx=5, pady=5, sticky="w")

cancelar_button = tk.Button(formulario_frame, text="Cancelar",  command=cancelar_cambios)
cancelar_button.grid_forget

eliminar_button = tk.Button(formulario_frame, text="Eliminar", command=eliminar_alumno)
eliminar_button.grid(row=5, column=1, padx=5,pady=5, sticky="nsew")

tree = ttk.Treeview(root, columns=("Nombre", "Apellido", "Carrera", "DNI"))
tree.heading("#1", text="Nombre")
tree.heading("#2", text="Apellido")
tree.heading("#4", text="Carrera")
tree.heading("#3", text="DNI")
tree.column("#0", width=0, stretch=tk.NO)
tree.pack(padx=10, pady=10)

cargar_button = tk.Button(root, text="Cargar Datos", command=cargar_datos)
cargar_button.pack(pady=5)

root.mainloop()

conexion.close()