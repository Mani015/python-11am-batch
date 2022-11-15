x=10
print('global v:',x)
def f1():
    global x
    x=20
    print('local variable:',x)
f1()
print('global variable:',x)

# global v: 10
# local variable: 20
# global variable: 20