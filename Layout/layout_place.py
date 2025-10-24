import tkinter as tk
from tkinter import ttk




#crete a window
root = tk.Tk()
root.title("Hello World")
root.geometry('500x400+100+100') #width,height
root.resizable(False,False)

hello_label=ttk.Label(root,text='Hello',background='Yellow')
Welcome_label=ttk.Label(root,text='Welcome',background="Green")

hello_label.place(x=100,y=100)
Welcome_label.place(x=300,y=100,width=100,height=100)






#run the window
root.mainloop() 