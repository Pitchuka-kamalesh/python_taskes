def mul1(a, b):
    return a*b


def mul2(a, b):
    print("multiplication value :", a*b)


def mul3():
    a = int(input("enter the a value:"))
    b = int(input("enter the b value:"))

    return a*b


def mul4():
    a = int(input("enter the a value:"))
    b = int(input("enter the b value:"))
    print("multiplication value of :", a*b)


print(mul1(10, 20))
mul2(10, 20)
print(mul3())
mul4()
