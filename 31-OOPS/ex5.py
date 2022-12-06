class Student_Details:
    fname='bharath'
    lname='kumar'
    Registerno=123456
    section='A-section'
    # print(fname)
    # print(lname)
    # print(Registerno)
    # print(section)
    def method1(self,New_section,register):
        self.section=New_section
        self.Registerno=register


ob1=Student_Details()
print(ob1.fname)
print(ob1.lname)
print(ob1.Registerno)
print(ob1.section)
print('After updating the section')
print('/////////////////////////////////////////////')
ob1.method1('b-section',00000000)
print(ob1.fname)
print(ob1.lname)
print(ob1.Registerno)
print(ob1.section)
ob2=Student_Details()
print(ob2.fname)
print(ob2.lname)
print(ob2.Registerno)
print(ob2.section)