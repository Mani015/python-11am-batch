# Nested function:In python, we can defined a function inside another function .
# the fucntion with in another functuion is caleed a nested function
# the fucntion in which a nested function is defined is called an enclosed function
x=10
def f1():
    x=20
    print(x)
f1()
print(x)