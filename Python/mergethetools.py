'''strn=input("Ënter the string!")
fac=int(input())
if fac%2==0:
     
else:
    print("This is not a Factor")    
'''    
s = input()
k = int(input())

i = 0
map, to_print = {}, ""
while i < len(s):
    if i % k == 0 and i != 0:
        print(to_print)
        map, to_print = {}, ""
    if s[i] not in map.keys():
        map[s[i]] = 0
        to_print += s[i]
    i += 1
print(to_print)
    