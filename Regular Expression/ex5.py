# Findall (): To find duplicate specified pattren
import re
sen='Cricket is a bat-and-ball1 game2 played3 between two teams of eleven players' \
    ' on a field at the centre of which is a 22-yard (20-metre) pitch with a wicket at each end, ' \
    'each comprising two bails balanced on three stumps1. '
find='which'

a=re.findall(find,sen)
# print(a)


l=r'[a-zA-Z][0-9]'
print(re.findall(l,sen))
# ['l1', 'e2', 'd3', 's1']
