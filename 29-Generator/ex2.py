# GENERATOR:Python provides a generator to create your own iterator function.
# A generator is a special type of function which does not return a single value,
# instead, it returns an iterator object with a sequence of values.
# In a generator function, a yield statement is used rather than a return statement.
# The following is a simple generator function.
def fun():
    yield 10
    yield 20
ob=fun()
print(ob)
# <generator object fun at 0x0000020283106F90>
print(next(ob))
# 10
print(next(ob))
# 20



