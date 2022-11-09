x=10
def outerfuction():
    x=12
    def insidefunction():
        y=20
        y=30
        print('local varaible',y)
        print('local varaible',y)
        print('local varaible:',x)
    insidefunction()
outerfuction()
print(x)