a=int(input("enter a number"))
b=int(input("enter another number"))

def Gcd(a,b):
    r=a%b
    while a%b!=0:
        a=b
        b=a
        r=a%b
    print(f"gcd is {b}")


Gcd(a,b)        
