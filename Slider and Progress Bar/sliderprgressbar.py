import tkinter as tk
from tkinter import ttk




#crete a window
root = tk.Tk()
root.title("Hello World")
root.geometry('400x400+100+100') #width,height
root.resizable(False,False)

scale_value =tk.DoubleVar(value=50)



scale = ttk.Scale(root, command=lambda value:print(value), from_=0, to=100,length=400,variable=scale_value)
scale.pack()

progressbar = ttk.Progressbar(root,variable=scale_value)
progressbar.pack()





#run the window
root.mainloop() 