# 4. Write a program to filter a list of numbers which are divisible by 5.


def divisible5(n):
    if n%5 == 0:
        return True
    return False

a = [32,32,45,65,223,12332,4312,4352,534,54,66,25]

f = list(filter(divisible5 , a))

print(f)