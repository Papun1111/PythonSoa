n=int(input("enter a number"))

sum=0
for i in range(1,n+1,1):
    count=0;
    for j in range(1,i+1,1):
        if(i%j==0):
            count+=1
    if(count==2):
        sum=sum+i

print(f"sum of all prime numbers less than {n} is {sum}")
