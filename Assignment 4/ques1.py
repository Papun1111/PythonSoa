import random
a=[]
n=int(input("enter size"))
for i in range(0,n):
    b=random.randrange(0,10)
    a.append(b)
sum=0
avg=0
for i in a:
    sum+=i
avg=sum/n
print(f"sum={sum} and average ={avg}")