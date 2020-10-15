#this is a basic 3d graph
from mpl_toolkits.mplot3d import axes3d
import matplotlib
fig= plt.figure()
graph=fig.add_subplot(1,1,1, projection = '3d')
X,Y,Z= [1,2,3,4,5,6,7], [2,3,4,5,8,10,14], [3,8,9,7,10,8,11]
graph.plot(X,Y,Z)                            #graph.plot_wireframe(X,Y,Z) is the old command
print(matplotlib.pyplot.show())
