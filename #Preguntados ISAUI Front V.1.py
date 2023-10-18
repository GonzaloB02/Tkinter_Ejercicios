#Preguntados ISAUI

from tkinter import *

root = Tk()
root.title("Preguntados ISAUI")
window_1 = Frame()
window_1.pack()
window_height = 600
window_width = 900


def enable_start_button():
    if entry_name == "" or entry_address == "" or entry_instagram == "":
        #Warning window
        return

def start_button():
    window_1.destroy()
    frame = Frame()
    frame.pack()
    window_config(frame)
    label = Label(frame, text="Test")
    label.pack()

def destoy_windows(window):
    window.destroy()

def window_config(window): 
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    root.resizable(False, False) 
    root.overrideredirect(True)

    return window == root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

window_config(window_1)

label_1 = Label(window_1, text="Preguntados ISAUI", font=("Rockwell Condensed", 20), )
label_1.grid(row=0, sticky=N)

label_2 = Label(window_1, text="Nombre", justify="center")
label_2.grid(row=1)

entry_name = Entry(window_1, width=25, justify="center")
entry_name.grid(row=2)

label_3 = Label(window_1, text="Apellido", justify="center")
label_3.grid(row=3)

entry_address = Entry(window_1, width=25, justify="center")
entry_address.grid(row=4)

label_4 = Label(window_1, text="Instagram", justify="center")
label_4.grid(row=5)

entry_instagram = Entry(window_1, width=25 ,justify="center")
entry_instagram.grid(row=6)

start_button = Button(window_1, text="START", padx=20, pady=5, command=start_button and enable_start_button, justify="center")
start_button.grid(row=9)

exit_button = Button(window_1, text="EXIT", padx=20, pady=5, command=root.destroy, justify="right")
exit_button.grid(row=10, sticky=NE)


root.mainloop()