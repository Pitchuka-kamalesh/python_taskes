from threading import *

repo = []
l = Condition()


def production():
    global repo
    l.acquire()
    while True:
        if len(repo) == 0:
            while i<200:
                repo.append(i)
                i+=2
                if len(repo) == 5:
                    print(repo)
                    break
        l.notify()
        l.wait()
    l.release()

def consumption():
    global repo
    l.acquire()


    l.release()


production()