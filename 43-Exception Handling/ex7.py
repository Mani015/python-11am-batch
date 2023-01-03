# try, except,...........else blocks:


n=int(input('enter one number:'))
a=[1,2,3,4,5,6,7,8,9]
try:
    print(a[n])
except ZeroDivisionError:
    print('zero dicision error')

except IndexError:
    print('index error ouucred')
else:
    print('i will excute with out any error')

print('this error ouucred maitaince')