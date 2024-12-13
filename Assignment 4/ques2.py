def rotate(x, y, z):
    return (z, x, y)

a, b, c = 'Doug', 22, 1984

a, b, c = rotate(a, b, c)
print(a, b, c)

a, b, c = rotate(a, b, c)
print(a, b, c)

a, b, c = rotate(a, b, c)
print(a, b, c)
