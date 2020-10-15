#plotting multiple plots in a graph
import matplotlib
import matplotlib.pyplot as plt 
x =[0,2,4,5,8]
y =[0,5,6,8,9]
x1=[2,3,7,5,8]
y2=[4,5,1,9,6]
x3=[0,6,7,8,8]
y3=[2,4,5,7,6]
xap = plt.figure()
kop = xap.patch
kop.set_facecolor("purple")
graph=xap.add_subplot(1,1,1)
graph.set_facecolor("Black")
graph.plot(x,y,"red", linewidth=3.0)
graph.plot(x1,y2,"yellow", linewidth=2.0)
graph.plot(x3,y3,"blue", linewidth=5.0)
print(plt.show())

