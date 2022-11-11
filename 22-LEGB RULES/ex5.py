x=10
def fun():
    global x
    x=20
    print(x)
fun()
print('updated global variable:',x)