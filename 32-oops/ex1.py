# Instance method:
#.by default the methods we  can create in class are instance methods.
# 2.Instance method is also called as a method of object
# Instance methods: Used to access or modify the object state.
# If we use instance variables inside a method, such methods are called instance methods.
# It must have a self parameter to refer to the current object.

class Bike:
    def method1(self):
        print('This is method one')
    def method2(self,a,b):
        print(a,b)

ob1=Bike()
ob1.method1()

ob1.method2(10,20)