#this is a guessing game based on the concept of random modules(randint) 
import random
comguess=random.randint(0,100) #computer chooses any random number between 0-100
while True:                                     #until the condition is true code written below will be repeated
    userguess=int(input("Enter your Number"))       
    if comguess>userguess:
        print("Guess higher")
    elif comguess<userguess:
        print("Guess lower")
    else:
        print("You got it. that's the right number")    
        break

