import pickle

def add_customerData(accno,name,bal,history=None):

    lst=[]
    lst.append(accno)
    lst.append(name)
    lst.append(bal)
    if history==None:
        lst.append(list())

    filename=str(accno)
    f=open('acc'+filename,'wb')
    pickle.dump(lst,f)
    f.close()

filename=str(1020200)
f=open('acc'+filename,'rb')
data=pickle.load(f)
print("customer data :",data)
h='debit 5000rs'
data[len(data)-1].append(h)
print(data)
f.close()
f=open('acc'+filename,'wb')
pickle.dump(data,f)
f.close()
"""
#add_customerData(10200,'ravi sharama',5000,)
add_customerData(1020200,'ravi sharama',5000,)

filename=str(1020200)
f=open('acc'+filename,'rb')
data=pickle.load(f)
print(data)

"""