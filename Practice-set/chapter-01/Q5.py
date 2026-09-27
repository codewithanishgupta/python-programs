# 5. Label the program written in problem 4 with comments.



import os

# Path of the directory   
directory = "."

# Get the contents of the directory
contents = os.listdir(directory)

# Print each item
for item in contents:
    print(item)