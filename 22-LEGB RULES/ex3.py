a=10
def localfunction():
    global a
    a=20
    print(a)
localfunction()
print(a)