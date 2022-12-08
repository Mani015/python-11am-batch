# With out object creation
# __init__:__init__ method (or) Constructor in python.
# This method is automatically called to allocate memory when a new object instance of a class is created.
# All classes have __init__method.
class Mobile:
    def __init__(self,Mobile_Brand,Mobile_price,Mobile_color,Mobile_Ram,Mobile_Rom,Mobile_os):
        self.brand=Mobile_Brand
        self.price=Mobile_price
        self.color=Mobile_color
        self.ram=Mobile_Ram
        self.rom=Mobile_Rom
        self.os=Mobile_os


        print(self.price,
              self.brand,
              self.rom,
              self.color,
              self.os,
              self.ram)

Mobile('Nokia',12000,'blue',120,'6gb','andrioid')

