import pickle
import time


def read_data(acc):
    key_s = ['Account Number', 'Name', 'user name', 'User password', 'Balance', 'Phone', 'Address', 'Pan', "Card",
             "Aadhaar", "History"]
    filename = "acc" + str(acc)
    f = open(filename, "rb+")
    data = pickle.load(f)
    print("*" * 10 + "  Account details  " + "*" * 10)
    print("\n")
    for i, j in zip(key_s, data):
        print(f"{i} : {j} \n")
        time.sleep(0.05)
