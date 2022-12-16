# Encapsulation is a mechanism of wrapping the data (variables) and code acting on the data (methods) together as a single unit.
# In encapsulation, the variables of a class will be hidden from other classes,
# and can be accessed only through the methods of their current class.



# Python Access Modifiers
# Let us see the access modifiers in Python to understand the concept of Encapsulation and data hiding −

# public
# private
# protected
# The public Access Modifier
# The public member is accessible from inside or outside the class.


class Finance:
    public_data1=100
    public_data2 = 'python'
    print('this is public datas we can use inside of class:',public_data1,public_data2)
    def m1(self):
        print('this is public data')

ob=Finance()

print('public data we can access the out isde of the class:',ob.public_data1,ob.public_data2)
ob.m1()
# this is public datas we can use inside of class: 100 python
# public data we can access the out isde of the class: 100 python
# this is public data