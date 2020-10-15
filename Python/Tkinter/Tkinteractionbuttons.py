#basic program for performing functions through buttons
from tkinter import *
root= Tk()

def greetings():
    print("What's up Mehran!")

button1=Button(root,text="Click here!",command=greetings)
button1.pack()    

root.mainloop()
