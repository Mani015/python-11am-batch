# Static method:
# 1. static methods are general methods
# 2.To do general task
# 3.static methods are also used to do general task in class
# 4.static method doesn't perform operations on objects  & class varaibles
# 5.statitc method called utility function

class User:

    @staticmethod
    def method1():
        # static variables
        firstname='python'
        # static variable
        Lastname='developer'
        print(firstname,Lastname)

        # static variable

User.method1()
