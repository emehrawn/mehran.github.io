#convert the data in tuples and list into dictionary


daata=[("Mehran", 4) , ("Ali", 7) , ("Abbas", 1) , ("Hussain", 5) , ("Muhammad", 56)]
trick = {}
for value, value2 in daata:
    trick[value]=value2

print(trick)    