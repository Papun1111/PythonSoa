import math

n = int(input("Enter the number of terms, n: "))
x = float(input("Enter the value of x (for series a and b): "))

sum_a = 1
sign = -1
for i in range(1, n + 1):
    term = (x ** (2 * i)) / math.factorial(2 * i)
    sum_a += sign * term
    sign *= -1

sum_b = 1
for i in range(1, n + 1):
    term = (x ** i) / math.factorial(i)
    sum_b += term

sum_c = 0
sign = 1
for i in range(n):
    sum_c += sign * (2 * i + 1)
    sign *= -1

print(f"Sum of series a (up to n terms): {sum_a}")
print(f"Sum of series b (up to n terms): {sum_b}")
print(f"Sum of series c (up to n terms): {sum_c}")
# Enter the number of terms, n: 4
# Enter the value of x (for series a and b): 3
# Sum of series a (up to n terms): -0.9747767857142857
# Sum of series b (up to n terms): 16.375
# Sum of series c (up to n terms): -4