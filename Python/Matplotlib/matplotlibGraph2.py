import matplotlib
import matplotlib.pyplot as pp
x=[]
y=[]
data=open("D:\Mozuer\PythonPrac\yahoo.txt","r")
data2=data.read().split("\n")
for i in data2:
    val=i.split(",")
    x.append(int(val[0]))
    y.append(int(val[1]))
pp.plot(x,y)

print(pp.show())