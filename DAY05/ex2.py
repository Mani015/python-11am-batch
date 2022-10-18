l=[1,2,3,4,5,6,7,8]
print(l)
# [1, 2, 3, 4, 5, 6, 7, 8]
l.append(22)
print(l)
# [1, 2, 3, 4, 5, 6, 7, 8, 22]
# add the single data item if the end of the list ,we are using append method
l.append(22,1)
print(l)
# TypeError: list.append() takes exactly one argument (2 given)