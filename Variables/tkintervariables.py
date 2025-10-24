import tkinter as tk
from tkinter import ttk



root=tk.Tk()
root.title('Variable')
root.geometry('300x200')

variable_value=tk.StringVar() #DoubleVar,IntVar


label = ttk.Label(root ,textvariable=variable_value)
label.pack()

entry=ttk.Entry(root,textvariable=variable_value)
entry.pack()

#creating Button
button=ttk.Button(root,text="Click Me",command=lambda:print(entry.get()))
button.pack()


root.mainloop()