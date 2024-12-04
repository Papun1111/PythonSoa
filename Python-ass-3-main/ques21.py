def calcFact(n):
    a=n
    prod=1
    while(a>0):
        prod=prod*a
        a=a-1
    return prod
n=int(input("Enter a number"))
a=calcFact(n)
print(f"factorial of {n} is {a}")    
# Enter a number5
# factorial of 5 is 120