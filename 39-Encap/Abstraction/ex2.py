

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

ob=Samsung()
ob.Mehtod1()
ob.Method2()

