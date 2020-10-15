#simple login screen
from tkinter import *
root= Tk()
xlabel=Label(root,text="Username:")
ylabel=Label(root,text="Password")
xlabel.grid(row=0,column=0, sticky="E")   #sticky just makes it look nicer
ylabel.grid(row=0,column=2, sticky="E")
ent=Entry(root)
ent.grid(row=0,column=1)
ent2=Entry(root)
ent2.grid(row=0,column=3)
cbutton=Checkbutton(root,text="Remember my Password")
cbutton.grid(columnspan=2)
root.mainloop()