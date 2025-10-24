import tkinter as tk
from tkinter import ttk




#crete a window
root = tk.Tk()
root.title("Hello World")
root.geometry('400x400+100+100') #width,height
root.resizable(False,False)



btn =ttk.Button(root, text='Click Me')
btn.pack()

root.bind('<Motion>' , lambda event:print(event))




#run the window
root.mainloop() 