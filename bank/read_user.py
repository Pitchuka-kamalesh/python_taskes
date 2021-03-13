import pickle
import time
key_s = ['Account Number','Name','user name','User password','Balance','Phone','Addr','Pan',"Card","Aadhar","History"]
f = open("acc10101","rb+")
data = pickle.load(f)
print(data)
print("*"*10+"  Account details  "+"*"*10)
print("\n")
for i,j in zip(key_s,data):
    print(f"{i} : {j} \n")
    time.sleep(0.25)


