''' In this program we learnt how to create Drop down menus and it's sub menus, and how to execute
a function through these menus and sub menus(accordingly we can create sub-sub menus as well and so on)
'''

from tkinter import *
mehran=Tk()                    #here mehran is the root that we've been using on the previous examples

def infoz():
    print("This is a statement")

def yoda():
    y=2+3
    print(y)

mainmenu=Menu(mehran)    
mehran.configure(menu=mainmenu)

submenu1=Menu(mainmenu)
submenu2=Menu(mainmenu)

mainmenu.add_cascade(label="File",menu=submenu1)
mainmenu.add_cascade(label="Edit",menu=submenu2)

submenu1.add_command(label="random func", command=infoz)
submenu1.add_separator()
submenu1.add_command(label="random func 2", command=infoz)

submenu2.add_cascade(label="Another func", command=yoda)
mehran.mainloop()