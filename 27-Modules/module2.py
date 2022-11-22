# from module1 import addtiton,subtraction
# from module3 import multiplication,division
from module1 import *
from module3 import  *
a=int(input('Enter your first number:'))
b=int(input('Enter your second number:'))

x=int(input('Enter 1 is addition:,Enter 2 is subtraction:,Enter 3 is multiplication:,Enter 4 is division'))

if x==1:
    print(addtiton(a,b))

elif x==2:
    print(subtraction(a,b))
elif x==3:
    print(multiplication(a,b))
elif x==4:
    print(division(a,b))


else:
    print('you have enter wrong number')
# print('This is the one exaple of module')
