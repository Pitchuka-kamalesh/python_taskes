import pickle
import time
key_s = ['Account Number','Name','user name','User password','Balance','Phone','Addr','Pan',"Card","Aadhar","History"]
f = open("acc10101","rb+")
data = pickle.load(f)
print(data)
print("*"*10+"  Update Account Details  "+"*"*10)

