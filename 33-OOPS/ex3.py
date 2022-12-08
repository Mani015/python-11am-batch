
class Employee:
    def m1(self):
        print('this method of employee')

ob1=Employee()
ob1.m1()
# TypeError: m1() takes 0 positional arguments but 1 was given
Employee.m1()
# TypeError: m1() takes 0 positional arguments but 1 was given

Employee.m1(ob1)
# this method of employee