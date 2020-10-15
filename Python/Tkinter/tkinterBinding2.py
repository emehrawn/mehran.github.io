#the program that tells you which button you clicked on the mouse including left and right keys on keyboard
from tkinter import *
root= Tk()

def leftClick(event):
    print("Left")

def rightClick(event):
    print("Right")

def scroll(event):
    print("Scroll")

def left(event):
    print("Left key pressed")

def right(event):
    print("Right")

root.geometry("500x500")

root.bind("<Button-1>",leftClick)
root.bind("<Button-2>",rightClick)
root.bind("<Button-3>",scroll)
root.bind("<Left>",left)
root.bind("<Right>",right)
root.mainloop()