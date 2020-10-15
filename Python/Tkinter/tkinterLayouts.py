#emplimentation of layouts, like top frame and bottomframe that assingn the position of buttons

from tkinter import *
root = Tk()
topframe=Frame(root)
topframe.pack()
bottomframe=Frame(root)
bottomframe.pack(side=BOTTOM)
button1=Button(topframe,text="Ok")
button2=Button(bottomframe,text="Next")
button3=Button(bottomframe,text="Previous")
button4=Button(topframe,text="Skip")                                       
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)  
root.mainloop()