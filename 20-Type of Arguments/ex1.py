# Keyword:There are arguments for which can be identifiyed by callers of the function using the parameters name's
def f1(a,b,c):
    print(a,b,c)
    # 10 20 30  a=10,b=20,c=30
    print(b,c,a)
    # 20 30 10   b=20,c=30,a=10
    print(c,a,b)
#     30 10 20   c=30,a=10,b=20
# f1(key=value,key=value,key=value)
f1(b=20,a=10,c=30)
# Keyword arguments it works as a depens on key = value
