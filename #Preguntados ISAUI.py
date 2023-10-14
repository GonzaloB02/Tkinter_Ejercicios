#Preguntados ISAUI

from tkinter import *

root = Tk()
window_1 = Frame(root)
window_1.pack()
window_height = 600
window_width = 900

def game_questions():
    return

def start_button():
    new_window = Toplevel()
    frame = Frame(new_window, height=window_height, width=window_width)
    frame.pack(window_config(new_window))
    game_questions()

def destoy_windows(window):
    window.destroy()

def window_config(window_1): 
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    root.resizable(False, False) 
    #root.overrideredirect(True)

    return window_1 == root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

window_config(window_1)

label_1 = Label(window_1, text="Preguntados ISAUI", font=("Rockwell Condensed", 20), )
label_1.grid(row=0, sticky=N)

exit_button = Button(window_1, text="EXIT", padx=20, pady=5, command=destoy_windows(window_1))
exit_button.grid(row=10, column=10, sticky=SW)

start_button = Button(window_1, text="START", padx=20, pady=5, command=start_button and destoy_windows(window_1), justify="center")
start_button.grid(row=5)



root.mainloop()