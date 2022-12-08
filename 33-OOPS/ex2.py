# With object creation to calling method
class Mobile:
    def __init__(self,Mobile_Brand,Mobile_price,Mobile_color,Mobile_Ram,Mobile_Rom,Mobile_os):
        self.brand=Mobile_Brand
        self.price=Mobile_price
        self.color=Mobile_color
        self.ram=Mobile_Ram
        self.rom=Mobile_Rom
        self.os=Mobile_os


    def display(self):
        print(self.brand,self.os,self.ram,self.rom,self.color,self.price)

obj=Mobile('Nokia',12000,'blue',120,'6gb','andrioid')
obj.display()
ob2=Mobile('lenovo',15000,'black',16,'4gb','kitkat')
ob2.display()
