x=20
print('global va:',x)
def f1():
    x=30
    print('enclosed v:',x)
    def f2():
        global x
        x=40
        print('local variable:',x)
    f2()
    print('enclosing v:',x)
f1()
print('global variable:',x)

# global va: 20
# enclosed v: 30
# local variable: 40
# enclosing v: 30
# global variable: 40
