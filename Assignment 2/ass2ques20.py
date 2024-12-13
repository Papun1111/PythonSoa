
n = int(input("Enter an integer: "))


factor = 2

first_output = True

while factor * factor <= n:
    while n % factor == 0:
        if first_output:
            print(factor, end='')
            first_output = False
        else:
            print(", ", factor, end='', sep='')
        n //= factor
    factor += 1

if n > 1:
    if first_output:
        print(n)
    else:
        print(", ", n, sep='')

# Enter an integer: 21
# 3, 7