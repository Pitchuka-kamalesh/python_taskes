# #
# c_id = int(input(" Enter the Electricity bill id: "))
# c_name = input("Enter the costumer name :")
# add_s = input("Enter the address of the costumer :")
# type_b = input("Enter the type of consumption Dom or Com")
# unit = int(input("enter the consumption units"))
#
#
#
#
#
#
#
# if type_b == "Dom":
#     if unit <= 100:
#         bill = unit *6
#     elif unit > 100 and unit <= 200 :
#         bill = unit*8
#     elif unit > 200 and unit <= 300:
#         bill = unit*10
#     else:
#         bill = unit*14
#
#
# elif type_b == "Com":
#     if unit <= 100:
#         bill = unit * 8
#     elif unit > 100 and unit <= 200:
#         bill = unit * 10
#     elif unit > 200 and unit <= 300:
#         bill = unit *12
#     else:
#         bill = unit*16

# # repo = [1,2,4,5,6]
# # print(repo)
# # for i in  range(len(repo)):
# #     repo.pop()
# #     print(repo)

# i = 0
# while i < 10:
#     print(f'{i} value ')
#     for j in range(10):
#         print(f'{i} in {j}')
#         if j == 6:
#             i = i+1
#             break

# a = 100
# b = 200
# c = 300
# if a>b and a>c:
#     print("a is largest number")
# elif b>a and b>c:
#     print("b is the biggest number")
# else:
#     print("c is the biggest number")
#
# print("hello world \n"*5)

# texts = input("enter the string ")
# for text in texts:
#     print(text)
#
# print("even numbers from o to 10")
# for i in range(0,11,2):
# 	print(i)
# apples = [1,2,3,4,5,]
# for apple in apples:
#     print("quantity of apples: ",apple)

# for i in range(0,5):
#     for j in range(0,4):
#         print(f"i value{i} ➡➡ j value{j}")

# print("printing the even numbers from 0 to 10 using while loop")
# i = 0
# while i<= 10:
#     print(i,end=",")
#     i+=2

# print("nested while loop")
# i = 0
# while i<=5:
#     j = 0
#     while j<=4:
#         print(f"i value{i} ➡➡ j value{j}")
#         j+=1
#     i+=1

# for i in range(0,11,1):
#     if i==5 or i==6 or i==7:
#         continue
#     print(' i :',i)
# i = 0
# while i<10:
#     j = 0
#     while j <10:
#         k = 0
#         while k <10:
#             print(f"i value{i} j value {j} k value {k} ")
#             k += 1
#             if k ==5:
#                 print("break in k = 5")
#                 break
#         j+=1
#     i+=1
# for i in range(11):
#     if i<11:
#         print(" i loop in if condition: ",i)
#         for j in range(10):
#             print(j)
#             if i%2 == 0:
#                 print(" befor break statement")
#                 break
#
# for i in range(0,10):
#     print("i loop : ",i)
#     for j in range(0,10):
#         print("j loop :",j)
#         if i == 7:
#             break
#
#    print ("loop break in j loop ")
# def grnor_1(n):
#     for i in range(0,n):
#         yield i
# class Add_1:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def show(self,c):
#         print(self.a + self.b+c)
#
# obj = Add_1(10,20)
# obj.show()
# a = "apple0000"
# while True:
#     if a[0:5].isalpha() and a[-1].isalpha() and a[5:-1].isnumeric():
#         break
#     else:
#         print("enter the valid pan number")
#         a = input("enter the pan number: ")
# print(a)

# def gen_acco(i):
#     while i<10:
#         i
#         i+=1
#
# x = gen_acco(0)
# print(next(g))
# n = 10# all ready have account
# k = 10# we want new account
# for i in range(n,k+n):
#     print(f"account number{i}")
# user_name = ["kamal","apple",]
#
# user = input("enter the username:")
# while True:
#     if user in user_name:
#         print(True)
#         user = input("this user name is all ready exits enter unique id:")
#     else:
#         print("user name: ", user)
#         break
# addar = input("enter addar number :")
#
# if len(addar) != 12:
#     print("enter the valid addhar number : ")
# elif len(addar) == 12:
#     try:
#         addar = int(addar)
#     except ValueError:
#         print("enter only numbers")
#         addar = input("enter addar number :")
#     print("addarnumber ",addar)

user_names = ["kamal", "apple", ]

# a = "apple"
#
# if a in user_name:
#     print(user_name.index())

# if user_name in user_names:
#     pos = user_names.index(user_name)
#     if password == pas[pos]:
#         print("succesfully login")
#         j = False
#         break
#     else:
#         enter the

# account details balance money transfer  transation history
# det = {}
# def detaisl(**kwargs):
#     global det
#     print(kwargs)
#     det = kwargs
# name = ["apple","bat"]
# detaisl(name=name,task = "bank details")
# print(det)
# def feb(n):
#     a = 0
#     b = 1
#     for i in range(n):
#         yield a
#         a,b = b,a+b
#
#
# g = feb(10)
#
# print(next(g))
# lamdba function

