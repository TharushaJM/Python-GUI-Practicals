import tkinter as tk
from tkinter import ttk




#crete a window
root = tk.Tk()
root.title("Hello World")
root.geometry('400x400+100+100') #width,height
root.resizable(False,False)

hello_label=ttk.Label(root,text='Hello',background='Yellow')
Welcome_label=ttk.Label(root,text='Welcome',background="Green")

#hello_label.pack(side='left',expand=True,fill='both')
#Welcome_label.pack()

root.columnconfigure(0 , weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)

root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)

hello_label.grid(row=1,column=1 , sticky='nsew')
Welcome_label.grid(row=0,column=2,sticky='nsew')




#run the window
root.mainloop() 