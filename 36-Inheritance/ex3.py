# Hybrid Inheritance
# When inheritance is consists of multiple types or a combination of different inheritance is called hybrid inheritance.

class Vehicle:
    def vehicle_info(self):
        print("Inside Vehicle class")

class Car(Vehicle):
    def car_info(self):
        print("Inside Car class")

class Truck(Vehicle):
    def truck_info(self):
        print("Inside Truck class")

# Sports Car can inherits properties of Vehicle and Car
class SportsCar(Car, Truck):
    def sports_car_info(self):
        print("Inside SportsCar class")

ob1=SportsCar()
ob1.car_info()
ob1.sports_car_info()
ob1.vehicle_info()
ob1.truck_info()

# Inside Car class
# Inside SportsCar class
# Inside Vehicle class
# Inside Truck class



