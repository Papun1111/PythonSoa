num=int(input("enter a number"))
r=0
a=num
d=0
while(a>0):
    d=a%10
    r=r*10+d
    a//=10
    
print(f"reverse of {num} is {r}")    
# enter a number1234
# reverse of 1234 is 4321