# Single Inheritance
# In single inheritance, a child class inherits from a single-parent class. Here is one child class and one parent class.
class parent_property:
    def pr1(self):
        print('This is parent property / '
              'and also we called as a super class')
class Child_Property(parent_property):
    def pr2(self):
        print('THis is child property2/ '
              'and also called as a inherit or subclass')





# Object creation for who is inherit:
ob1=Child_Property()
ob1.pr2()
# THis is child property2/ and also called as a inherit or subclass
ob1.pr1()
# This is parent property / and also we called as a super class

