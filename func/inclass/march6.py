from time import sleep

class A:

    def __init__(self):
        print("This is Init class A")
        super().__init__()

class B:

    def __init__(self):
        print("This is Init class B")
        super().__init__()

class C:

    def __init__(self):
        print("This is Init class C")
        super().__init__()

class D:

    def __init__(self):
        print("This is Init class D")
        super().__init__()

class X(A,B):

    def __init__(self):
        print("This is Init class X")
        super().__init__()

class Y(B,C):
    def __init__(self):
        print("This is Init class Y")
        super().__init__()


class V(C,D):

    def __init__(self):
        print("This is Init class v")
        super().__init__()

class Z(X,Y,V):

    def __init__(self):

        print("This is Init class Z")
        super().__init__()


obj = Z()

