x=20
def function1():
    x=30
    print(x)
    def function2():
        global x
        x=80
        print(x)
    function2()
    print(x)
function1()
print(x)