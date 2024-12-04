def isEven(i):
    return i % 2 == 0

def squaresOfEven():
    s = 0
    for i in range(1, 51):
        if isEven(i):
            s += pow(i, 2)
    return s

sum_of_squares = squaresOfEven()
print(sum_of_squares)
