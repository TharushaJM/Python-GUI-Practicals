import tkinter as tk
from tkinter import ttk




#crete a window
root = tk.Tk()
root.title("Hello World")
root.geometry('400x400+100+100') #width,height
root.resizable(False,False)


menu=tk.Menu(root)

#creating Sub Menu called file menu
file_menu=tk.Menu(menu)
file_menu.add_command(label='New')
file_menu.add_command(label='Open')
menu.add_cascade(label='File', menu=file_menu)


result_menu=tk.Menu(menu)
result_menu.add_command(label='Display')
result_menu.add_checkbutton(label='Light')
menu.add_cascade(label='Option',menu=result_menu)

root.configure(menu=menu)


#run the window
root.mainloop() 