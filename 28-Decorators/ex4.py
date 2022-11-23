def outerfunction(fun):
    def innerfunction():
        a=fun()
        return a + 'python developer'
    return innerfunction


@outerfunction
def concretefunction():
    return 'sai prasad'

ob=concretefunction()
print(ob)
@outerfunction
def lal():
    return 'lalsingh'
ob1=lal()
print(ob1)