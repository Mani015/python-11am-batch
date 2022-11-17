
def f1(i):
    if i>=4:
        return True

k=list(filter(f1,range(1,20)))
print(k)
# [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
