# Multiple Inheritance
# In multiple inheritance, one child class can inherit from multiple parent classes.
# So here is one child class and multiple parent classes.

class Parent1:
    def method1(self):
        print('This is parent1 property')


class Parent2:
    def method2(self):
        print('This is parent2 property')


class Child(Parent1,Parent2):
    def method3(self):
        print('THis is child property')
object=Child()
object.method1()
object.method2()
object.method3()
# This is parent1 property
# This is parent2 property
# THis is child property