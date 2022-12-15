class Multiplication:
    def m1(self,x,y,z):
        print(x*y+z)

    def m1(self,a,b):
        print(a*b)

ob=Multiplication()
# ob.m1(10,20,30)
# TypeError: m1() takes 3 positional arguments but 4 were given


ob.m1(10,30)
# 300