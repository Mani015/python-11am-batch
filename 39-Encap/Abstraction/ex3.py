
from abc import ABC, abstractmethod
class Mobile(ABC):
    @abstractmethod
    def Mehtod1(self):
        pass

    @abstractmethod
    def Method2(self):
        None





class Samsung(Mobile):
    def Mehtod1(self):
        print('this is instance of abstract base class')
    def Method2(self):
        print('this is method2 ')


class one(Mobile):
    def method1(self):
        print('this is method one')
ob=Samsung()
ob.Mehtod1()
ob.Method2()

ob2=one()
ob2.method1()