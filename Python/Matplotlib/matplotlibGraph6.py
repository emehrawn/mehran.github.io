#plotting 3 graphs, here we actually create 4 sub-slots i.e (2,2,x) where x is the graph on which the current code is being written
#we treat 2 graphs as 1 then the 3rd graph as 2nd, such that 3 graph takes as much space as ist 2 graphs, we can change it as per our convienence
import matplotlib.pyplot as pp
fig = pp.figure()
rect = fig.patch
rect.set_facecolor("Red")  #changes the color of the background/figure
x=[2,4,8,7,6]
y=[4,7,6,8,12]
x2=[2,14,5,7,9]
y2=[0,9,6,4,15]
x3=[0,3,4,11,16]
y3=[2,4,5,9,11]
#graph1
graph1=fig.add_subplot(2,2,1)    #here (2,2,1) means create a 2X2 graph, and write code on graph 1, (2,2) creates 4 sub-plot slots in a figure
graph1.set_facecolor('Black')    #changes the color of plot inside
graph1.plot(x,y,"white",linewidth=2.0)
graph1.tick_params(axis="x",color="red")   #gives color to parameters (x-axis)
graph1.tick_params(axis="y",color="red")   #gives color to parameters (y-axis)
graph1.set_title("Test Graph",color="blue")    #this and following 2 lines set title and x,y labels along with there colors
graph1.set_xlabel("This is an x-axis",color="blue")
graph1.set_ylabel("This is a y-axis",color="blue")
#graph2
graph=fig.add_subplot(2,2,2)    #here (2,2,2) means create a 2X2 graph, and write code on graph 2
graph.set_facecolor("black")
graph.plot(x2,y2,"blue", linewidth=5.0)
#graph3
graph=fig.add_subplot(2,1,2)    #here (2,1,2) means create 2x1 graph and write code on 2 graph(2nd graph place for (2,1))
graph.set_facecolor("black")
graph.plot(x3,y3,"yellow", linewidth=5.0)

print(pp.show())