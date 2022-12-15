# Polymorphism can be carried out through inheritance, with sub classes making use of base class methods or overriding them.
#
# There are two types of polymorphism
#
# Overloading
# Overriding


# Overloading
# Overloading occurs when two or more methods in one class have the same method name but different parameters.
# Method Overloading in python:
# method over loading is the ability to have multiple method with same name but a different number of parameters.
#
# if the class contains more than one methods has same name & the method contains different datatypes(or)parameter(or)different no.of parameters
# python doesn't support method overloading unlike other oops langugae such as java and c++
#
# When we define a method with the same name as an already existing method, python replaces the oldmethod with the new method .
# It raises a type error when we try to accesss the old method.


class Addition:
    def method1(self,a,b):
        print(a+b)
    def method1(self,a,b,c):
        print(a+b+c)


ob=Addition()
ob.method1(10,20)
# TypeError: method1() missing 1 required positional argument: 'c'


