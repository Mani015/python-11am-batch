# Orbitary arguments:it will accept orbitary number of arguments this can be done by palceing star as prefix ti the arguents of function defination
def f1(*kw):
    print(kw)

# f1(1,2,3,4,5,6,7,8,9,10)
# (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
f1(1)
# 1,
f1('python','java','sql','html')