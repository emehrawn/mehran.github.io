#basic animations on tkinter
from tkinter import *
import time
root = Tk()
can=Canvas(root,width=500,height=500)
can.pack()

can.create_polygon(10,10,50,80,100,10)
can.create_text(10,200,text="What's up")

for i in range(0,100):

    can.move(1,4,2)     #here 1 is the identifier for the first object made and here it's polygon 
                        # 4 here represents how many pixels will it move on x-axis
                        # 2 here represents how many pixels will it move on y-axis

    can.move(2,5,0)     #representation as above

    root.update()
    time.sleep(0.3)

root.mainloop()    