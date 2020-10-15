#if you wanna study 3d graphs, this is the best example on the pc
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d

matplotlib.rcParams["backend"] = "TkAgg"
fig = plt.figure()
chart=fig.add_subplot(1,1,1, projection="3d")

x =[1,2,3,4,5,6,7,8,9]             
y =[2,4,6,8,10,12,14,16,18]     #x-y graph, watch from above for perspective, since x and y are present on the base it'll create a ladder
z =[0,0,0,0,0,0,0,0,0]          #all are 0 such that graph sits on the base, z reps height

dx=np.ones(9)           #np.ones means [1,1,1,1,1,1,1,1,1] 9 times 1
dy=np.ones(9)                
dz=[1,2,3,4,5,6,7,8,9]       #graph ascends in this manner

chart.bar3d(x,y,z,dx,dy,dz,color="cyan")
chart.set_xlabel("x=axis")
chart.set_ylabel("y=axis")
chart.set_zlabel("z=axis")
print(plt.switch_backend("TkAgg"))
print(plt.show())




'''from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt 
import numpy as np 
fig = plt.figure()
chart=fig.add_subplot(1,1,1, projection="3d")
#x,y,z represent where the bar is located on the graph
x =[1,2,3,4,5,6,7,8,9]             
y =[0,0,0,0,0,0,0,0,0]        
z =[0,0,0,0,0,0,0,0,0]             #all are 0 such that graph sits on the base, z reps height

#dx,dy,dz give the dimensions to the bar itself
dx=np.ones(9)                   #np.ones means [1,1,1,1,1,1,1,1,1] 9 times 1, i,e square of unit lenght is the base with dz ascending
dy=np.ones(9)                   
dz=[1,2,3,4,5,6,7,8,9]          #graph ascends in this manner because you can invision it as a height

chart.bar3d(x,y,z,dx,dy,dz,color="cyan")
chart.set_xlabel("x=axis")
chart.set_ylabel("y=axis")
chart.set_zlabel("z=axis")
print(plt.show())
'''
