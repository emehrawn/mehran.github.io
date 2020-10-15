#this is just another method for the actions through buttons program
#this meyhod is mainly used in gaming
from tkinter import *
root= Tk()

def greetings(event):
    print("What's up Mehran!")

button1=Button(root,text="Click here!")
button1.bind("<Button-1>", greetings)  
button1.pack()  

root.mainloop()
