# 1.single level inheritance

class parent_property:
    def pr1(self):
        print('This is parent property / '
              'and also we called as a super class')
class Child_Property():
    def pr2(self):
        print('THis is child property2/ '
              'and also called as a inherit or subclass')



ob1=parent_property()
ob1.pr1()
# This is parent property / and also we called as a super class

ob2=Child_Property()
ob2.pr2()
# THis is child property2/ and also called as a inherit or subclass