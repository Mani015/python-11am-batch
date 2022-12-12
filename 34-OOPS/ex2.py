# There can be some functionality that relates to the class,
# but does not require any instance(s) to do some work, static methods can be used in such cases.
# A static method is a method which is bound to the class and not the object of the class.
# It can’t access or modify class state.
# It is present in a class because it makes sense for the method to be present in class.
# A static method does not receive an implicit first argument.
class User:
    usingvariable='python developer'
    @staticmethod
    def method1():
        firstname = 'python'
        Lastname = 'developer'
        print(firstname, Lastname)
        print(usingvaraible)

        # static variable

User.method1()

# python developer
# NameError: name 'usingvaraible' is not defined
