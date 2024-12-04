def checkPerfect(n):
    a=n
    sum=0
    while(a>0):
        d=a%10
        sum+=d
        a=a//10
    if sum==n:
        return True
    return False

n=int(input("Enter a number"))
print(checkPerfect(n))
# Enter a number6
# True