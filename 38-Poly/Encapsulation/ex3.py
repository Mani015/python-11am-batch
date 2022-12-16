# The private Access Modifier
# The private member is accessible only inside class.
# Define a private member by prefixing the member name with two underscores, for example __a

class A:
    __privatedata='private data member'
    __a=100
    print(__a)
    print(__privatedata)


ob=A()
# 100
# private data member