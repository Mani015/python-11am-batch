# To creating object
class Student_Details:
    # attribute and class variable
    fname='bharath'
    lname='kumar'
    Registerno=123456
    section='A-section'
    def school(self):
        print('this is method creation')


Student_Details
print(Student_Details.fname)


# syntax= object name=classname ()
object_1=Student_Details()

# TO method calling
# syntax:object name. method name
object_1.school()
