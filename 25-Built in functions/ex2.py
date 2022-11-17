# Map

# Sytax: map(functiona name, iterables (or) sequence of values)
# iterables: list, tuple etc

l=[11,22,33,44,55,66,77,88,99]
def f1(i):
    return i**2


x=map(f1,l)
print(x)
# <map object at 0x0000023F9A61BF10>
# print(list(x))
# print(set(x))
print(tuple(x))
# (121, 484, 1089, 1936, 3025, 4356, 5929, 7744, 9801)