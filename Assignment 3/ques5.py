n=int(input("enter a postive number"))
def countNumbers(n):
    c=0
    a=n
    while(a>0):
        a=a//10
        c=c+1
    return c

count=countNumbers(n)  
print(f"there are {count} digits in number {n}")      