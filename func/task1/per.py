import timeit

steps = "looping for prime numbers"
mycodefor = """
pro = 1
for i in range(1,10000):
    pro=pro*i

"""
mycodefun = """
def fact(n=10000):
    if n == 1 or n == 0:
        return(1)
    else:
        t = (n * fact(n-1))
        print(t)
        

"""

mycodewhile = """
i = 1
pro = 1
while i<10000:
    pro = pro*i
    i+=1
"""
time_fu = timeit.timeit(stmt = mycodefun,number = 10000)
time_f = timeit.timeit(stmt = mycodefor,number = 10000)
time_w = timeit.timeit(stmt = mycodewhile,number = 10000)
print(time_fu,"func loop")
print(time_f,"fun loop")
print(time_w,"while loop")
# print(fact(5))
