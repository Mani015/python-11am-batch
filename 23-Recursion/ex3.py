# indirect recursion

def f1():
    print('function 1')
    f3()

def f2():
    print('Function 2')
    f2()

def f3():
    print('function 3')
    f1()

f1()
f2()
f3()

# function 1
# Function 2
# function 3
# Function 2
# function 3
# function 3