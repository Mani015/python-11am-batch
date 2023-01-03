try:
    a1 = int(input('enter 1st input:'))
    a2 = int(input('enter second input:'))

    print(a1 / a2)
except ValueError:
    print('this is value error')
except ZeroDivisionError:
    print('Zero division error ')

except IndexError:
    print('index error')
else:
    print('i ll excute without any error')
finally:
    print('I will excute any time [with errors/without errors]')

print('excutuion successfully occured')