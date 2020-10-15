import random
lista=["Stone","paper","scicssor"]
You=input("Stone, Paper or Scicssor\nEnter your Choice:")
Player2=random.choice(lista)
if You=="Stone" and Player2=="Scicssor":
    print("You won because you had "+str(You)+" and Player 2 had "+str(Player2))
elif You=="Paper" and Player2=="Stone":
    print("You won because you had "+str(You)+" and Player 2 had "+str(Player2))
elif You=="Scicssor" and Player2=="Paper":
    print("You won because you had "+str(You)+" and Player 2 had "+str(Player2))
else:
    print("Player 2 won because he had "+str(Player2)+" and You had "+str(You))        
