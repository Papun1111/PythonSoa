data=[1,2,3,2,3,4,4,4,5,4,5,6]
n=len(data)
sum=0
mode=data[0]
maxcount=0
for i in range(n):
    count=0
    for j in range(i+1,n):
        if data[i]==data[j]:
            count+=1
    if(maxcount>count):
        mode=data[i]
data=data.sort()
median=0
if(n%2==0):
    median=(data[n/2]+data[n//2+1])/2
else:
    median=data[(n+1)//2]
    
mean=sum/n

print(f"mean={mean},median={median},mode={mode}")
    
