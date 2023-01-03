# Try and Except statement is used to handle these errors within our code in Python. The try block is used to check some code for errors i.e the code inside the try block will execute when there is no error in the program.
# Whereas the code inside the except block will execute whenever the program encounters some error in the preceding try block.

l=[1,2,3,[22,33,4,5,6,['python','java','html','mysql'],12,13,14,15,['a','b','c']
    ,11,33,44,55,66],10,'general','purpose','class']


# print(l[20])
# IndexError: list index out of range

try:
    print(l[2])
except:
    print('list index error occred')
# list index error occred




