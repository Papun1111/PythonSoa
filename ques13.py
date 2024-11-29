l = [(1, 10, 3), (4, 5, 6), (7, 8, 9)]

def func(t):
    return t[1]

l.sort(key=func)
print(l)
