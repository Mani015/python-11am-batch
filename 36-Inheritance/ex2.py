# Hierarchical Inheritance
# In Hierarchical inheritance, more than one child class is derived from a single parent class.
# In other words, we can say one parent class and multiple child classes.

class Parent:
    def method1(self):
        print('this is parent property')


class Child1(Parent):
    def method2(self):
        print('child1 property')

class Child2(Parent):
    def method3(self):
        print('child2 propety')

ob1=Child1()
ob1.method1()
ob1.method2()
# this is parent property
# child1 property

ob2=Child2()
ob2.method1()
ob2.method3()
# this is parent property
# child2 propety







