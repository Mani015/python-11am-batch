
# a1=int(input('enter 1st input:'))
# a2=int(input('enter second input:'))

try:
    a1 = int(input('enter 1st input:'))
    a2 = int(input('enter second input:'))

    print(a1 + a2)
except ValueError:
    print('this is value error')
except ZeroDivisionError:
    print('Zero division error ')

except IndexError:
    print('index error')

print('excutuion successfully occured')

# enter 1st input:12
# enter second input:kl
# this is value error
# excutuion successfully occured


