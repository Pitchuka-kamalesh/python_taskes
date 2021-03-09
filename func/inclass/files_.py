# march 9 topic files
f = open("adds.txt", "r+")

a = f.readline()
print("a value :")
b = f.readline()
print(b)
c = int(a)+int(b)
print("sum:", c)

f.write("sum of numbers:"+str(c))
f.close
