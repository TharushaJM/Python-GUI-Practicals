import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.geometry('300x400')
root.resizable(False,False)

def checkbox_result(): 
   output_string="Selected Languages:"+check1_variable.get()+" " + check2_variable.get()
   label_variable.set(output_string)
   
   
#Creting Variabels for Checkboxes
check1_variable=tk.StringVar()
check2_variable=tk.StringVar()
label_variable=tk.StringVar()



check1 = ttk.Checkbutton(root, text='Python' , variable=check1_variable, onvalue='Python')  #methanata onvalue
check1.pack()                                                             #dameema thulin apita pulwan 1 print wenwa
                                                                          #wenuwata Python kiyala print karanna 

check2 = ttk.Checkbutton(root, text='Java', variable=check2_variable, onvalue='Java')
check2.pack()

button=ttk.Button(root,text='Clcik Me',command=checkbox_result)
button.pack()

label=ttk.Label(root, textvariable=label_variable)
label.pack()

root.mainloop()

