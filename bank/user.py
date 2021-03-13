from datetime import datetime as dt
import pickle


def acc_gen():
    i = 10101
    while True:
        yield i
        i+=1


def add_costumerData(acc_num,name,phone,addr,pan,card,u_name,u_pass,aadhaar,balance):
    lis = []
    lis.append(acc_num)
    lis.append(name)
    lis.append(u_name)
    lis.append(u_pass)
    lis.append(balance)
    lis.append(phone)
    lis.append(addr)
    lis.append(pan)
    lis.append(card)
    lis.append(aadhaar)
    acc_date = dt.today()
    hist = "deposit  " + str(acc_date) + "  amount: " + str(balance)
    his = [hist]
    lis.append(his)
    filename = str(acc_num)
    f = open('acc'+filename,"wb")
    pickle.dump(lis,f)
    f.close()



def enter_data():
    accont = acc_gen()

    acc_num = next(accont)

    name = input("enter the full name : ")

    phone = int(input("enter the phone number : "))

    addr = input("enter the address: ")

    pan = input("enter the pan number")

    card = input("enter the debit or credit card:")

    u_name = input("enter the user name we have: ")

    u_pass = input("enter the password:")

    aadhaar = int(input("enter the 12 digit  addhar number:"))

    balance = float(input("Enter the min balance 5000"))

    while True:
        if len(str(aadhaar)) != 12:
            aadhaar = int(input("enter the 12 digit addhar number:"))
        if not(pan[0:5].isalpha() and pan[5:-1].isnumeric() and pan[-1].isalpha()):
            pan = input("enter the  correct pan number:")
        if balance < 5000.00:
            print("Amount is less than min amount")
            balance = float(input("enter the minimum balance"))
        if name == u_name:
            print("user_name is unique not same as Name")
            u_name = input("enter the user name we have: ")
        else:
            break

    add_costumerData(acc_num = acc_num,name = name,phone = phone,addr = addr,pan=pan,card = card,u_name = u_name,u_pass=u_pass,aadhaar = aadhaar,balance = balance)

enter_data()