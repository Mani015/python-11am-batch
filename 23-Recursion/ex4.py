
def f1(n):
    if n==1:
        return 1
    else:
        return n+f1(n-1)



ob=f1(10)
print(ob)