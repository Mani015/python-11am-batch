from abc import  ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def m1(self):
        pass
    def m2(self):
        print('this is concreate method')




class B(A):
    def m1(self):
        print('m1 method')


ob=B()
ob.m1()
ob.m2()