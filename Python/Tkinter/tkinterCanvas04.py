#Text and arcs in tkinter
from tkinter import *
root=Tk()
can=Canvas(root,width=400,height=400)
can.pack()

can.create_arc(10,10,200,80,style=ARC)                       #default (extent = 90)
can.create_arc(90,100,200,150,extent=180,style=ARC)


root.mainloop()