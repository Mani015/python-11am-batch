# Using return keyword to develop a table
n=int(input('Enter one number:'))
def f1(n):
    list=[]
    for i in range(1,11):
        list.append(f'{n}x{i}={n * i}')
    return list
# n=int(input('Enter one number:'))
renuka=f1(n)
import sys


k=sys.getsizeof(renuka)
print('size taken:',k)
for i in renuka:
    print(i)