# abstract base class used to as a blue print of for other classes
# if a project lot of classes and lot methods then developers create abstract class and use by the classes by inheritance
#
# Whrer we use:
# design level: we are creating class, if  the classes have same methods and implementations is different  then we create abstract class.
from abc import  ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def sides(self):
        pass
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

    def dimensional(self):
        print('this is 3 d dimensional ploygon')

class Rectangle(Polygon):
    def sides(self,lenght, breadth):
        self.lenght=lenght
        self.breadth=breadth
    def area(self):
        print(self.lenght * self.breadth)
    def perimeter(self):
        return 2*(self.lenght + self.breadth)


class Traingle(Polygon):
    def sides(self,a,b,c):
        self.side1=a
        self.side2=b
        self.side3=c
    def area(self):
        s=self.perimeter()
        return 2*((s-self.side1)*(s-self.side2)*(s-self.side3))
    def perimeter(self):
        return (self.side1+self.side3+self.side2)/2



ob1=Rectangle()
ob1.sides(10,20)
ob1.dimensional()
ob2=Traingle()
ob2.sides(11,11,11)
ob2.dimensional()


for i in [ob1,ob2]:
    print(i.area())
    print(i.perimeter())
