x=20
def f1():
    x=30
    # print("enclosing variable:",y)
    def f2():
        # nonlocal y
        # y=50
        # print('local variable:',y)
        def f3():
            nonlocal y
            y=60
            # print(y)
        f3()
        # print('f2 variable:',y)
    f2()
    print('enclosing variable:',x)


f1()