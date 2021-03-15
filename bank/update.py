import pickle
import re

data = []

a = [1, 2, 3, 5, 6, 7, 8, 9]


def profile_update():
    name = input("enter the full name : ")
    while True:
        if len(name) != 0 and re.match(r"[a-zA-z ]{0,60}", name):
            break
        else:
            name = input("enter the full name : ")

    u_name = input("enter the user name we have: ")

    while True:
        if name == u_name:
            print("user_name is unique not same as Name")
            u_name = input("enter the user name we have: ")
        else:
            break

    u_pass = input("enter the password len is 8:")
    while True:
        if len(u_pass) == 8 and re.fullmatch(r"[a-zA-z0-9@]{8}", u_pass):
            break
        else:
            print("Allowed characters in password  are [a-zA-z0-9@]")
            u_pass = input("enter the password:")

    phone = int(input("enter the phone number : "))
    while True:
        if re.fullmatch(r"^[6-9][0-9]{9}", phone) and len(phone) == 10:
            phone = int(phone)
            break
        else:
            phone = input("enter the phone number : ")

    addr = input("enter the address: ")
    while True:
        if len(addr) == 0 and re.match(r"^\w", addr):
            addr = input("enter the full name : ")
        else:
            break

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

    aadhaar = int(input("enter the 12 digit  addhar number:"))

    while True:
        if len(aadhaar) != 12 and re.fullmatch(r"[0-9]{12}", aadhaar):
            aadhaar = int(aadhaar)
            break

        else:
            aadhaar = input("enter the 12 digit addhar number:")

    return name, u_name, u_pass, phone, addr, pan, card, aadhaar


def update(acc):
    global data, a
    key_s = ['Account Number', 'Name', 'user name', 'User password', 'Balance', 'Phone',
             'Address', 'Pan', "Card", "Aadhaar", "History"]
    filename = "acc" + str(acc)
    f = open(filename, "rb+")
    data = pickle.load(f)
    print("*"*10 + "  Update Account Details  " + "*"*10)
    data_update = profile_update()
    for i, j in zip(a, data_update):
        print(" "*20 + f"{key_s[i]}" + " "*20)
        print(str(data[i]) + f"  ⏩ {j} ")
        data[i] = j
    f.seek(0, 0)
    pickle.dump(data, f)
    f.close()
