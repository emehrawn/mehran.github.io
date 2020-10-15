#in this program we create an array, specify it's length and insert elements in it
#We then print out it's elements in reversed form

ary=[]
length=int(input())

for i in range(0,length):

    r=input()     #this takes input as many times as length

    ary.append(r) #this adds the data to the array i,e (ary) as many times as length


print(ary[::-1]) #this changes the dxn of an array backwards (reversed -1)

print(min(ary))