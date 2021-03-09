def fact(num):
    a = 1
    for i in range(1, num+1):
        a = i*a
    return a


fac = fact(5)

print(" factorial of 5 is :", fac)
