#Text
from tkinter import *
root=Tk()
can=Canvas(root,width=400,height=400)
can.pack()

can.create_text(200,200,text="Hello World", font=("Times", 30))



root.mainloop()