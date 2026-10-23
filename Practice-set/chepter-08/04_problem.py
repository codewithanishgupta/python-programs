# 4. Write a recursive function to calculate the sum of first n natural numbers


def rec_sum(n):
    if n==1:
        return 1
    
    return n+rec_sum(n-1)
    
n = int(input("Enter n natural number : "))

print("Sum of n natural number is : ",rec_sum(n))