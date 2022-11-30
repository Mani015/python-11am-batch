# Search()
# To test the specified pattren is present not in the given input
import re
para1='class is a blue print of object'
# search='blue'

r=re.search(r'is',para1)
print(r)
# <re.Match object; span=(6, 8), match='is'>



print(re.search(r'print',para1))
# <re.Match object; span=(16, 21), match='print'>
print(re.search('oops',para1))
# None
