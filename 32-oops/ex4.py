class Car:
    def __init__(self,Brandname,carcolor,carprice,carno):
        self.brand=Brandname
        self.color=carcolor
        self.price=carprice
        self.no=carno
        print(self.brand,
              self.color,
              self.no,
              self.price)

Car('suziki','blue',120000,1020)
