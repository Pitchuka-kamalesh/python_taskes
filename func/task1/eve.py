def eve(num):
    print("\n even numbers")
    for i in range(0, num+1, 2):
        print(i, end=",")


def odd1(num):
    print("\n odd numbers")
    for i in range(1, num+1, 2):
        print(i, end=",")


eve(10)
odd1(10)
