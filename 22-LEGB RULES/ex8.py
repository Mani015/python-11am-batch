y=10
def f1():
    # nonlocal y
    y=20
    # print('en v:',y)
    def f2():
        # global y

        y=30
        print('local v:',y)
        def f3():
            nonlocal y
            y='sai prasad'
            print('local :',y)
        f3()
        print('enclosing v:',y)
    f2()
    print('enclosing:',y)
f1()
# print('global v:',y)
# en v: 20
# local v: 30
# enclosing: 30
# global v: 10