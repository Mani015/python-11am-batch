# File handling is a cursor, which define from where the data has to be read ot write in file
# Syntax: open('filename','mode')
# modes:
# 1.X is open for file
# 2. W is write an exisiting file
# 3. r is read for an exisiting file
# 4.a append is adding the data of an existing file


# 'x' ------> open file
file=open('f1.txt','x')
print(file)