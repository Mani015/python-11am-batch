# Exception:An unwanted and unexcpected event that distrubs, noraml flow of progrma is called exceptions

a1=int(input('enter 1st input:'))
a2=str(input('enter second input:'))

print(type(a1))
print(type(a2))

# print(a1+a2)
# ValueError: invalid literal for int() with base 10: 'l'


# In the above error to handle the try and except blocks:


try:
   print(a1+a2)
except:
    print('arjun marriage got fix')


# enter 1st input:123
# enter second input:arjun
# <class 'int'>
# <class 'str'>
# error occured


