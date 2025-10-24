import tkinter as tk
from tkinter import ttk




#crete a window
root = tk.Tk()
root.title("Canvas")
root.geometry('400x400+100+100') #width,height
root.resizable(False,False)


canvas=tk.Canvas(root,bg='White')
canvas.pack()

##canvas.create_rectangle((10,10,100,200),fill='grey')
#canvas.create_oval((110,110,200,250),fill='green')

#canvas.create_polygon((255,30,260,155,340,100),fill='blue')


#canvas.create_line((0,0,300,255),fill='red',width=5)


brush_width=1
def draw(event):
    x =event.x
    y=event.y
    canvas.create_oval((x-brush_width,y-brush_width,x+brush_width,y+brush_width),fill='black')
    
    
def start_drawing(event):
    x=event.x
    y=event.y
    canvas.create_oval((x-brush_width,y-brush_width,x+brush_width,y+brush_width),fill='black')
    canvas.bind('<B1-Motion>', draw)
    
canvas.bind('<Button-1>', start_drawing)


#run the window
root.mainloop() 