
def fun(i):
    if i>=3:
        return True

sai=[1,2,3,4,5,6,7,8,9,10,12,1314]

s=set(filter(fun,sai))
print(s)
# {1314, 3, 4, 5, 6, 7, 8, 9, 10, 12}
