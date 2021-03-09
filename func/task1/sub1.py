# fun with args and return

def sub1(a, b):

    return a-b


def sub2(a, b):
    c = a-b

    print("Subtraction value is :", c)


def sub3():
    a = int(input("enter the a value :"))
    b = int(input("enter the b value"))
    return a-b


def sub4():
    a = int(input("enter the a  value: "))
    b = int(input("enter the b value: "))

    print("Subtraction value is :", a-b)


print(sub1(10, 20))
sub2(10, 20)
print(sub3())
sub4()
