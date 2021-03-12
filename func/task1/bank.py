from user_data import *
import sys
data = bank_acc

def goback():
    print("\n")
    print(" "*15+"1 : for go back to previous menu")
    print(" "*15+"2 : for exit")
    i = int(input("enter the option:"))
    if i == 1:
        transfer()
    elif i ==2:
        sys.exit()
    else:
        print("option not found enter the option")
        goback()


def transfer():
    print("\n")
    print(" " * 20 + "1 is bank details ")
    print(" " * 20 + "2 is transition_history ")
    print(" " * 20 + "3 is payee ")
    j = int(input("enter the details:"))
    if j == 1:
        bank_details()
    elif j == 2:
        trans_history()
    elif j == 3:
        transistion()
    else:
        transfer()


def bank_details():
    global data
    for keys, values in data.items():
        print(f"{keys}  : {values}")
    goback()


def transistion():
    global data
    name = input("enter the name  of user :")
    acc_no = int(input("enter the account number:"))
    while True:
        if acc_no == data['acc_num']:
            break
        else:
            acc_no = int(input("enter the account number:"))
    pay_name = input("enter the name:")
    pay_acc = int(input("enter the payee account number:"))
    amount = float(input("enter the amount to be transfer :"))
    if amount > data['balance']:
        print("insufficient fund :")
        print("account balance amount :", data['balance'])
        transistion()
    else:
        print(f"amount {amount} is transfer for to {pay_name} with account {pay_acc}")
        trn = "Transfer "+str(datetime.datetime.today())+" "+"amount:"+str(amount)
        data['history'].append(trn)
        data['balance'] = data['balance']-amount
        goback()


def trans_history():
    global data

    for i in data['history']:
        print(i)
    goback()


print("*"*20)
print("\n")
print("Welcome To the Bank ")
print("\n")
print("*"*20)

print(" "*10+"Enter 1 for new user: ")
print(" "*10+"enter 2 for exciting user:")
i = int(input("Enter the number:"))

if i == 1:
    print("Bank details form \n")
    data = enter_data()
    print("\n")
    print("Your account number is :", data['acc_num'])
    print("\n")
    transfer()
else:
    pass
    print("Enter the user name :")
    print("enter the password:")
    if i == 2:
        print(" "*20+"1 is bank details ")
        print(" "*20+"2 is transition ")
        print(" "*20+"3 is payee ")

        j = int(input("enter the details:"))
        if j == 1:
            bank_details(data)
            pass
        elif j == 2:
            pass
        else:
            pass

#    k = input("submit")
#     print()




# goback()