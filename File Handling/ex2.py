# Write : open the file for reading ,handle is positioned at least
# cursor the file if the file does'nt exit

w=open('f2.txt','w')
x=w.write('python is object oriented programming language,\n also genreral purpose programming language')
print(x)

w.close()
