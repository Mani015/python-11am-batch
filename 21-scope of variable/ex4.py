# Scope of local variable:A local variable we declared in side of the function , and also we access the inside of the function

def f1():
    a=100
    print('local varaible:',a)
#     local varaible: 100
f1()
# inscase we are trying local variable 'a' ,acessing the out side of the function is not defined bcz, it'a local variable
print('local varaible:',a)
# NameError: name 'a' is not defined