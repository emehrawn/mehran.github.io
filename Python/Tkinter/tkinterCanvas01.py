#basics of canvas example
from tkinter import *
root = Tk()
can=Canvas(root, width=300, height=300)
can.pack()
can.create_rectangle(20,20,80,60)  #simple rectrangle created from canvas
can.create_line(0,150,300,150)     #simple line created from canvas
can.create_polygon(70,100,100,100,100,20) #polygon created from canvas
root.mainloop()