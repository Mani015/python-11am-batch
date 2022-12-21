import datetime

# Original Date
t = datetime.datetime.today()
print(t)

start = t.replace(year=1999, month=12, day=27)
print(start)

end = datetime.datetime(year=2021, month=10, day=3)
print(end)

d = (end-start)
print(d)
