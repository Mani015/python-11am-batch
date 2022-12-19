# dir() is a powerful inbuilt function in Python3,
# which returns list of the attributes and methods of any object (say functions , modules, strings, lists, dictionaries etc.)

# Syntax: object(dir())

# NAME MANGLING : atleast two leading underscore __a
# atmost one trailing underscore a_

# __a_       <========= this is the proper syntax

class XYZ:
    __a='lal'
    # '_XYZ__a'
    __b_='vishnu'
    # '_XYZ__b_'
    ___c='arjun'
    # '_XYZ___c'
    __d__='mahesh'
    # no name mangling--->'__d__'
    ___e___='hari'
    # no name mangling --->'___e___'
    ______f=100
#     '_XYZ______f'


ob=XYZ()
print(dir(XYZ))


# ['_XYZ______f', '_XYZ___c', '_XYZ__a', '_XYZ__b_', '___e___', '__class__', '__d__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',