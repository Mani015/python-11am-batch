import time

localtime = time.localtime()

t = time.strftime("%H", localtime)
print(t)

t = time.strftime("%I", localtime)
print(t)

t = time.strftime("%j", localtime)
print(t)

t = time.strftime("%m", localtime)
print(t)

t = time.strftime("%p", localtime)
print(t)

t = time.strftime("%w", localtime)
print(t)

t = time.strftime("%x", localtime)
print(t)

t = time.strftime("%X", localtime)
print(t)

t = time.strftime("%c", localtime)
print(t)

t = time.strftime("%y", localtime)
print(t)

t = time.strftime("%Y", localtime)
print(t)

t = time.strftime("%Z", localtime)
print(t)