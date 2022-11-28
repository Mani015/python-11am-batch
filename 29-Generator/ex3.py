def f1():
    yield 10
    yield 20
    yield 30
    yield 40
ob=f1()
print(ob.__next__())
print(ob.__next__())
print(ob.__next__())
print(ob.__next__())
# print(ob.__next__())
# 10
# 20
# 30
# 40
