from collections import OrderedDict
line = input()
n = int(input())
split = [line[i:i+n] for i in range(0, len(line), n)]
for i in split:
   print ("".join(OrderedDict.fromkeys(i)))