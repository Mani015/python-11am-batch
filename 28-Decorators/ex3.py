
def outerfunction(fun):
    def innerfunction():
        a=fun
        return a + 'python developer'
    return innerfunction



def concretefunction():
    return 'sai prasad'

ob=outerfunction(concretefunction())
print(ob())

# sai prasadpython developer