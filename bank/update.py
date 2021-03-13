import pickle
import time
def update(acc):
    key_s = ['Account Number','Name','user name','User password','Balance','Phone','Addr','Pan',"Card","Aadhar","History"]
    filename = "acc"+str(acc)
    f = open(filename,"rb+")
    data = pickle.load(f)
    print("*"*10+"  Update Account Details  "+"*"*10)


