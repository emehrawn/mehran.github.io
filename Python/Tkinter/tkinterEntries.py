#Basic example of Entry in tkinter
from tkinter import *
root= Tk()
xlabel=Label(root,text="Enter your Name:",fg="Blue")
xlabel.grid(row=0,column=0)
ent=Entry(root)
ent.grid(row=0,column=1)
root.mainloop()