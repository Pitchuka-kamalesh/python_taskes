from user import *
from read_user import *
from update import *

# varibles used
#1 . for the new user account details
#2.  for the read the account details
#3.  for the modifing the account details

print("*******  WELCOME TO BANK  ********")
while True:
   choice=input('enter the Yes to continue and No stop')
   if choice=='No':
       break
   print(" press 1 to create the account")
   print(" press 2 to read the customer data")
   print(" press 3 to update the account")
   option=int(input("Enter the option: "))
   if option==1:

       enter_data()
       break
   if option==2:

       read_data()
       break
   if option==3:
       update()
       break
   else:
      print("invalid option")