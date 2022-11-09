# Scope of Global variable:a variable declared out side of the function , we can use (or)access any whrere
a=10
print('Global varaible:->S1:',a)
def f1():

    print('globa variable:->s2',a)


f1()
print('Global varaible:->s3',a)

