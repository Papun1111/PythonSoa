from statistics import mean, stdev

n = int(input("Enter the number of elements you want to enter: "))
l = []

for i in range(n):
    a = float(input("Enter a number: "))
    l.append(a)

meane = mean(l)
sample_deviation = stdev(l)

print("Mean:", meane)
print("Sample Standard Deviation:", sample_deviation)
