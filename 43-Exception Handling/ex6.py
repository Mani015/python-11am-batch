n=int(input('enter one number:'))
a=[1,2,3,4,5,6,7,8,9]
try:
    print(a[n])
except ZeroDivisionError:
    print('zero dicision error')

except IndexError:
    print('index error ouucred')

print('this error ouucred maitaince')


# enter one number:10
# index error ouucred
# this error ouucred maitaince
