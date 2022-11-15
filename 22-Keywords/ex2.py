
student1='sai'
print('global variable:',student1)

def outsidefunction():
    global student1
    student2='vishnu'
    print('local variable:',student2)
    print('global variable:',student1)

outsidefunction()
print('global variable:',student1)

# global variable: sai
# local variable: vishnu
# # We are taken different name 'using the global and local ,while there is no update
# global variable: sai
# global variable: sai