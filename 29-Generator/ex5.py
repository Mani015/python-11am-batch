
n=int(input('Enter one number:'))

def f1(n):
    for i in range(1, 11):
        yield f'{n}*{i}={n*i}'

ob=f1(n)
# print(ob)
import sys


k=sys.getsizeof(ob)
print('size taken yiled :',k)
for k in ob:
    print(k)