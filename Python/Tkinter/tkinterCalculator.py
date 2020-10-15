from tkinter import *
root=Tk()
label1=Label(root,text="This is a simple manual Calculaor", fg="Purple")
label1.pack()

def dataYo(event):
    data=soko.get()
    ans.configure(text="Answer:"+str(eval(data)))
    
soko=Entry(root)   
soko.bind("<Return>",dataYo)
soko.pack()
ans=Label(root)
ans.pack()
root.mainloop()