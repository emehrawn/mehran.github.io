#tkinter canvas fill example and the shapes here will bw made through functions

from tkinter import *
root=Tk()
can=Canvas(root,width=400,height=400)
can.pack()

def CreateRec(x1,x2,x3,x4):
    can.create_rectangle(x1,x2,x3,x4, fill="purple")

CreateRec(20,40,190,160)
CreateRec(250,40,320,160)
CreateRec(360,40,390,160)
CreateRec(398,40,400,160)

root.mainloop()