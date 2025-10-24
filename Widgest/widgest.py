import tkinter as tk
from tkinter import ttk
import r

root = tk.Tk()


root.title("Basic Widgest")
root.geometry('300x200')
root.resizable(False,False)

def button_click_fun(): 
    entry_field_value = entry.get()  #methanadi api walue eka gannawa entry field
    label.configure(text=entry_field_value)
    button.configure(state='disable') #button eka 1 parak click kalata passe disabel wenawa
    

entry = ttk.Entry(root)
entry.pack()

button=ttk.Button(root, text="Click Me", command=button_click_fun)  #use ttk button become modern
button.pack()

label= ttk.Label(root, )
label.pack


root.mainloop()

