while True:
    n=int(input("enter a number"))
    if(n>0):
        break        

if(n%2==0):
    n=n*2
else:
    n=pow(n,2)

print(n)    
