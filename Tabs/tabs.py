import tkinter as tk
from tkinter import ttk




#crete a window
root = tk.Tk()
root.title("Hello World")
root.geometry('400x400+100+100') #width,height
root.resizable(False,False)

def add_name():
    table.insert('', tk.END, values=(entry_value.get()))
    print(entry_value.get())



notebook= ttk.Notebook(root)

frame1=ttk.Frame(notebook,width=200,height=100,relief=tk.GROOVE)
frame1.pack_propagate(False)
frame1.pack()

entry_value=tk.StringVar()

frame2=ttk.Frame(notebook,width=200,height=100,relief=tk.GROOVE)
frame2.pack_propagate(False)
frame2.pack()

frame3=ttk.Frame(notebook,width=200,height=100,relief=tk.GROOVE)
frame3.pack_propagate(False)
frame3.pack()


notebook.add(frame1,text='Input')
notebook.add(frame2, text='Output')
notebook.add(frame3, text='Test')
notebook.pack()


entry=ttk.Entry(frame1)
entry.pack(pady=10)

button = ttk.Button(frame1, text='Submit', command=lambda:add_name())
button.pack()

table= ttk.Treeview(frame2, columns=('Names'),show='headings')
table.column('Names', width=198)
table.heading('Names', text='Names')
table.pack()

names = ['Kamal','Saman']
for idx, value in enumerate(names):
    table.insert('',index=idx,values=(names[idx]))
    


#run the window
root.mainloop() 