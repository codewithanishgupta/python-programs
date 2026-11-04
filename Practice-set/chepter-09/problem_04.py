# A file contains a word “Donkey” multiple times. You need to write a program which replaces this word with ##### by updating the same file.


word = "Donkey"
with open("donkey.txt") as f :
    contains = f.read()
    
containsNew = contains.replace(word,"#####")

with open("donkey.txt","w") as  f :
    f.write(containsNew)
