#random rectrangle generator
from tkinter import *
import random
root=Tk()
can=Canvas(root,width=400,height=400)
can.pack()
def rect(num):                                   #num represents number of rectrangles to be printed
    for i in range(0,num):
        x1=random.randrange(400)
        y1=random.randrange(400)
        x2=x1+random.randrange(400)
        y2=y1+random.randrange(400)
        can.create_rectangle(x1,x2,y1,y2)

rect(910)        #here 720 is no. of rectrangles


can.mainloop()