'''
3. A list contains the multiplication table of 7. Write a program to convert it to vertical string
of same numbers.
                    7
                    14
                    .
                    .
                    .
'''


table = [str(7*i) for i in range(1,11)]

s ="\n".join(table)

print(s)