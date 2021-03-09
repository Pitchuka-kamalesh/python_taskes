import os, sys


if (os.path.isfile("adds.txt")):
    print("file is present")
    f = open("adds.txt","r")
else:
    print("file is not present ")
    sys.exit()
line = word = char = 0
for i in f:
    l = i.split()
    line = line+1
    word = word+len(l)
    char = len(i)

print("no of lines :",line)
print("no of words: ",word)
print("no of char :",char)