#This game plays rock, paper, scissors with a computer
#All user input is in integers, so only type numbers in the console
#Game will keep your score and the computer's score

import random

user_score = 0
comp_score = 0

choice_list = ["rock", "paper", "scissors"]


i = 1
while i == 1:
    x = random.randint(0,2)

    num = int(input("Choose from the following options and enter a number: 0: rock, 1: paper, or 2: scissors? "))

    print("Computer: " + choice_list[x])
    print("User: " + choice_list[num])
    
    if num == x:
        print("Draw!")
    elif num == 0 and x==1 or num==1 and x==2 or num==2 and x==0:
        print("Computer wins.")
        comp_score += 1
    else:
        print("User wins!!")
        user_score += 1

    print(f"User score: {user_score}\nComputer score: {comp_score}")
    i = int(input("Another game? Type 1 for 'yes' and 0 for 'no': "))
