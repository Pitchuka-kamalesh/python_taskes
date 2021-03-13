import pickle
print("*******WELCOME TO BANK********")
filename=str(1020200)
f=open('acc'+filename,'rb')
data=pickle.load(f)
print("customer data :",data)
h='debit 5000rs'
data[len(data)-1].append(h)
print(data)
f.close()
while True:
   choice=input('enter the Yes to continue and No stop')
   if choice=='No':
       break
   print(" press 1 to create the account")
   print(" press 2 to read the customer data")
   print(" press 3 to update the account")
   option=int(input())
   if option==1:
     print("create the account")
   if option==2:
     print("read the customer data")
   if option==3:
     print("update the account")
   else:
      print("invalid option")
