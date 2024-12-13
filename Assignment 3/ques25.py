def CheckCoprime(n,m):
    maxi=max(n,m)
    mini=min(n,m)
    c=0
    for i in range (1,mini+1):
        if maxi%i==0 and mini %i==0:
            c+=1
    if(c!=1):
        return False
    return True
n=int(input("Enter First Number"))
m=int(input("Enter 2ND Number"))
print(CheckCoprime(n,m))
# Enter First Number14
# Enter 2ND Number15
# True