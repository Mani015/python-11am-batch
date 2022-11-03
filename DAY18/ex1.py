n=int(input('Enter one number:'))
i=0
while i<10:
    if n%6==0 and n%8==0:
        print(n)
        i=i+1
    n=n+1

print('loop completed')