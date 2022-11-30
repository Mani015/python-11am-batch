# Sub function replace the matches with the text of your choice
import re


names=' pavan, sravani, pallavi, vamsi, rajesh, thusara'
s=re.sub('\s','-->CA',names)
# print(s)
players=' dhoni, jaddu, guikwad, ali, raina, chahar, doobe, rayudu'
x=re.sub('\s','-->CSK',players)
print('CSK TEAM:',x)

