# self:self is used to represent the instance of class.
# with this keyword,you can accesse the attributes and methods of the class in python.
# it binds the attributes with the given argumetns.
# self is used to different placesesand often thought to be a keyword
class Student_Details:
    def instancemethod1(self,fname,lname,rollno):
        # syntax:object.attribute=value
        self.fname=fname
        self.lname=lname
        self.no=rollno

        print(self.fname)
        print(self.no)
        print(self.lname)



school=Student_Details()
school.instancemethod1('rajesh','kumar',1230)
