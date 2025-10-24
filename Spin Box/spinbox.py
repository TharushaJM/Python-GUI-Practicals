import tkinter as tk
from tkinter import ttk




#crete a window
root = tk.Tk()
root.title("Hello World")
root.geometry('400x400+100+100') #width,height
root.resizable(False,False)
#variyabale
spinbox_var=tk.StringVar()

spinbox=ttk.Spinbox(root,values=[1,2,3,4,5,6,7,8,9] , textvariable=spinbox_var)
spinbox.pack()

label=ttk.Label(root,textvariable=spinbox_var)
label.pack()




#run the window
root.mainloop() 