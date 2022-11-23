# Decorator is a higer - order function,to modifying the existing function
# A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure.
# Decorators are usually called before the definition of a function you want to decorate.
def function1():
    return 'This  is function1 '

def function2():
    return function1()

# print(function2())
ob=function2()
print(ob)