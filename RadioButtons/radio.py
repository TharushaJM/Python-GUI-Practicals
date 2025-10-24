import tkinter as tk
from tkinter import ttk

root=tk.Tk()


root.title('Radio Button')
root.geometry('300x400')
root.resizable(False,False)



#Creating Funtion
def select_radio():
    label.configure(text=radio_var.get())

#Creating only one variyable because radio button only get one value comprae with checkbox

radio_var=tk.StringVar()


radio1=ttk.Radiobutton(root,text='Python',value='python',variable=radio_var,command=select_radio)  #value use kereema thulin radio button seperate wenawa 
radio1.pack()                                                                   #nathnam radio button okkoma ekpa para wada karanne
                                                        

radio2=ttk.Radiobutton(root,text='Java',value='java',variable=radio_var,command=select_radio)
radio2.pack()

radio3=ttk.Radiobutton(root,text='C#',value='c#',variable=radio_var,command=select_radio)
radio3.pack()


label=ttk.Label(root)
label.pack()

root.mainloop()