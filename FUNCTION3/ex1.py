# z=20
# def f1():
#     global z
#     z=30
#     print('local variable:',z)
# f1()
# print(z)
# print('modifying the gloval keyword:',z)




list=[1,2,3,4,5,6]
def f1():
    global list
    list.append(7)
f1()
print('after using global keyword:',list)
