#GUESS THE NUMBER
from random import *
name = input("What is your name = ")
print("  GUESS THE NUMBER   ")
print(f"Well {name} I've thought of a number between 1 and 100")
number_user = input("Guess your number ")
int(number_user)
number = (randint(1,100))
i = 8

while i<=8:
    if int(number_user) < 1 or int(number_user) > 100:
        print("invalid response,choose a number between 1 to 100")

    elif int(number_user) < number:
         print(f"Higher than that , try again you have {i} chances")
    elif int(number_user) > number:
         print(f"Lower than that , try again you have {i} chances")
    elif int(number_user) == number:
         print("WOW! that is the correct answer")
         break
    i = i - 1

    number_user = input("**Try another number** ")
    if i == 0:
        print("GAME OVER")
        break
