
def fun1(x):
    print('square of x:',x**2)

def fun2(y):
    print('cube of y:',y**3)

def decorete(function):
    return (function)

# print(decorete(fun2(10)))
decorete(fun1(10))
decorete(fun2(5))