# def swaps(a,b):
#     print (f"before swap in function a : {a} b : {b}")
#     a,b = b,a
#     print(f"after swapping the function in a: {a} b: {b}")
#     return a,b
#
# a = 10
# b = 20
# print(f"***before swap a : {a} b : {b}")
# a,b = swaps(a,b)
#
# print(f"after swapping the  a: {a} b: {b}")

# def outer():
#     print("it is outer function")
#     def inner():
#         print("it is inner function")
#     return inner
#
# a = outer()
# a()

adata = {}


# def user_data(**kwargs):
#     global adata
#     adata = kwargs
#
#     print(adata)
#
#
# def data():
#     acc_no = int(input("enter the account number: "))
#     name = input("enter the name : ")
#     ads = input("enter the address: ")
#     phone = int(input("enter the phone number: "))
#     bal = float(input("enter the min balance 5000: "))
#     uname = input("enter the user name:")
#     upass = input("enter the password:")
#     user_data(acc_no=acc_no, name=name, ads=ads, phone=phone, bal=bal, uname=uname, upass=upass)
#
#
# choice = int(input("enter 1 for user creation form" ))
#
# if choice == 1:
#     data()
# lambda i:i+1
#
# filter()
# f = open("test.txt","a+")
#
# f.write("welcome")
# f.read()
# f.close()
# class Add_cls:
#
#     def setdata(self,a):
#         self.a = a
#         print(self.a)
#     def add(self,x,y):
#         self.a = x.a+y.a
#         self.y = y
#         print(self.a)
#
# obj = Add_cls()
# obj1 = Add_cls()
#
# obj.setdata(100)
# obj1.setdata(200)
# print(obj)
# obj1.add(,200)

# a = [1,2,3,4,5,6]
# for r in a:
#     if r%2 == 0:
#         print(r

# i = 1
# while i<10:
#     if i == 0:
#         break
#     print(i)
#     i+=1

# class Student_data:
#     def student(self,roll,name,addres,eng,math,ches):
#         self.roll = roll
#         self.name = name
#         self.address = addres
#         self.math = math
#         self.eng = eng
#         self.ches = ches
#         self.total = self.eng+self.ches+self.math
#         self.percent = self.total/3
#     def show(self):

# write a program for student details
# def student(name,roll,addr,eng,math,ches):
#     total_marks = 300
#     total = eng+math+ches
#     per = (total/total_marks)*100
#     print("*"*5)
#     print("marks memo")
#     print(f"Student name :  {name}")
#     print(f"roll number: {roll}")
#     print(f"English marks :{eng}")
#     print(f"Maths marks: {math}")
#     print(f"chemistry marks: {ches}")
#     print(f"Total marks : {total}")
#     print(f'Overall total marks:{total_marks} ')
#     print(f"percentage :{per} ")
#     print("*" * 5)
#
#
#
#
#
#
# name = input("enter the name: ")
# roll = input("enter the roll number :")
# addr = input("enter the address : ")
# print("each subject overall marks 100")
# eng = float(input("enter the english marks :"))
# math = float(input("enter the maths marks :"))
# chem = float(input("enter the chemistry marks:"))
#
# student(name=name,roll = roll,addr=addr,eng = eng,math = math,ches=chem)


# write a lambda function with example
#
# # given a list of elements from 1 to 10
#
# a = list(filter(lambda x : x%2==0,range(1,11)))
# print(a)
#
# # squaring a every number from the filter list
#
# b = list(map(lambda x:x**2,a))
# print(b)

# Decorator function
# def: we have to  change the functionality of the function with out changing the code of the function

# def decor_1(fun):
#     def update_div(a,b):
#         if b == 0:
#             print("ZeroDivisionError because denominator is  b value is 0: ")
#         else:
#
#             print(f"division value {a},{b}",a/b)
#     return update_div
# @decor_1
# def div(a,b):
#
#     return(a/b)
#
# print("division of two numbers :",div(10,0))

#generators:
# generator are used generate the value in one place and we can retive the value one by one

#
# def gen_1(n):
#     for _ in range(n):
#         yield(_)
#
# a = gen_1(10)
# for _ in range(10):
#     print(next(a))
#     # print(a.__next__())


# Recuration function :
# calling the function by it self is called recuraction function

# num = 1
# def fact(n):
#     global num
#     num = num*n
#     n+=1
#     if <n:
#         fact(n)
#     return num
#
# print(fact(1))

# palindrome's number

# a = input("enter num or string: ")
# b = ""
# for i in a:
#     b = i+b
# if a == b:
#     print(f"given string or int is {a} is palindrome number")
# else:
#     print("given the numbers is not palindrome number:")








