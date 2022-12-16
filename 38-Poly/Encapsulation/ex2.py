# The protected Access Modifier
# The protected member is accessible. from inside the class and its sub-class.
# Define a protected member by prefixing the member name with an underscore, for example −






class parent:
    _protectedmember=10
    def protectedmethod1(self):
        print(self._protectedmember)
class child(parent):
    def protectedmethod2(self):
        print(self._protectedmember)


ob1=parent()
ob1.protectedmethod1()
print(ob1._protectedmember)
print('--------------------------------------------')

ob2=child()
ob2.protectedmethod2()
print(ob2._protectedmember)
ob1.protectedmethod1()