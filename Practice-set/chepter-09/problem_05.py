# Repeat program 4 for a list of such words to be censored.

words = ["Donkey","bad","ganda"]

with open("donkey.txt") as f :
    contains = f.read()
   
for word in words :  
    contains = contains.replace(word,"#" * len(word))

with open("donkey.txt","w") as  f :
    f.write(contains)