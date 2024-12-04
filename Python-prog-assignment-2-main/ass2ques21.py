n = int(input("Enter a number: "))
if n < 1:
    print("No, the number is not a factorial number.")
else:
    factorial = 1
    i = 1
    while factorial < n:
        i += 1
        factorial *= i
    if factorial == n:
        print("Yes, the number is a factorial number.")
    else:
        print("No, the number is not a factorial number.")
# Enter a number: 120
# Yes, the number is a factorial number.