
# APPEND
f1=open('file1.txt','r+')
# print(f1.write('it was developed by guido van rossum'))
print(f1.read())
f1.close()

# f2=open('file1.txt','w')
# a=f2.write('\n it is discoverd by 1991')
# print(a)
#
# f2.close()


f3=open('file1.txt','a')
x=f3.write('\n python is a object \noriented progtramming languge')
# print(x)

f3.close()