import tkinter as tk
from tkinter import ttk




#crete a window
root = tk.Tk()
root.title("Frames")
root.geometry('400x400+100+100') #width,height
root.resizable(False,False)


frame1 =ttk.Frame(root, width=200,height=100,relief=tk.GROOVE)
frame1.pack_propagate(False) #reson to use False so adding Components the frame size dosent change
frame1.pack(side='bottom')  #align frame to left use side

#addingg component to frame
entry=ttk.Entry(frame1)  #master should be frame1 because we include this entry field in a frame
entry.pack(pady=10)

button=ttk.Button(frame1,text='Submit')
button.pack() 

frame2=ttk.Frame(root,width=200,height=500, relief=tk.GROOVE)
frame2.pack_propagate(False)
frame2.pack(side='right')

label1 = ttk.Label(frame2,text='Welcome')
label1.pack()

button2=ttk.Button(frame2, text='Click Me')
button2.pack()



#run the window
root.mainloop() 