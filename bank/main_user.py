from user import *
from read_user import *
from update import *

# variable's used
# 1 . for the new user account details
# 2.  for the read the account details
# 3.  for the modifying the account details
# TODO: have to update the bank transaction history and payee and validation of bank account and storing of
#  bank account number
print("*******  WELCOME TO BANK  ********")
while True:
    choice = input('enter the yes to continue and no stop :')
    if choice == "no":
        break

    elif choice == "yes":
        print(" press 1 to create the account")
        print(" press 2 to read the customer data")
        print(" press 3 to update the account")

        option = input("Enter the option: ")
        if option == "1":
            create_user_account()  # This function is in user.py file
            continue

        elif option == "2":
            acc = int(input("Enter the account Number:"))
            read_data(acc)  # This function is in read_user.py
            continue

        elif option == "3":
            acc = int(input("Enter the account Number:"))
            update(acc)   # This function is in update.py
            continue
        else:
            print("invalid  option")
    else:
        print("invalid option")
