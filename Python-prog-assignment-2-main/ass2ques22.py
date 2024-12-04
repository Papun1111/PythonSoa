n=int(input("enter a number"))

a=n
d=0
sum=0
val=True
while val:
    while(a>0):
        d=a%10
        sum+=d
        a=a//10
    if(sum<10):
        val=False
    else:
        a=sum
        sum=0
print(sum)        
