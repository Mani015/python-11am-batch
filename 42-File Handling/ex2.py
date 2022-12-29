
# x=To open a one new file

# f1=open('file1.txt','x')
# print(f1)
#
# f1.close()

# # r=open an exisiting file for a read operation'
f2=open('file1.txt','r')
print(f2.read())
f2.close()


#  w=open an exisiting file for a write operation. if the file already contains some data then it will be overridden.
# f3=open('file1.txt','w')
# a=f3.write('python is a general purpose porgramming languge')
# print(a)
# f3.close()