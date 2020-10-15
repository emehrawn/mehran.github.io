#creating a pie chart and addind a Legend

import matplotlib.pyplot as plt
sizes=[45,7,3,25,10,5,5]
labs=["Apple","windows","linux","bada os","selfmade os","samsung os","unix"]
cols =['green', 'magenta' , 'yellow' , 'orange' , 'purple' , 'blue' , 'cyan']
plt.axis("equal")
plt.pie(sizes,colors=cols,labels=labs)
plt.legend(title="Legend",loc="lower left")
print(plt.show())

'''simple pie chart
import matplotlib.pyplot as plt
sizes=[45,7,3,25,10,5,5]
plt.pie(sizes)
print(plt.show)'''