import tkinter as tk
from tkinter import ttk




#crete a window
root = tk.Tk()
root.title("Hello World")
root.geometry('500x400+100+100') #width,height
root.resizable(False,False)

table=ttk.Treeview(root,columns=('name','age','email'), show='headings')
table.heading('name',text='Name')
table.heading('age',text='Age')
table.heading('email',text='E-Mail')
table.column('age',width=100)
table.column('name',width=200)
table.column('email',width=200)
table.pack()

name=['Kamal','Saman','Pawan','Gayan']
age=[30,53,32,54]

def selected_item(event):
      label.configure(text=table.item(table.selection()))   

for idx, value in enumerate(name):
    table.insert('',idx,values=(name[idx],age[idx],f'{name[idx]}@gmail.com'))
    
    
table.bind('<<TreeviewSelect>>' , lambda event:selected_item(event))   

label=tk.Label(root,textvariable=selected_item)
label.pack()

#run the window
root.mainloop() 