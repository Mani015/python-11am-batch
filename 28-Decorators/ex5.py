
def f1(n):
    def f2():
        x=n()
        return 'square of x:',x**2
    return f2


@f1
def f3():
    return 5
ob=f3()
print(ob)

@f1
def f4():
    return 10
ob1=f4()
print(ob1)