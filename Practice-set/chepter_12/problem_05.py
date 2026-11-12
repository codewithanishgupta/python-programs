# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt .


n = int(input("Enter a number : "))

l = [i*n for i in range(1 , 11)]

print(l)

with open("Table.txt","a") as e:
    e.write(f"table of {n} : {str(l)}\n ")