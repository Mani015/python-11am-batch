import sys
# sys:The sys modules provieds accesss to the system specific parameter and function

# print(sys.getrecursionlimit())


print(sys.setrecursionlimit(200))

def f1():
    print('this is function')
    f1()
f1()
