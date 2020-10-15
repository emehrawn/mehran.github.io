import matplotlib.pyplot as pp
fig = pp.figure()
rect = fig.patch
rect.set_facecolor("Purple")
x=[2,3,8,9,9]
y=[3,4,7,6,7]
graph1=fig.add_subplot(1,1,1)
graph1.plot(x,y,"Red",linewidth=2.0)
print(pp.show())
