from datetime import datetime as dt
import pickle
import re


def acc_gen():
    i = 10101
    while True:
        yield i
        i += 1


def add_costumerdata(acc_num, name, phone, addr, pan, card,
                     u_name, u_pass, aadhaar, balance):
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
    f = open('acc' + filename, "wb")
    pickle.dump(lis, f)
    f.close()


accont = acc_gen()


def create_user_account():
    global accont
    acc_num = next(accont)

    name = input("enter the full name : ")
    while True:
        if len(name) == 0:
            name = input("enter the full name : ")
        else:
            break

    phone = input("enter the phone number : ")
    while True:
        if re.fullmatch(r"[0-9]{10}", phone) and len(phone) == 10:
            phone = int(phone)
            break
        else:
            phone = input("enter the phone number : ")

    addr = input("enter the address: ")

    pan = input("enter the pan number")
    while True:
        if re.match(r"^[a-z]{5}[0-9]{5}[a-z]$", pan) and len(pan) != 0:
            break

        else:
            pan = input("enter the  correct pan number:")

    card = input("enter the debit or credit card:")
    while True:
        if re.match("credit|debit", card):
            break
        else:
            card = input("enter the debit or credit card:")

    u_name = input("enter the user_name: ")
    while True:
        if len(u_name) != 0:
            if u_name == name:
                print("user_name is unique not same as Name")
                u_name = input("enter the user_name: ")
            else:
                break
        elif len(u_name) == 0:
            u_name = input("enter the user_name: ")
        else:
            break

    u_pass = input("enter the password len is 8:")
    while True:
        if len(u_pass) == 8 and re.fullmatch(r"[a-zA-z0-9@]{8}", u_pass):
            break
        else:
            print("Allowed characters in password  are [a-zA-z0-9@]")
            u_pass = input("enter the password:")

    aadhaar = input("enter the 12 digit  addhar number:")

    while True:
        if len(aadhaar) != 12 and re.fullmatch(r"[0-9]{12}", aadhaar):
            aadhaar = int(aadhaar)
            break

        else:
            aadhaar = input("enter the 12 digit addhar number:")

    balance = input("Enter the min balance 5000")

    while True:
        if re.match(r"\d{4}", balance):
            balance = float(balance)
            if balance < 5000.0:
                print("Amount is less than min amount")
                balance = input("Enter the min balance 5000")
            else:
                break
        else:
            balance = input("Enter the min balance 5000")

    add_costumerdata(acc_num = acc_num, name = name, phone = phone,
                     addr = addr, pan = pan, card = card,
                     u_name = u_name, u_pass = u_pass,
                     aadhaar = aadhaar, balance = balance)
