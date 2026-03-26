#P10 Random Number guess

import random

def numberguess():

    print("Welcome to the Game!")
    print("I selected a Number between 1 to 100.")
    print("Choosse any one number\nYou have only 3 attempts")

    num=random.randint(1,100)
    attempt=0

    while attempt<3:
        try:
            guess=int(input("Enter your guesses Number: "))
            attempt+=1

            if guess==num:
                print("Correct...You Won! ")
                break
                

            elif guess>num:
                print("Guess little Lower")
                print("Attempts left:", 3-attempt)
            else:
                print("Guess little Higher")
                print("Attempts left:", 3-attempt)
        except ValueError:
            print("Enter a Valid Number")
        
        if attempt==3:
            print("You user all your attempts!")
            break
while True:
    numberguess()
    choice=input("Want to Play Again (y/n): ").lower()
    if choice!='y':
        print("Thank your playing!")
        break
numberguess()


