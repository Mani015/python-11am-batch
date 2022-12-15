import multipledispatch as multipledispatch
# import multipledispatch as dispatch


class parent:
    @multipledispatch.dispatch(int,int)
    def f1(self,x,y):
        print(x+y)
    @multipledispatch.dispatch(int,int,int)
    def f1(self,x,y,z):
        print(x+y+z)
    @multipledispatch.dispatch(str,str,int,int)
    def f1(self,x,y,z,a):
        print(x,y,z,a)



ob=parent()
ob.f1(10,20)
# ob.f1('python',10,20)
ob.f1('python','java',10,20)
