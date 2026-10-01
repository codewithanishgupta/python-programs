# 7. Write a program to find out whether a given post is talking about “Anish” or not.


post = input("Enter your post : ")

if("anish" in post.lower()):
    print("This post is talking about anish!")
else:
    print("This post is not talking about anish!")
    