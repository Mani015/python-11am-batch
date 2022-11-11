a='Global variable it can access entire function '
def function1():
    b='Local variable it access only inside of the function'
    print(b)
    print(a)
    def function2():
        c=120
        print(a)
    function2()
    print(a)
function1()
print(a)
