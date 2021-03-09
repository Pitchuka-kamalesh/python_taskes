# march 5 topic

# def add_n(*args):
#     sum = 0
#
#     print(args)
#     for arg in args:
#         sum = sum +arg
#     print("addition  is :",sum)
#
# add_n(10,20,30,40,50,60)
#
# sum = add_n
# sum(10,20)
# print("address od add_n",id(add_n))
# print("address of sum:",id(sum))
#
# def outer_fun():
#     print("it is outer function")
#     def inner_fun():
#         print("it is inner function:",id((inner_fun)))
#
#     return inner_fun # return the address of  inner_fun  to the outer_fun
#
# x = outer_fun()
# x()

# decerators functions  @function_name
"""
def function_name(arguments(fun)):
    def modified_fun(args):
        statement
    return modified_fun

def main_fun(arguments):
    logic & statement
    return value
"""
def div(a,b):
    return (a/b)

