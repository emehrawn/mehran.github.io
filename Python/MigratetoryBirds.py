'''import statistics
import heapq
list=[]
naka=int(input("Enter the number of birds"))
for i in range(0,naka):
    birdid=int(input("Enter the type of Bird"))
    list.append(birdid)
print("Birds are of type:  ",list)   
print(statistics.mode(list))  #used to find most repeated element
'''

import sys
from collections import Counter

n = int(input().strip())
types = list(map(int, input().strip().split(' ')))
freq = Counter(types)
print(max(freq, key=freq.get))
# your code goes here
