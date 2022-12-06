class Student_Details:
    # attribute and class variable
    fname='bharath'
    lname='kumar'
    Registerno=123456
    section='A-section'
    def school(self):
        print('this is method creation')


ob1=Student_Details()

print(ob1.fname)
print(ob1.lname)
print(ob1.Registerno)
print(ob1.section)


ob1.school()