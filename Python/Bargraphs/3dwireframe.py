from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt 
import numpy as np 
fig = plt.figure()
chart=fig.add_subplot(1,1,1, projection="3d")

x,y,z=axes3d.get_test_data(0.02)
chart.plot_wireframe(x,y,z, rstride=2,cstride=2)      #less l&rstride more detailed is the graph

chart.set_xlabel("x-axis")
chart.set_ylabel("y-axis")
chart.set_zlabel("z-axis")

print(plt.show())