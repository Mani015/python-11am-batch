# Sytax: filter(functiona name, iterables (or) sequence of values)
l=[1,2,3,4,5,6,7,8,9]
def fun(i):
    if i%2==0:
        return True

z=filter(fun,l)
print(tuple(z))
# (2, 4, 6, 8)

