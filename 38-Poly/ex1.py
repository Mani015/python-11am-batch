# Overriding
# Overriding means having two methods with the same method name and parameters (i.e., method signature).
# One of the methods is in the parent class and the other is in the child class.
#
# working:Method Overriding  want to change the behaviour of a mehtod defined in the parent class.
# we can simply create a new method in the child class with the same name asthe method  in the parent class
# new method overrides the oldmethod .....--->THis is callled method overiding





class A:
    def method1(self):
        print('THis is mehtod one')
class B(A):
    def method1(self):
        print('This is second method')

object=B()
object.method1()
object.method1()
# This is second method
# This is second method
