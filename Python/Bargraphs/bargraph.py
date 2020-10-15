import matplotlib.pyplot as kkk
import numpy as np
names = ["Boe","Joe","Don","Ali","Ram","Bob"]
xap = kkk.figure()
cap = xap.patch
xap.set_facecolor("grey")
graph=xap.add_subplot(1,1,1)
graph.set_facecolor("black")
kos = np.arange(6) + 1.0
graph.tick_params(axis="x",color="white")
graph.tick_params(axis="y",color="white")
kkk.title("Test Bar Graph", color="white")
kkk.xlabel("Hardwork Potential", color="white")
kkk.ylabel("Number of Students", color="white")
kkk.barh(kos,(4,9,12,19,14,6), color="red")
kkk.yticks(kos,names)        #takes the array names and asingns it to y axis elements(kos)
print(kkk.show())



"""to put code into perspective, simplest bar graph is:
import matplotlib.pyplot as plt
import numpy as np
pos = np.arange(6) + 1.0
plt.barh(pos,(4,9,12,19,14,6), color="red")
print(plt.show())"""


