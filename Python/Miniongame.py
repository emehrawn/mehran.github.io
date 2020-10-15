X = int(input()) + 1;
Y = int(input()) + 1;
Z = int(input()) + 1;
N = int(input());
lst = [];
for x in range(0,X):
    for y in range(0,Y):
        for z in range(0, Z): 
            if (x + y + z) != N: 
                lst.append([x,y,z]);

print(lst);  