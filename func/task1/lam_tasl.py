a = [1,2,3,4,5,6,7,8,9,10]

a = list(filter(lambda x: x%2==0, a))

def pow(a):
    c = []
    for i in a:
        if i%2 == 0:
            c.append(i**2)
    return c
# print(pow(a))

c = list(map(lambda x:x**2,filter(lambda x:x%2==0,a)))

print(c)