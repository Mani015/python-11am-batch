def f1():
    n=1
    while n<=10:
        square=n*n
        yield square
        n+=1
ob=f1()
for i in ob:
    print(i,end=',')
# 1,4,9,16,25,36,49,64,81,100,
