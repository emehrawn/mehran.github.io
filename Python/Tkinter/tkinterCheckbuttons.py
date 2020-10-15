from tkinter import *
root= Tk()
xlabel=Label(root,text="Enter your Name:")
xlabel.grid(row=0,column=0)
ent=Entry(root)
ent.grid(row=0,column=1)
cbutton=Checkbutton(root,text="Remember my Name")
cbutton.grid(columnspan=2)
root.mainloop()