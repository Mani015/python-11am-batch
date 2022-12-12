class Car:
    carname='innova'
    carno=1230
    @staticmethod
    def m1(a,b):
        print('addition of a,b:',a+b)

        print(Car.carname)
        print(Car.carno)
Car.m1(10,20)
# addition of a,b: 30
# innova
1230