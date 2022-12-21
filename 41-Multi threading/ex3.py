# Multi-Threading:


class A:
    def f1(self):
        for i in range(10):
            print('hello pyhton',i)



class B:
    def f2(self):
        for i in range(10):
            print('hello java',i)


ob1=A()
ob1.f1()
print('java class will start:')
ob2=B()
ob2.f2()


