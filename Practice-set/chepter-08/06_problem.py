# 6. Write a python function which converts inches to cms


def in_to_cms(n):
    return n*2.54

n = int(input("Enter the given inches : "))
print(f"In inch : {n} In cm : {in_to_cms(n)}")