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
f1()
print('global variable:',x)

# enclosed v: 30
# local variable: 40
# global variable: 40