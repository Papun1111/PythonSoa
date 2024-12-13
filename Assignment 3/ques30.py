def prodDigits(n):
    a=n
    prod=1
    while(a>0):
        d=a%10
        prod*=d
        a=a//10
    return prod

n=int(input("Enter a number"))
print(prodDigits(n))
# Enter a number123
# 6