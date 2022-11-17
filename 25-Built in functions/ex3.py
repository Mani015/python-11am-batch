
# def f1(i):
#     return i**3
#
# x=(1,2,3,4,5,6,7)
# a=list(map(f1,x))
# print(a)
# [1, 8, 27, 64, 125, 216, 343]

# def x(l):
#     return l**3
#
# k=map(x,[1,2,3,4,5,6])
# print(set(k))
# {64, 1, 8, 216, 27, 125}


# Using lambda :
x=list(map(lambda n:n**2,[1,2,3,4,5]))
# print(x)
# [1, 4, 9, 16, 25]

y=[23,1,45,62,78]
# print(list(map(lambda i:i**3,y)))
# [12167, 1, 91125, 238328, 474552]
print(tuple(map(lambda n:n**2,range(1,11))))
# (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# print(tuple(map(lambda i:3*i,range(1,11))))
