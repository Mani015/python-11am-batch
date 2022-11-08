# Default: The default value of an arguments will bw used in side function, if you don't pass a value to that argunemts at the time of the function
def f1(k=11,l=12,m=13):
    print(k,l,m)
f1()
# 11 12 13
f1(l=20)
# 11 20 13
f1(m=100)
# 11,20,100
