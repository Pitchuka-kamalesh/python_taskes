def deco_1(fun):
    def update_div(a,b):
        if b == 0:
            b = int(input("enter the valid input other than 0:"))
            return(a/b)
    return (update_div)



@deco_1
def div(a,b):

    return(a/b)

a = div(10,0)
print(a)