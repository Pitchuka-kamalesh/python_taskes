from threading import *

repo = []

l = Condition()
# n = int(input("enter the range "))
i = 0
j = True

def production():
    global repo
    global i
    global j
    global e
    l.acquire()
    print("Entering the Production ")
    while j:
        if len(repo) == 0:
            # print("looping in production started")
            while i <= 200:
                repo.append(i)
                print("repo =", repo)
                i += 2
                if len(repo) == 5:
                    break

        l.notify()
        l.wait()

    l.release()


def consumption():
    global repo
    global j
    global i
    global  e
    l.acquire()
    print("enter into consumption")
    print("repo before while loop in consumption =", repo)
    while j:
        for k in range(len(repo)):
            print("repo =", repo)
            repo.pop()
            # print("repo =", repo)
            if len(repo) == 0:
                if i == 200:
                    j = False
                break
        if i == 200:
            continue
        l.notify()
        l.wait()
    l.notify()
    l.release()


t1 = Thread(target=production)
t2 = Thread(target=consumption)
t1.setName("t1")
t2.setName("t2")
t1.start()
t2.start()
