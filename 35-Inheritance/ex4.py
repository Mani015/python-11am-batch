# Multilevel inheritance
# In multilevel inheritance, a class inherits from a child class or derived class.
# Suppose three classes A, B, C. A is the superclass, B is the child class of A, C is the child class of B.
# In other words, we can say a chain of classes is called multilevel inheritance.

class A:
    def p1(self):
        print('this is parent wealth')

class B(A):
    def p2(self):
        print('This   child wealth ')



class C(B):
    def p3(self):
        print('This is grand child wealth')


ob1=C()
ob1.p1()
ob1.p2()
ob1.p3()