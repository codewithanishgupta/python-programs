# 4. Write a program to find whether a given username contains less than 10 characters or not

user = input("Enter the given username : ")

l = len(user)
print(l)
if l < 10 :
    print("You Enter less than 10 characters!")
else:
    print("Good username is grater than 10 character!")