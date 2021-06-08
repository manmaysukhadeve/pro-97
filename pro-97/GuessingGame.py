import random

chances = 0

number=random.randint(1,9)
Guess = int(input("choose a number between 1-9" ))
chances = int(input("guess"))

while chances > 5:
    print("take ur guess")
    chances = input()
    chances = int(chances)

    chances = chances+1

    if Guess == number:
        print("congratulations! you win")
        break
    

if not chances > 5:
    print("YOU LOSE!! THE NUMBER IS", number)

elif Guess < number:
    print("UR GUESS WAS TOO LOW !")

else:
    print("UR GUESS WAS TOO HIGH")


    



    

