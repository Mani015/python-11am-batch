import time

t = time.ctime()
print(t)

localtime = time.localtime()

# Abbreviated weekday Name
t = time.strftime("%a", localtime)
print(t)

# Full weekday Name
t = time.strftime("%A", localtime)
print(t)

# Full Month Name
t = time.strftime("%B", localtime)
print(t)

# Abbreviated Month Name
t = time.strftime("%b", localtime)
print(t)