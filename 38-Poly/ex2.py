# How to get old method data in method overriding in polymorphism:

# Super() in python:The Super() function retirn a temparory object that represents parent class .
# this is used to accesss the parent class method and attributes.
# with the help of the super(), we can also access the over ridden method

class Parent:
    def property1(self):
        print('This is property 1')

class Child(Parent):
    def property1(self):
        print('this is child property 2')
    def property2(self):
        super().property1()


obj=Child()
obj.property1()
# this is child property 2
# We are using the super () function to get parent methods and attributes

# temparory method:
obj.property2()
# this is child property 2
# This is property 1
