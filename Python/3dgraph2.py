#this is modified and the scattered plot for the previous graph (3d graph.py file)
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt 
fig=plt.figure()
plt.style.use("dark_background")                   #this line is used for styling the graph, there are so many options available, Google em'
graph=fig.add_subplot(1,1,1, projection = '3d')
X,Y,Z= [1,2,3,4,5,6,7], [2,3,4,5,8,10,14], [3,8,9,7,10,8,11]
graph.plot(X,Y,Z)
graph.scatter(X,Y,Z,c='red',marker="o")
graph.set_xlabel('x-axis')
graph.set_ylabel('y-axis') 
graph.set_zlabel('z-axis')                         
print(plt.show())