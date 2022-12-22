import time
import threading
def double(num):
    print('Double numbers:')
    for i in num:
        # time.sleep(0.2)
        print('square of i:',i**2)
        time.sleep(0.2)

def thriple(num):
    print('Triple numbers:')
    for i in num:
        # time.sleep(0.2)
        print('cube values:',i**3)
        time.sleep(0.2)

hari=time.time()
l=[1,2,3,4,5,6]
t1=threading.Thread(target=double,args=(l,))
t2=threading.Thread(target=thriple,args=(l,))

t1.start()
time.sleep(0.1)
t2.start()

t1.join()
t2.join()

print('time taken with thread:',time.time()-hari)

