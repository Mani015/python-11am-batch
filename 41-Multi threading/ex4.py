from time import *
from threading import *


# class threading

class whatsapp(Thread):
    def run(self):
        for i in range(10):
            print('using whatsapp')
            sleep(1)

class telegram(Thread):
    def run(self):
        for i in range(10):
            print('using telegram')
            sleep(1)
t1=whatsapp()
t2=telegram()

t1.start()
sleep(0.2)
t2.start()