from threading import *
from time import *
def the1(fil):
    a = int(input("enter the number"))
    sleep(1)
    with open(fil,"a+") as f:
        f.write(str(a)+"\n")


f = "trail.txt"
t1 = Thread(target=the1,args=(f,))
t2 = Thread(target=the1,args=(f,))

t1.setName("thread1")
t2.setName("thread2")

t1.start()
sleep(1)
t2.start()
