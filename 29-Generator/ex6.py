n=int(input('Enter one number:'))

def f1(n):
    for i in range(1, 11):
        return f'{n}*{i}={n*i}'

ob=f1(n)
# print(ob)
for k in ob:
    print(k)