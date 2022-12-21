import datetime

d = datetime.date(2021, 10, 4)
print(d)

t = datetime.time(12,45)
print(t)

x = datetime.datetime.combine(d, t)
print(x)