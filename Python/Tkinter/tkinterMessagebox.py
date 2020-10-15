'''
This program is a simple example of Message Box in Tkinter where you can use various types,
in this program we only came across (askquestion & showinfo)
'''
from tkinter import *
import tkinter.messagebox
root=Tk()

answer=tkinter.messagebox.askquestion("Question","Do you get offended if i use swear words?")
if answer=="no":
    tkinter.messagebox.showinfo("Information Title","You're a nice person")
else:
    tkinter.messagebox.showinfo("Information Title","You're just another typical shithead")  
root.mainloop()         