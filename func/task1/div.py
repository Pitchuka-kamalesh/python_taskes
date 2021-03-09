def div1(a, b):
    if b != 0:
        return (a/b)
    else:
        b = int(input("enter the b value not (0):"))
        return (a/b)


def div2(a, b):
    if b != 0:
        print("Division value is :", a/b)
    else:
        b = int(input("enter the b value other than 0 :"))
        print("Division value is :", a/b)


def div3():
    a = int(input("enter the a value:"))
    b = int(input("enter the b value:"))
    if b != 0:
        return (a/b)
    else:
        c = int(input("enter the b value other than 0:"))
        return (a/c)


def div4():
    a = int(input("enter the a value :"))
    b = int(input("enter the b value:"))
    if b != 0:
        print("division value is :", a/b)
    else:
        c = int(input("enter the b value:"))
        print("division value:", a/c)


print(div1(10, 0))
div2(10, 5)
print(div3())
div4()
