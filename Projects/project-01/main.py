'''
snake water gun gam

1 for snake 
2 for water
3 for gun

'''

import random

computer = random.choice([1,2,3])
userstr = input("Enter your choice : ")
userDict = {"s":1 , "w" : 2 , "g":3}
reverseDict = {1 : "s" , 2 : "w" , 3 : "g"}

user = userDict[userstr]

print(f"You chose {reverseDict[user]} \nComputer chose {reverseDict[computer]}")

if computer == user:
    print("Match Draw!")
else :
    if computer == 1 and user == 2:
        print("you lose!")
    elif computer == 1 and user == 3 :
        print("yow win!")
    elif computer == 2 and user == 1:
            print("you win!")
    elif computer == 2 and user == 3 :
        print("yow lose!")
    elif computer == 3 and user == 1:
            print("you win!")
    elif computer == 3 and user == 2 :
        print("yow win!")
    else:
        print("Somthing went worng!")