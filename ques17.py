from statistics import mean

n=int(input("enter number of elements you want to enter"))
l=[]
for i in range(1,n+1):
    a=int(input("Ener a number"))
    l.append(a)

meane=mean(l)

x_mean=[]

for i in l:
    minus=meane-i
    x_mean.append(pow(minus,2))

sum=0
for i in x_mean:
    sum+=i

deviation=pow((sum/n-1),(1/2))
print(deviation)


