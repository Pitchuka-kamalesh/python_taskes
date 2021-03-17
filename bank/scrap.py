# import pickle
#
# key_s = ['Account Number', 'Name', 'user name', 'User password', 'Balance', 'Phone',
#          'Address', 'Pan', "Card", "Aadhaar", "History"]
# f = open("acc1010152","rb+")
# data = pickle.load(f)
# print(data)
# for i, j in zip(list(range(0,len(key_s))),data):
#     print(str(data[i]) + f" ⏩ {j} ")
#
# f.close()

# aadhaar = "123456789012"
# b = not(len(aadhaar) != 12 and aadhaar.isnumeric())
# print(len(aadhaar) != 12)
# u_name = input("enter the user name")
# a = u_name == ""
# print(a)
# import re

# balance=input("Enter the min balance 5000")

# while True:
#     if re.match(r"\d", balance):
#         balance = float(balance)
#         if balance < 5000.0:
#             print("Amount is less than min amount")
#             balance=input("Enter the min balance 5000")
#         else:
#             break
#     else:
#         balance=input("Enter the min balance 5000")

data_1 = {'one':10,"two":{"three":30,"four":{"five":50,"six":{"seven":70}}}}
out = []
while True:

    for k_key,k_valu in data_1.items():
        out.append(k_valu)
    if str(out[-1]).isnumeric():
        break
    else:
        data_1 = out.pop()
 
print(out)