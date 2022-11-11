x=10
def f1():
    # global x
    x=20
    print(x)
    def f2():
        global x
        x=300
    f2()
    print(x)
f1()
print(x)
