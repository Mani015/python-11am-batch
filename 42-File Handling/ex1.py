# file  hadling is an importtant part of any web applications
# The key function of working with files in python is the
# Syntax: open()
# open('filename','mode')

# x=To open a one new file
# r=open an exisiting file for a read operation'
# w=open an exisiting file for a write operation. if the file already contains some data then it will be overridden.
# a=open an eixisting file for a append operation.if won't overriden existing data

# r+=To read file and to write file
# a+=read and append


f1=open('ex2.py','x')
print(f1)

f1.close()
