#Combining two graphs (graph1 and graph)
import matplotlib.pyplot as pp
fig = pp.figure()
rect = fig.patch
rect.set_facecolor("xkcd:mint green")  #changes the color of the background/figure
x=[2,4,8,7,6]
y=[4,7,6,8,12]
x3=[0,6,7,8,16]
y3=[2,4,5,9,11]
#graph1
graph1=fig.add_subplot(2,1,1)
graph1.set_facecolor('xkcd:salmon')    #changes the color of plot inside
graph1.plot(x,y,"white",linewidth=2.0)
graph1.tick_params(axis="x",color="red")   #gives color to parameters (x-axis)
graph1.tick_params(axis="y",color="red")   #gives color to parameters (y-axis)
graph1.set_title("Test Graph",color="blue")    #this and following 2 lines set title and x,y labels along with there colors
graph1.set_xlabel("This is an x-axis",color="blue")
graph1.set_ylabel("This is a y-axis",color="blue")
#graph2
graph=fig.add_subplot(2,1,2)
graph.set_facecolor("xkcd:salmon")
graph.plot(x3,y3,"blue", linewidth=5.0)
print(pp.show())



print(pp.show())









