#creating a colorful graph
import matplotlib.pyplot as pp
fig = pp.figure()
rect = fig.patch
rect.set_facecolor("xkcd:mint green")  #changes the color of the background/figure
x=[2,4,8,9,9]
y=[4,7,6,8,7]
graph1=fig.add_subplot(1,1,1)
graph1.set_facecolor('xkcd:salmon')    #changes the color of plot inside
graph1.plot(x,y,"white",linewidth=2.0)
graph1.tick_params(axis="x",color="red")   #gives color to parameters (x-axis)
graph1.tick_params(axis="y",color="red")   #gives color to parameters (y-axis)
graph1.spines["top"].set_color("white")    #this and following 3 lines give color to the boundary
graph1.spines["bottom"].set_color("white")
graph1.spines["left"].set_color("white")
graph1.spines["right"].set_color("white")
graph1.set_title("Test Graph",color="blue")    #this and following 2 lines set title and x,y labels along with there colors
graph1.set_xlabel("This is an x-axis",color="blue")
graph1.set_ylabel("This is a y-axis",color="blue")
print(pp.show())


"""" For code to put in perspective, for learning purpose only
>>> import matplotlib

>>> import matplotlib.pyplot as hit

>>> kit = hit.figure()

>>> pot = kit.patch

>>> pot.set_facecolor('green') 

>>> x = [3,12,20,24,29]

>>> y = [5,9,15,19,23]

>>> bit = kit.add_subplot(1,1,1,axisbg='red')"""