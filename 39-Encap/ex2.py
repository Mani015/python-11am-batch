class ABC:
    __privatedata_=100
    ___privatedata=200
    def m1(self):
        print(self._ABC__privatedata_)
class DEF(ABC):
    def m2(self):
        print(self._ABC__privatedata_)




ob=DEF()
ob.m1()
ob.m2()
print('private data acessing the out of the class usnig with class name:',ob._ABC__privatedata_)
# 100
# 100
# private data acessing the out of the class usnig with class name: 100

