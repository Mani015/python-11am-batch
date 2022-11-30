# Match is used to test the input string start with specified pattren or not

import re

para1='python is a general purpose programming language'

r=re.match(r'python is a',para1)
print(r)
# <re.Match object; span=(0, 6), match='python'>



# print(re.match('python',para1))