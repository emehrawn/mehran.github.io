#In this program we alligned text in the form of a grid
from tkinter import *
root = Tk()

label1=Label(root,text="Alif")
label2=Label(root,text="Bay")
label3=Label(root,text="Pay")

label1.grid(row=0,column = 0)
label2.grid(row=0,column = 1)
label3.grid(row=1,column = 0)

root.mainloop()