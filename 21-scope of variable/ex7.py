x1=100
print('global v:',x1)
# global v: 100
def f1():
    x=20
    # x=33333333
    print('enclosing variable:',x)
    # enclosing variable: 20
    print('global variable:',x1)
#     global variable: 100
    def f2():
        y=30
        print('local varaible:',y)
    #     local varaible: 30
        print('enclosing variable:', x)
        print('global variable:', x1)
        def f3():
            a=25
            print('local varaible:',a)
            print(x,x1,y)
        f3()
    f2()
    print('enclosing variable:', x)
f1()
print('global variable:',x1)
# global variable: 100
# print('local variable:',x)
# NameError: name 'x' is not defined
print(20)

