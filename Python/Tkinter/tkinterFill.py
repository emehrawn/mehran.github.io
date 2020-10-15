from tkinter import *
root = Tk()

button1=Button(None,text="Previous")
button2=Button(None,text="Ok", fg="blue")
button3=Button(None,text="Skip", fg="red")
button4=Button(None,text="Next")

button1.pack(side=LEFT, fill=Y) #this button fills on the left side vertically
button2.pack(fill=X)
button3.pack(side=BOTTOM,fill=X) #this button fills at bottom horizantally
button4.pack(side=RIGHT, fill=Y) #this button fills on the right side vertically 

root.mainloop()