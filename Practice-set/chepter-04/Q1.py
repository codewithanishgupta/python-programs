# 1. Write a program to store seven fruits in a list entered by the user.

list = []


print("Enter the 7 Fruits name  ")

for l in range(1,8):
    f=input(f"Enter {l} fruit name : ")
    list.append(f)

print(list)